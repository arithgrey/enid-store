<template>
  <div>
  <Banner />
  <BannerOffert />
  <div class="">
    <div class="mx-auto xs:w-full md:w-10/12">
      <ProductList />
    </div>
  </div>
  <TrusthHome />  
  </div>
</template>

<script>
import ProductList from "@/components/Products/ProductList.vue";
import Banner from "@/components/Banner/Banner.vue";
import BannerOffert from "@/components/Banner/BannerOffert.vue";
import TrusthHome from "@/components/Trusth/TrusthHome.vue";
//import ShoppingCartList from "@/components/Cart/ShoppingCartList.vue";
import App from '../../App.vue';

export default {
  components: {
    ProductList,
    Banner,
    BannerOffert,
    TrusthHome    
  },
  data() {},
};
</script>
