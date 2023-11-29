<template>
  <div class="min-h-screen flex flex-col">
    
    <ShippingAndReturns />
    <div class="flex-grow sm:py-12">      
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