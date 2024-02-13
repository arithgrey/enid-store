<template>
  <div>
    <h1 class="sm: text-2xl font-bold text-gray-900 sm:text-3xl">
      {{ product.name }}
    </h1>
    <p class="mt-1 text-sm">{{product.specific_name}}</p>
    <div class="mt-6">
      <h3 class="sr-only">Reviews</h3>
      <div class="flex items-center">
        <div class="flex items-center">
          <StarIcon
            v-for="rating in [0, 1, 2, 3, 4]"
            :key="rating"
            :class="[
              reviews.average > rating ? 'text-gray-900' : 'text-gray-200',
              'h-5 w-5 flex-shrink-0',
            ]"
            aria-hidden="true"
          />
        </div>
        <p class="sr-only">{{ reviews.average }} out of 5 stars</p>
        <a
          :href="reviews.href"
          class="ml-3 text-sm font-medium text-blue-600 hover:text-blue-500"
          >{{ reviews.totalCount }} reseñas</a
        >
      </div>
    </div>


    <div
      class="mt-10 flex flex-col items-center justify-between space-y-4 border-t border-b py-4 sm:flex-row sm:space-y-0"
    >
      <div class="flex flex-col">
        <h1 class="text-3xl font-bold">{{ product.formatted_price }}</h1>
        <span class="text-slate-600 line-through">
          ${{ normalizedPrice }}
        </span>
      </div>

      <button
  type="button"
  @click="addToCart()"
  class="inline-flex items-center justify-center rounded-md border-2 border-transparent bg-gray-900 bg-none px-12 py-3 text-center text-base
   font-bold text-white transition-all duration-200 ease-in-out focus:shadow hover:bg-gray-800 xs:w-full lg:w-auto"
>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    class="shrink-0 mr-3 h-5 w-5"
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
    stroke-width="2"
  >
    <path
      stroke-linecap="round"
      stroke-linejoin="round"
      d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"
    />
  </svg>
  Añadir al carrito
</button>
    </div>
    
    <div>
      <SelectItems v-if="product.product_group > 0" :product_group="product.product_group" :currentProduct="product.id"/>
    </div>
  
    <ul class="mt-8 space-y-2">
      <li class="flex items-center text-left text-sm font-medium text-gray-600">
        <svg
          class="mr-2 block h-5 w-5 align-middle text-gray-500"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            class=""
          ></path>
        </svg>
        Envío gratis


      </li>

      <li class="flex items-center text-left text-sm font-medium text-gray-600">
        <svg
          class="mr-2 block h-5 w-5 align-middle text-gray-500"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"
            class=""
          ></path>
        </svg>
        
        Cancelar en cualquier momento

      </li>
    </ul>
  </div>
</template>
<script>
import { StarIcon } from "@heroicons/vue/20/solid";
import SelectItems from "@/components/ProductGroup/SelectItems.vue";
export default {
  components: { StarIcon, SelectItems },
  props: {
    product: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      reviews: { href: "#", average: 4, totalCount: 1209 },
    };
  },  
  computed: {
    
    normalizedPrice() {      
      return (this.product.price * 1.2).toFixed(2);
    },
  },
  methods: {
    addToCart() {
      
      this.$emit("open_shopping_cart_product");
      return this.$store.commit("addToCart", this.product);
      
    },    
  },
  
};
</script>