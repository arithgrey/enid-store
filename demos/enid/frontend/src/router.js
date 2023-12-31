import { createRouter, createWebHistory } from 'vue-router';
import MainLayout from '@/layouts/MainLayout.vue'; 
import FaqList from '@/views/Faq/FaqList.vue';
import ReturnsList from '@/views/Faq/Returns/ReturnsList.vue'
import ReturnsDetail from '@/views/Faq/Returns/ReturnsDetail.vue'
import SeachOrders from '@/views/SearchOrders/Form.vue'
import ProductList from '@/views/Product/ProducList.vue'

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
        component: SeachOrders,
      },
      {
        path: '/',
        name: 'product-list',
        component: ProductList,
      },

    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
