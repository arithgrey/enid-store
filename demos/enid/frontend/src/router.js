import { createRouter, createWebHistory } from 'vue-router';
import MainLayout from '@/layouts/MainLayout.vue'; // Ajusta la ruta según la estructura de tu proyecto
import FaqList from './views/Faq/FaqList.vue';

const routes = [
  {
    path: '/',
    component: MainLayout,
    children: [
      {
        path: 'faq',
        component: FaqList,
      },
      // Otras rutas pueden ir aquí
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
