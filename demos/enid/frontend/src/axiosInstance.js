import axios from 'axios';

const apiBaseUrl = import.meta.env.VITE_APP_API;

const axiosInstance = axios.create({
  baseURL: apiBaseUrl, 
  headers: {    
    'Content-Type': 'application/json',
  },   
});

export default axiosInstance;
