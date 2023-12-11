<template>
  <div
    class="mt-10 lg:mt-12 grid grid-cols-1 lg:grid-cols-3 gap-x-8 gap-y-10 lg:gap-y-0"
  >
    <div
      v-for="(item, index) in products"
      :key="index"
      class="flex flex-col mt-20"
    >
      <div class="relative">
        <img :src="item.path_main_image" :alt="item.name" class="block" />
      </div>
      <div class="mt-6 flex justify-between items-center">
        <div class="flex justify-center items-center">
          <p
            class="tracking-tight text-2xl font-semibold leading-6 text-gray-800"
          >
            {{ item.short_name }}
          </p>
        </div>
        <div class="flex justify-center items-center">
          <button
            aria-label="show menu"
            @click="toggleShow(index)"
            class="focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-800 py-2.5 px-2 bg-gray-800 text-white hover:text-gray-400"
          >
            <svg
              v-if="item.show"
              :id="'chevronUp' + index"
              class="fill-stroke"
              width="10"
              height="6"
              viewBox="0 0 10 6"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M9 5L5 1L1 5"
                stroke="currentColor"
                stroke-width="1.25"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
            <svg
              :id="'chevronDown' + index"
              v-if="!item.show"
              class="fill-stroke"
              width="10"
              height="6"
              viewBox="0 0 10 6"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M1 1L5 5L9 1"
                stroke="currentColor"
                stroke-width="1.25"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </button>
        </div>
      </div>
      <div
        v-if="item.show"
        :id="'menu' + index"
        class="flex flex-col jusitfy-start items-start mt-12"
      >
        <ProductVarianList :product="item" />
        <div
          class="flex jusitfy-between flex-col lg:flex-row items-center mt-10 w-full space-y-4 lg:space-y-0 lg:space-x-4 xl:space-x-8"
        >
          <div class="w-full">
            <button
              class="focus:outline-none focus:ring-gray-800 focus:ring-offset-2 focus:ring-2text-gray-800 w-full tracking-tight py-4 text-lg leading-4 hover:bg-gray-300 hover:text-gray-800 bg-white border border-gray-800"
            >
              Más info
            </button>
          </div>
          <div class="w-full">
            <button
              class="focus:outline-none focus:ring-gray-800 focus:ring-offset-2 focus:ring-2 text-white w-full tracking-tight py-4 text-lg leading-4 hover:bg-black bg-gray-800 border border-gray-800"
            >
              Añador al carrito
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProductVarianList from "@/components/Variants/ProductVarianList.vue";
export default {
  components: {
    ProductVarianList,
  },
  data() {
    return {
      products: [],       
    };
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await this.$axios.get(`productos`);
        this.products = response.data.map((product) => ({
          ...product,
          show: false, // Inicializar show como false para cada producto
          code: `FENID-0${product.id}`,
        }));
      } catch (error) {
        console.error("Error products FAQ list:", error);
      }
    },
    toggleShow(index) {
      this.products.forEach((product, i) => {
        product.show = index === i && !product.show;
      });
    },
  },
};
</script>
