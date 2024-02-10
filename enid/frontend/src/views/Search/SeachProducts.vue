<template>
  <div class="bg-white py-10 sm:px-10 mt-3 md:mt-5">
    <div
      id="top-sellers"
      class="grid grid-cols-1 lg:grid-cols-4 gap-x-2 gap-y-2 lg:gap-y-0"
    >
      <ProductCart
        v-if="api"
        :api="api"
        @open_shopping_cart_product_list="handlerOpenShoppingCart"
        :key="api" 
      />
    </div>
  </div>
</template>

<script>
import ProductCart from "@/components/Products/ProductCart.vue";
export default {
  components: {
    ProductCart,
  },  
  data() {
    return {
      open: false,      
      api: null
    };
  },
  watch: {
    '$route.params.q': function(newQ, oldQ) {
      this.api = `search/product/${newQ}/`;
    }
  },
  mounted() {
    this.api = `search/product/${this.$route.params.q}/`;
  },
  methods: {    
    handlerOpenShoppingCart() {
      this.$emit("open_shopping_cart_product_list");
    },
  },  
};
</script>
