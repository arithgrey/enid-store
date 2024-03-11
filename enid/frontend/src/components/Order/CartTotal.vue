<template>
  <div>
    <div class="flex justify-between text-base font-medium">
      <p>Total</p>
      <p>
        {{ totalPriceQuantity }}
      </p>
    </div>
    <div>
      <p class="text-right mt-0.5 text-sm text-gray-900">
        ({{ totalItems }} Productos)
      </p>
      
    </div>
  </div>
</template>

<script>
import OrderHelper from "@/components/Products/js/OrderHelper.js";

export default {
  props: {
    productsFromCart: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      orderHelper: new OrderHelper(this.productsFromCart),
    };
  },
  computed: {
    totalPriceQuantity() {
      return this.orderHelper.totalPriceQuantity();
    },
    totalItems() {
      return this.orderHelper.totalItems();
    },
  },
};
</script>
