<template>
  <div class="bg-white py-10 sm:px-10 mt-3 md:mt-5" id="top-sellers">
    <div class="grid">
      <h3 class="text-5xl font-semibold leading-5 text-gray-900 uppercase">
        {{ title }}
      </h3>

      <h3 class="text-5xl font-semibold text-gray-900 uppercase mt-5">
        Los populares
      </h3>
    </div>
    <div      
      class="grid grid-cols-1 lg:grid-cols-2 gap-x-2 gap-y-2 lg:gap-y-0"
    >
      <ProductCart
        :api="api"
        @open_shopping_cart_product_list="handlerOpenShoppingCart"
      />
    </div>
    <div></div>
  </div>
</template>

<script>
import ProductCart from "@/components/Products/ProductCart.vue";

export default {
  components: {
    ProductCart,
  },
  props: {
    title: {
      type: String,
      default: "Ya sabes..",
    },
  },
  data() {
    return {
      open: false,
      api: "productos/top-sellers",
    };
  },

  methods: {
    handlerOpenShoppingCart() {
      this.$emit("open_shopping_cart_product_list");
    },
  },
};
</script>
