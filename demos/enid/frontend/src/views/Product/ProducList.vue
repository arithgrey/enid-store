<template>
  <div>
    <Banner />
    <BannerOffert />
    <div class="mx-auto xs:w-full md:w-10/12 p-5 md:p-0">
      <ProductList @open_shopping_cart_product_list="handleOpenCartProductList" />
    </div>
    <div class="mx-auto xs:w-full">
      <TrusthHome />
      <Community />      
    </div>
    
  </div>
</template>

<script >
import ProductList from "@/components/Products/ProductList.vue";
import Banner from "@/components/Banner/Banner.vue";
import BannerOffert from "@/components/Banner/BannerOffert.vue";
import TrusthHome from "@/components/Trusth/TrusthHome.vue";
import Community from "@/components/Trusth/Community.vue";


export default {
  components: {
    ProductList,
    Banner,
    BannerOffert,
    TrusthHome,
    Community,
    
  },
  methods: {
    handleOpenCartProductList() {      
      this.$emit("open_shopping_cart_product_list");
    },
  },
};
</script>
