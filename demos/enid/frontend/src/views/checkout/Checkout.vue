<template>
  <div>
    <div class="mt-10">
      <StepsShop :show_buy="true" />
    </div>
    <div
      v-if="showAddToCart"
      class="grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 px-4 py-24 sm:px-6 sm:py-32 lg:max-w-7xl lg:grid-cols-2 lg:px-8"
    >
      <div>
        <h2 class="text-2xl font-bold tracking-tight text-gray-900 sm:tc mb-5">
          Resumen de pedido
        </h2>
        <div class="mb-10 p-3 bg-gray-50">
          <div class="flex justify-between text-base font-medium text-gray-900">
            <p class="text-2xl">Total</p>
            <p class="text-2xl border-b border-black">
              {{ totalPriceQuantity }}
            </p>
          </div>

          <p class="mt-0.5 text-sm text-gray-900">({{ totalItemsCart }} Productos)</p>

          <p class="mt-0.5 text-sm text-gray-900">Envío gratis</p>
        </div>
        <CartList />

        <div class="mt-20 p-3">
          <h2
            class="text-2xl font-bold tracking-tight text-gray-900 sm:tc mb-2"
          >
            Llegada ?<span class="border p-1">?</span>
          </h2>
          <div class="bg-gray-50 p-2">
            <p class="text-sm">
              Llegan <span class="font-bold">HOY en CDMX</span> y área
              metropolitana
            </p>
            <p class="text-sm">
              En los estados, recibe tu pedido de
              <span class="font-bold">2 a 4 días hábiles</span>
            </p>
          </div>
        </div>
      </div>
      <div>
        <h2 class="text-2xl font-bold tracking-tight text-gray-900 sm:tc mb-5">
          Información de envío
        </h2>
        <p class="mt-4 text-sm text-gray-950 bg-gray-50">
          Solo usaremos estos datos para ayudarnos a entregar tu pedido
        </p>
        <FormCheckout />
      </div>
    </div>
  </div>
</template>
<script>
import CartList from "@/components/Cart/CartList.vue";
import FormCheckout from "@/components/Cart/FormCheckout.vue";
import StepsShop from "@/components/Trusth/StepsShop.vue";

export default {
  components: {
    CartList,
    StepsShop,
    FormCheckout,
  },
  data() {
    return {};
  },
  methods: {
    formattedPrice(price) {
      return price.toLocaleString("es-MX", {
        style: "currency",
        currency: "MXN",
        minimumFractionDigits: 2,
      });
    },
  },
  computed: {
    displayedCartProducts() {
      return this.$store.getters.getProductsFromCart;
    },
    totalPriceQuantity() {
      const total = this.displayedCartProducts.reduce((acc, product) => {
        let total_quantity = product.price * product.quantity;
        return acc + total_quantity;
      }, 0);

      return this.formattedPrice(total);
    },
    totalItemsCart() {
      return this.$store.getters.totalItemsInCart;
    },    
    showAddToCart() {
      return this.$store.getters.totalItemsInCart > 0;
    },

  },
};
</script>
