import axios from 'axios';

const localBaseUrl = 'http://127.0.0.1:8000/api/';
const productionBaseUrl = 'http://enidservice.com:8000/api/';
const apiBaseUrl = import.meta.env.VITE_APP_LOCAL ? localBaseUrl : productionBaseUrl;

const axiosInstance = axios.create({
  baseURL: apiBaseUrl, 
  headers: {    
    'Content-Type': 'application/json',
  },   
});

export default axiosInstance;