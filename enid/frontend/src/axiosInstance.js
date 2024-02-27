import axios from 'axios';

  const apiBaseUrl = import.meta.env.VITE_APP_API;

  const axiosInstance = axios.create({
    baseURL: apiBaseUrl, 
    headers: {    
      'Content-Type': 'application/json',
    },   
  });


  axiosInstance.interceptors.request.use(
    config => {
      
      const requiresToken = config.url.includes('/api/');        
      config.headers['X-Store-Id'] = 1;          

      if (requiresToken) {

        const token = localStorage.getItem('token');
        
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
      }
    
      
      return config;
    },
    error => {
      return Promise.reject(error);
    }
  );



  axiosInstance.interceptors.response.use(
    response => {
      return response;
    },
    async error => {
      
      const originalRequest = error.config;
      if (error.response.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;
  
        try {
          
          const refreshToken = localStorage.getItem('refresh_token');
          const response = await axiosInstance.post('login/refresh-token/', { refresh_token: refreshToken });                    
          const newAccessToken = response.data.access_token;

          localStorage.setItem('token', newAccessToken);          
          originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;

          return axiosInstance(originalRequest);
        } catch (refreshError) {
          
          console.error('Error al intentar actualizar el token de acceso:', refreshError);
          
        }
      }
  
      return Promise.reject(error);
    }
  );
  export default axiosInstance;