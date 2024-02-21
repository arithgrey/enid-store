<template>
  <div>
    <header class="relative bg-white">
      <BannerAcion />
      <nav aria-label="Top" class="mx-auto w-full px-4 sm:px-6 lg:px-8">
        <div class="border-b border-gray-200">
          <div class="flex h-16 items-center">
            
            <!-- Logo -->
            <div class="ml-4 flex lg:ml-0">
              <router-link to="/">
                <div class="md:border-b p-0 md:px-2 border-black">
                  <span class="font-bold"> Enid </span>
                  service
                </div>
              </router-link>
            </div>

            <div class="ml-auto flex items-center navegacion">
              <!-- Search -->
              <div class="flex lg:ml-6">
                <div class="flex lg:ml-6">
                  <a
                    @click="openSearchProducts"
                    class="p-2 cursor-pointer text-gray-400 hover:text-gray-500"
                  >
                    <span class="sr-only">Search</span>
                    <MagnifyingGlassIcon class="h-6 w-6" aria-hidden="true" />
                  </a>
                </div>
              </div>

              <!-- Cart -->

              <div class="ml-4 flow-root lg:ml-6">
                <a
                  class="group -m-2 flex items-center p-2"
                  @click="openShoppingCart"
                >
                  <ShoppingBagIcon
                    :class="[
                      totalItemsCart > 0
                        ? 'font-bold text-gray-950 border-b border-black group-hover:text-blue-700'
                        : 'text-gray-400 group-hover:text-gray-500',
                      'h-6 w-6 flex-shrink-0  cursor-pointer',
                    ]"
                    aria-hidden="true"
                  />

                  <span
                    class="ml-2 text-sm font-medium text-gray-700 group-hover:text-gray-800"
                    >{{ totalItemsCart }}
                  </span>
                  <span class="sr-only">items in cart, view bag</span>
                </a>
              </div>
             

           
              <MenuImageuser/>

            </div>
          </div>
        </div>
      </nav>
    </header>
  </div>
</template>

<script setup>
import { ref } from "vue";
import {
  Bars3Icon,
  MagnifyingGlassIcon,
  ShoppingBagIcon,
  XMarkIcon,
} from "@heroicons/vue/24/outline";
const open = ref(false);
</script>

<script>
import CategoryList from "@/components/Category/CategoryList.vue";
import BannerAcion from "@/components/Banner/BannerAction.vue";
import MenuImageuser from "@/components/Banner/MenuImageUser.vue";

export default {
  components: {
    CategoryList,
    BannerAcion,
    MenuImageuser
  },
  data() {
    return {
      showMenu: true,      
    };
  },
  model: {
    event: "open_cart",
  },
  methods: {    
    openSearchProducts() {
      this.$emit("open_search_products");
    },
    openShoppingCart() {
      this.$emit("open_shopping_cart");
    },    
   
  },
  computed: {
    totalItemsCart() {
      return this.$store.getters.totalItemsInCart;
    },
 
  },
  watch: {
    $route(newVal, oldVal) {
      this.showMenu = true;
      if (newVal.path.includes("checkout")) {
        this.showMenu = false;
      }
    },
  },
};
</script>