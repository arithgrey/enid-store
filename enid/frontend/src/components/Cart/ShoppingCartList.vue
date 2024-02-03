<template>
  <div>
    <TransitionRoot as="template" :show="open">
      <Dialog as="div" class="relative z-50" @close="open = false">
        <TransitionChild
          as="template"
          enter="ease-in-out duration-500"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="ease-in-out duration-500"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div
            class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
          />
        </TransitionChild>

        <div class="fixed inset-0 overflow-hidden">
          <div class="absolute inset-0 overflow-hidden">
            <div
              class="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10"
            >
              <TransitionChild
                as="template"
                enter="transform transition ease-in-out duration-500 sm:duration-700"
                enter-from="translate-x-full"
                enter-to="translate-x-0"
                leave="transform transition ease-in-out duration-500 sm:duration-700"
                leave-from="translate-x-0"
                leave-to="translate-x-full"
              >
                <DialogPanel class="pointer-events-auto w-screen max-w-md">
                  <div
                    class="flex h-full flex-col overflow-y-scroll bg-white shadow-xl"
                  >
                    <div class="flex-1 overflow-y-auto px-4 py-6 sm:px-6">
                      <div class="flex items-start justify-between">
                        <DialogTitle class="text-lg font-medium text-gray-900"
                          >Tu carro de compra</DialogTitle
                        >
                        <div class="ml-3 flex h-7 items-center">
                          <button
                            type="button"
                            class="relative -m-2 p-2 text-gray-400 hover:text-gray-500"
                            @click="open = false"
                          >
                            <span class="absolute -inset-0.5" />
                            <span class="sr-only">Close panel</span>
                            <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                          </button>
                        </div>
                      </div>

                      <div class="mt-8">
                        <div class="flow-root">
                          <StepsShop/>
                          <CartList/>                          
                        </div>
                      </div>
                    </div>

                    <div class="border-t border-gray-200 px-4 py-6 sm:px-6">
                      <div
                        class="flex justify-between text-base font-medium text-gray-900"
                      >
                        <p>Total</p>
                        <p>{{ totalPriceQuantity }}</p>
                      </div>
                      <p class="mt-0.5 text-sm text-gray-500">Envío gratis</p>
                      <div class="mt-6">

                        <router-link                         
                        v-if="showReviewAndPay"
                        @click="open = false"
                        class="flex items-center justify-center 
                        rounded-md border border-transparent bg-slate-900 px-6 py-3 text-base font-medium text-white shadow-sm 
                        hover:bg-slate-950"
                        to="/checkout">Revisar y Pagar
                        </router-link>
                        
                        <div
                        v-if="!showReviewAndPay"                        
                        class="flex items-center justify-center 
                        rounded-md border border-transparent bg-slate-400 px-6 py-3 text-base font-medium text-white shadow-sm 
                        hover:bg-slate-400"
                        >Revisar y Pagar
                        </div>                      
                      </div>
                      <div
                        class="mt-6 flex justify-center text-center text-sm text-gray-500"
                      >
                        <p>
                          o
                          <button
                            type="button"
                            class="font-medium text-blue-600 hover:text-blue-500"
                            @click="open = false"
                          >
                            Sigue Comprando
                            <span aria-hidden="true"> &rarr;</span>
                          </button>
                        </p>
                      </div>
                    </div>
                  </div>
                </DialogPanel>
              </TransitionChild>
            </div>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  </div>
</template>

<script>
import {
  Bars3Icon,
  MagnifyingGlassIcon,
  ShoppingBagIcon,
  XMarkIcon,
} from "@heroicons/vue/24/outline";

import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import CartList from '@/components/Cart/CartList.vue';
import StepsShop from '@/components/Trusth/StepsShop.vue';

export default {
  components: {
    Dialog,
    DialogPanel,
    DialogTitle,
    TransitionChild,
    TransitionRoot,
    Bars3Icon,
    MagnifyingGlassIcon,
    ShoppingBagIcon,
    XMarkIcon,
    CartList,
    StepsShop,
  },
  data() {
    return {
      open: false,
    };
  },
  methods: {
    openCart() {      
      this.open = true;
    },
    closeCart() {
      this.open = false;
    },
    formattedPrice(price) {
      return price.toLocaleString("es-MX", {
        style: "currency",
        currency: "MXN",
        minimumFractionDigits: 2,
      });
    },
  },
  computed:{
    showReviewAndPay() {      
      return (this.$store.getters.totalItemsInCart) > 0;
    },    
    totalPriceQuantity() {
      const total = this.$store.getters.getProductsFromCart.reduce((acc, product) => {
        let total_quantity = product.price * product.quantity;
        return acc + total_quantity;
      }, 0);

      return this.formattedPrice(total);
    },
  }
};
</script>