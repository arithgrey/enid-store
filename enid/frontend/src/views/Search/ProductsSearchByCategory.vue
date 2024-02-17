<template>
<div class="container mx-auto px-4">
  <div class="bg-white py-10 sm:px-10 mt-3 md:mt-5">
    <nav aria-label="Breadcrumb">
      <ol role="list" class="flex max-w-2xl items-center space-x-2 mb-3 w-full">
        <li>
          <div class="flex items-center">
            <h1
              class="mr-2 font-medium text-gray-900 uppercase"
              v-if="categoryName"
            >
              {{ categoryName }}</h1
            >            
          </div>
        </li>      
      </ol>
    </nav>
    <div
      id="product-categoryes"
      class="grid grid-cols-1 lg:grid-cols-3 gap-x-2 gap-y-2 lg:gap-y-0"
    >
      <ProductCart
        v-if="api"
        :api="api"
        @open_shopping_cart_product_list="handlerOpenShoppingCart"
        :key="api"
      />
    </div>
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
      api: null,
      categoryName:null,
    };
  },
  watch: {
    "$route.params.categorySlug": function (newQ, oldQ) {
      this.api = `product-category/${newQ}/`;      
      this.categoryName = newQ.replace(/-/g, " ");
    },
  },
  mounted() {
    this.api = `product-category/${this.$route.params.categorySlug}/`;
    this.categoryName = this.$route.params.categorySlug.replace(/-/g, " ");
    
  },
  methods: {
    handlerOpenShoppingCart() {
      this.$emit("open_shopping_cart_product_list");
    },
  },
};
</script>
