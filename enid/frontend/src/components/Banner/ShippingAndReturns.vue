<template>
  <div>
    <TransitionRoot as="template" :show="open">
      <Dialog as="div" class="relative z-40 lg:hidden" @close="open = false">
        <TransitionChild
          as="template"
          enter="transition-opacity ease-linear duration-300"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="transition-opacity ease-linear duration-300"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="fixed inset-0 bg-black bg-opacity-25" />
        </TransitionChild>

        <div class="fixed inset-0 z-40 flex">
          <TransitionChild
            as="template"
            enter="transition ease-in-out duration-300 transform"
            enter-from="-translate-x-full"
            enter-to="translate-x-0"
            leave="transition ease-in-out duration-300 transform"
            leave-from="translate-x-0"
            leave-to="-translate-x-full"
          >
            <DialogPanel
              class="relative flex w-full max-w-xs flex-col overflow-y-auto bg-white pb-12 shadow-xl"
            >
              <div class="flex px-4 pb-2 pt-5">
                <button
                  type="button"
                  class="relative -m-2 inline-flex items-center justify-center rounded-md p-2 text-gray-400"
                  @click="open = false"
                >
                  <span class="absolute -inset-0.5" />
                  <span class="sr-only">Close menu</span>
                  <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                </button>
              </div>

              <!-- Links -->
              <TabGroup as="div" class="mt-2">
                <div class="border-b border-gray-200">
                  <TabList class="-mb-px flex space-x-8 px-4">
                    <Tab
                      as="template"
                      v-for="category in navigation.categories"
                      :key="category.name"
                      v-slot="{ selected }"
                    >
                      <button
                        :class="[
                          selected
                            ? 'border-indigo-600 text-indigo-600'
                            : 'border-transparent text-gray-900',
                          'flex-1 whitespace-nowrap border-b-2 px-1 py-4 text-base font-medium',
                        ]"
                      >
                        {{ category.name }}
                      </button>
                    </Tab>
                  </TabList>
                </div>
                <TabPanels as="template">
                  <TabPanel
                    v-for="category in navigation.categories"
                    :key="category.name"
                    class="space-y-10 px-4 pb-8 pt-10"
                  >                                          
                    <Currents/>                    
                    <div>
                      <p
                        :id="`sports--heading`"
                        class="font-medium text-gray-900"
                      >
                        Deporte en casa!
                      </p>
                      <CategoryList />
                    </div>
                    <div
                      v-for="section in category.sections"
                      :key="section.name"
                    >
                      <p
                        :id="`${category.id}-${section.id}-heading-mobile`"
                        class="font-medium text-gray-900"
                      >
                        {{ section.name }}
                      </p>
                      <ul
                        role="list"
                        :aria-labelledby="`${category.id}-${section.id}-heading-mobile`"
                        class="mt-6 flex flex-col space-y-6"
                      >
                        <li
                          v-for="item in section.items"
                          :key="item.name"
                          class="flow-root"
                        >
                          <a
                            :href="item.href"
                            class="-m-2 block p-2 text-gray-500"
                            >{{ item.name }}</a
                          >
                        </li>
                      </ul>
                    </div>
                  </TabPanel>
                </TabPanels>
              </TabGroup>

              <div class="space-y-6 border-t border-gray-200 px-4 py-6">            
                <router-link v-for="page in navigation.pages" :key="page.name" :to="generateRoute(page)"
                  class="flex items-center text-sm font-medium text-gray-950 hover:text-gray-800">
                  {{ page.name }}
                </router-link>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </Dialog>
    </TransitionRoot>

    <header class="relative bg-white">
      <BannerAcion />
      <nav aria-label="Top" class="mx-auto w-full px-4 sm:px-6 lg:px-8">
        <div class="border-b border-gray-200">
          <div class="flex h-16 items-center">
            <button
              type="button"
              class="relative rounded-md bg-white p-2 text-gray-400 lg:hidden"
              @click="open = true"
            >
              <span class="absolute -inset-0.5" />
              <span class="sr-only">Open menu</span>
              <Bars3Icon class="h-6 w-6" aria-hidden="true" />
            </button>

            <!-- Logo -->
            <div class="ml-4 flex lg:ml-0">
              <router-link to="/">
                <div class="md:border-b p-0 md:px-2 border-black">
                  <span class="font-bold"> Enid </span>
                  service
                </div>
              </router-link>
            </div>

            <!-- Flyout menus -->
            <PopoverGroup
              class="hidden lg:ml-8 lg:block lg:self-stretch navegacion"
              v-if="showMenu"
            >
              <div class="flex h-full space-x-8">
                <Popover
                  v-for="category in navigation.categories"
                  :key="category.name"
                  class="flex"
                  v-slot="{ open }"
                >
                  <div class="relative flex">
                    <PopoverButton
                      :class="[
                        open
                          ? 'border-indigo-600 text-indigo-600'
                          : 'border-transparent text-gray-700 hover:text-gray-950',
                        'relative z-10 -mb-px flex items-center border-b-2 pt-px text-sm font-medium transition-colors duration-200 text-gray-950 ease-out',
                      ]"
                      >{{ category.name }}</PopoverButton
                    >
                  </div>

                  <transition
                    enter-active-class="transition ease-out duration-200"
                    enter-from-class="opacity-0"
                    enter-to-class="opacity-100"
                    leave-active-class="transition ease-in duration-150"
                    leave-from-class="opacity-100"
                    leave-to-class="opacity-0"
                  >
                    <PopoverPanel
                      class="absolute inset-x-0 top-full text-sm text-gray-500"
                    >
                      <!-- Presentational element used to render the bottom shadow, if we put the shadow on the actual panel it pokes out the top, so we use this shorter element to hide the top of the shadow -->
                      <div
                        class="absolute inset-0 top-1/2 bg-white shadow"
                        aria-hidden="true"
                      />

                      <div class="relative bg-stone-100">
                        <div class="mx-auto max-w-7xl px-8">
                          <div class="grid grid-cols-2 gap-x-8 gap-y-10 py-16">
                            <div class="col-start-2 gap-x-8">
                              <Currents/>                             
                            </div>
                            <div
                              class="row-start-1 grid grid-cols-3 gap-x-8 gap-y-10 text-sm"
                            >
                              <div>
                                <p
                                  :id="`sports--heading`"
                                  class="font-medium text-gray-900"
                                >
                                  Deporte en casa!
                                </p>
                                <CategoryList />
                              </div>

                              <div
                                v-for="section in category.sections"
                                :key="section.name"
                              >
                                <p
                                  :id="`${section.name}-heading`"
                                  class="font-medium text-gray-900"
                                >
                                  {{ section.name }}
                                </p>
                                <ul
                                  role="list"
                                  :aria-labelledby="`${section.name}-heading`"
                                  class="mt-6 space-y-6 sm:mt-4 sm:space-y-4"
                                >
                                  <li
                                    v-for="item in section.items"
                                    :key="item.name"
                                    class="flex"
                                  >
                                    <a
                                      :href="item.href"
                                      class="hover:text-gray-800"
                                      >{{ item.name }}</a
                                    >
                                  </li>
                                </ul>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </PopoverPanel>
                  </transition>
                </Popover>              
               <router-link  v-for="page in navigation.pages"   :key="page.name" :to="generateRoute(page)"
                class="flex items-center text-sm font-medium text-gray-950 hover:text-gray-800">
                {{ page.name }}
              </router-link>
              </div>
            </PopoverGroup>

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
              <!-- Login -->
              <div class="ml-4 flow-root lg:ml-6" v-if="!isAuthenticated">
                <a
                  class="group -m-2 flex items-center cursor-pointer p-2"
                  @click="openSeccionLogin"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="w-6 h-6"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z"
                    />
                  </svg>
                </a>
              </div>

              <div class="ml-4 flow-root lg:ml-6" v-if="isAuthenticated">
                <a
                  class="group -m-2 flex items-center cursor-pointer p-2"
                  @click="logout"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="w-6 h-6"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M8.25 9V5.25A2.25 2.25 0 0 1 10.5 3h6a2.25 2.25 0 0 1 2.25 2.25v13.5A2.25 2.25 0 0 1 16.5 21h-6a2.25 2.25 0 0 1-2.25-2.25V15m-3 0-3-3m0 0 3-3m-3 3H15"
                    />
                  </svg>
                </a>
              </div>
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
  Dialog,
  DialogPanel,
  Popover,
  PopoverButton,
  PopoverGroup,
  PopoverPanel,
  Tab,
  TabGroup,
  TabList,
  TabPanel,
  TabPanels,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import {
  Bars3Icon,
  MagnifyingGlassIcon,
  ShoppingBagIcon,
  XMarkIcon,
} from "@heroicons/vue/24/outline";

import BannerAcion from "@/components/Banner/BannerAction.vue";
import Currents from "@/components/Banner/Currents.vue";

const navigation = {
  categories: [
    {
      id: "lo_mas_buscado",
      name: "LO MÁS BUSCADO",      
      sections: [
        {
          id: "ayuda",
          name: "Ayuda!",
          items: [            
            { name: "Tiempos de entrega", href: "/#tiempos-entrega" },
            { name: "Atención al cliente", href: "/#atencion-al-cliente" },            
          ],
        },
      ],
    },
  ],
  pages: [
    { name: "REFERENCIAS", href: "referencias",  authenticated: false},
    { name: "RASTREO", href: "rastreo",  authenticated: true },
    { name: "CAMBIOS", href: "cambios-y-devoluciones", authenticated: true, id:1  },
  ],
};


const open = ref(false);
</script>

<script>
import CategoryList from "@/components/Category/CategoryList.vue";

export default {
  components: {
    CategoryList,
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
    generateRoute(page) {
    if (page.id) {
      return {
        name: page.href,
        params: {
          id: page.id
        }
      };
    } else {
      return {
        name: page.href
      };
    }
    },
    openSearchProducts() {
      this.$emit("open_search_products");
    },
    openShoppingCart() {
      this.$emit("open_shopping_cart");
    },
    openSeccionLogin() {
      this.$emit("open_seccion_login");
    },
    logout() {
      
      const refresh_token  = localStorage.getItem('refresh_token');
      
      this.$axios.post(`/logout/`,{refresh_token:refresh_token})
        .then(response => {
      
          this.$store.commit("clearToken");
        })
        .catch(error => {
      
          console.error("Error al realizar la solicitud de logout:", error);
        });
      
    },
  },
  computed: {
    totalItemsCart() {
      return this.$store.getters.totalItemsInCart;
    },

    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
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