import { createRouter, createWebHistory } from 'vue-router';
import MainLayout from '@/layouts/MainLayout.vue'; 
import FaqList from '@/views/Faq/FaqList.vue';
import ReturnsList from '@/views/Faq/Returns/ReturnsList.vue'
import ReturnsDetail from '@/views/Faq/Returns/ReturnsDetail.vue'
import SeachOrders from '@/views/SearchOrders/Form.vue'
import ProductList from '@/views/Product/ProducList.vue'
import Checkout from '@/views/checkout/Checkout.vue'
import ProductDetail from '@/views/Product/ProductDetail.vue'
import References from '@/views/References/ReferencesList.vue'
import OrderDetail from '@/views/Order/OrderDetail.vue'
import UserArea from '@/views/UserArea/Area.vue'
import SeachProducts from '@/views/Search/SeachProducts.vue';
import ProductsSearchByCategory from '@/views/Search/ProductsSearchByCategory.vue';
import AccountEcommerce from '@/views/Account/Ecommerce.vue';
import SearchLead from '@/views/Leads/Search.vue';
import Searchorders from '@/views/Order/Search.vue';


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
        path: 'checkout',
        name: 'checkout',
        component: Checkout,
      },
      {
        path: '/',
        name: 'product-list',
        component: ProductList,
      },
      { 
        path: '/:categorySlug/',
        name: 'products-by-category',
        component: ProductsSearchByCategory,       
      },  
      {
        path: '/:categorySlug/:productSlug',
        name: 'product-detail',
        component: ProductDetail,        
      },
      {
        path: 'referencias',
        name: 'referencias',
        component: References,        
      },
      {
        path: '/orden-compra/:id',
        name: 'order-detail',
        component: OrderDetail,        
      },
      {
        path: '/user-area/',
        name: 'user-area',
        component: UserArea,        
      },
      {
        path: '/search/products/:q',
        name: 'search-product',
        component: SeachProducts,        
      },
      {
        path: '/account',
        name: 'ecommerce-user',
        component: AccountEcommerce,
        meta:{requiresAuth: true}
        
      },
      {
        path: '/search-leads/',
        name: 'search-lead',
        component: SearchLead,
        meta:{requiresAuth: true}
        
      },
      {
        path: '/search-orders/',
        name: 'search-orders',
        component: Searchorders,
        meta:{requiresAuth: true}
        
      },
    
    ],
   
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
