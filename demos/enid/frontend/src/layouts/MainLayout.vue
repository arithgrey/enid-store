<template>

<div>  
    <div class="fixed top-0 left-0 right-0 z-50 bg-white ">
      
      <!-- Contenido del menú aquí -->
      <ShippingAndReturns @open_shopping_cart="handleOpenCart" />
    </div>
    <div class="relative mt-32 mb-8">
      <!-- Contenido de la página aquí -->
      <div class="relative">
        <router-view @open_shopping_cart_product_list="handleOpenCartOnViews" />
      </div>
      <ShoppingCartList ref="shoppingCartList" />
      <div class="flex-shrink-0">
        <Footer v-if="display_footer" />
      </div>
    </div>
  </div>
</template>

<script>
import ShippingAndReturns from "@/components/Banner/ShippingAndReturns.vue";
import ShoppingCartList from "@/components/Cart/ShoppingCartList.vue";

import Footer from "@/layouts/Footer.vue";

export default {
  components: {
    ShippingAndReturns,
    ShoppingCartList,
    Footer,
  },
  data(){
    return {
      display_footer: true
    }
  },
  methods: {
    handleOpenCart() {      
      this.$refs.shoppingCartList.openCart(); // Llamar al método openCart de ShoppingCartList
    },
    handleOpenCartOnViews(){
      this.$refs.shoppingCartList.openCart();
    }
  },
};
</script>
