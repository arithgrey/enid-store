import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import router from './router'; // Importa el archivo de rutas
import axiosInstance from "@/axiosInstance";

const app = createApp(App);

app.use(router);
app.config.globalProperties.$axios = axiosInstance;

app.mount('#app');
