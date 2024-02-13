<template>
  <div>
    <div class="text-1xl font-bold mt-3" v-if="category">
      {{ category }}
    </div>
    <button
      v-for="product in products"
      :key="product.id"
      :value="product.id"
      :class="[
        'py-2.5',
        'px-4',
        'mt-2',
        'mr-2',
        'text-gray-900',
        'bg-transparent',
        'border-2',
        'border-gray-300',
        'hover:bg-gray-200',
        'dark:border-gray-600',
        'dark:hover:bg-gray-100',
        'focus:outline-none',
        'focus:ring-0',
        { 'border-blue-600': currentProduct === product.id },
      ]"
      @click="showProduct(product)"
    >
      {{ product.name_product_group }}
    </button>
  </div>
</template>

<script>
export default {
  props: {
    currentProduct: {
      type: Number,
      required: true,
    },
    product_group: {
      type: Number,
      required: true,
    },
  },

  data() {
    return {
      products: [],
      category: null,
    };
  },

  mounted() {
    if (this.product_group) {
      this.fetchProductsGroup();
    }
  },

  watch: {
    product_group: {
      immediate: true,
      handler(newVal) {
        if (newVal) {
          this.fetchProductsGroup();
        }
      },
    },
  },

  methods: {
    async fetchProductsGroup() {
      try {
        const response = await this.$axios.get(
          `/product-group/${this.product_group}/products/`
        );
        this.products = response.data.products;
        this.category = response.data.category;
      } catch (error) {
        console.error("Error fetching products on group:", error);
      }
    },
    showProduct(product) {
      this.$router.push({
        name: "product-detail",
        params: {
          categorySlug: product.category.slug,
          productSlug: product.slug,
        },
      });
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    },
  },
};
</script>
