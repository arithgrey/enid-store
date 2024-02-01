<template>
  <div>
    <ProductDetail @open_shopping_cart_product="handle_open_shoping_cart"/>    
  </div>
</template>

<script >
import ProductDetail from "@/components/Products/ProductDetail.vue";


export default {
  components: {
    ProductDetail,    
  },
  methods: {        
    handle_open_shoping_cart(){
      
      this.$emit("open_shopping_cart_product_list");
    }
  },
};
</script>
