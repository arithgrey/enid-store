<template>
    <div
        v-for="(item, index) in products"
        :key="index"
        class="flex flex-col mt-10"
      >
        <div class="relative">
           <router-link
                :to="{
                  name: 'product-detail',
                  params: {
                    categorySlug: item.category.slug, 
                    productSlug: item.slug,
                  },
                }">
          <img
            :src="getMainImage(item)"
            :alt="item.name"
            class="block w-full h-auto"
          />
           </router-link>
        </div>
        <div class="mt-6 flex justify-between items-center">
          <div class="flex justify-center items-center">
            <p
              class="tracking-tight text-5xl font-semibold leading-12 text-slate-950"
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
              <router-link
                :to="{
                  name: 'product-detail',
                  params: {
                    categorySlug: item.category.slug,
                    productSlug: item.slug,
                  },
                }">
                <button class="focus:outline-none focus:ring-gray-800 focus:ring-offset-2 focus:ring-2text-gray-800 w-full tracking-tight py-4 text-lg leading-4 hover:bg-gray-300 hover:text-gray-800 bg-white border border-gray-800">
                Más info
                </button>
              </router-link>
            </div>
            <div class="w-full">
              <button
                @click="addToCart(item)"
                class="focus:outline-none focus:ring-gray-800 focus:ring-offset-2 focus:ring-2 text-white w-full tracking-tight py-4 text-lg leading-4 hover:bg-black bg-gray-800 border border-gray-800"
              >
                Añadir al carrito
              </button>
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
  props: {
  
    api: {
      type: String,
      required:true
    },
  },
  data() {
    return {
      open: false,
      products:[],
    };
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await this.$axios.get(this.api);
        const paginator = response.data;
                
        this.products = paginator.results.map((product) => ({ 
          ...product,
          show: false,
          code: `FENID-0${product.id}`,
        }));
      } catch (error) {
        console.error("Error products  list:", error);
      }
    },
    addToCart(product) {
      this.$emit("open_shopping_cart_product_list");
      return this.$store.commit("addToCart", product);
    },
    toggleShow(index) {
      this.products.forEach((product, i) => {
        product.show = index === i && !product.show;
      });
    },
    getMainImage(item) {
      const mainImage = item.images.find((img) => img.is_main);
      return mainImage ? mainImage.get_image_url : "";
    },
  },
};
</script>
