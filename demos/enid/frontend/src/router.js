import { createRouter, createWebHistory } from 'vue-router';
import FaqList from './views/Faq/FaqList.vue';


const routes = [
  { path: '/faq', component: FaqList },  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;