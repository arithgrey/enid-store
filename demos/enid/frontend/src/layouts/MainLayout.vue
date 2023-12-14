<template>
  <div class="min-h-screen flex flex-col">    
    <div class="fixed top-0 left-0 right-0 z-50">
    <ShippingAndReturns/>
    </div>
    <div class="flex-grow sm:py-12 w-96 md:w-full mx-auto md:mx-0 ">      
      <router-view />
    </div>
    <div class="flex-shrink-0">
      <Footer />
    </div>
  </div>
</template>

<script>
import ShippingAndReturns from "@/components/Banner/ShippingAndReturns.vue";
import Footer from "@/layouts/Footer.vue";
/* En tu archivo de estilos principal */


export default {
  components: {
    ShippingAndReturns,
    Footer,    
  },
  // Otras configuraciones del layout
};
</script>

<style scoped>


</style>