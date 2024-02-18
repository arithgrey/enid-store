<template>
  <ul
    role="list"
    :aria-labelledby="`sport-in-house-heading`"
    class="mt-6 space-y-6 sm:mt-4 sm:space-y-4"
  >
    <li v-for="item in product_categories" :key="item.name" class="flex">
      <router-link
        :to="{
          name: 'products-by-category',
          params: {
            categorySlug: item.slug,
          },
        }"
        @click="filterCategory"
      >
        <span class="-m-2 block p-2 text-gray-500">{{ item.name }} </span>
      </router-link>
    </li>
  </ul>
</template>
<script>
export default {
  data() {
    return {
      product_categories: {},
    };
  },
  model: {
    event: "open_cart",
  },
  mounted() {
    this.fetchProductCategories();
  },
  methods: {
    async fetchProductCategories() {
      try {
        const response = await this.$axios.get("categorias");
        this.product_categories = response.data.map((category) => ({
          ...category,
          href: `${category.slug}`,
        }));
      } catch (error) {
        console.error("Error category products list:", error);
      }
    },
    filterCategory(){
      this.$emit("close_filters");
    }
  },
};
</script>