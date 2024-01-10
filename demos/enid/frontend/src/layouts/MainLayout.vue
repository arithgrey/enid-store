<template>
  <div class="min-h-screen flex flex-col">
    <div class="fixed top-0 left-0 right-0 z-50">
      <ShippingAndReturns @open_shopping_cart="handleOpenCart" />
    </div>
    <div class="flex-grow sm:py-12 w-96 md:w-full mx-auto md:mx-0">
      <router-view 
      @open_shopping_cart_product_list="handleOpenCartOnViews"      
      />
    </div>
    <ShoppingCartList ref="shoppingCartList" />
    <div class="flex-shrink-0">
      <Footer v-if="display_footer"/>
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
