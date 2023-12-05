import { createRouter, createWebHistory } from 'vue-router';
import MainLayout from '@/layouts/MainLayout.vue'; 
import FaqList from '@/views/Faq/FaqList.vue';
import ReturnsList from '@/views/Faq/Returns/ReturnsList.vue'
import ReturnsDetail from '@/views/Faq/Returns/ReturnsDetail.vue'

const routes = [
  {
    path: '/',
    component: MainLayout,
    children: [
      {
        path: 'faq',
        component: FaqList,
      },
      {
        path: 'cambios-y-devoluciones',
        component: ReturnsList,        
      },
      {
        path: '/cambios-y-devoluciones/:id',
        name: 'cambios-y-devoluciones',
        component: ReturnsDetail,
      },
      {
        path: 'rastreo',
        name: 'rastreo',
        component: [],
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
