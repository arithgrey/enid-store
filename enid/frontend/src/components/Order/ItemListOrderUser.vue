<template>
  <div>
    <div v-if="orders && orders.length === 0">
      <p>No se encontraron resultados.</p>
    </div>
    <div v-else>
      <div
        v-for="item in orders"
        :key="item.id"
        @click="selectOrder(item)"
        :class="{
          'border-cyan-700': selectOrder && selectOrder.id === item.id,
        }"
        class="shadow-md bg w-full border cursor-pointer"
      >
        <div class="p-6">
          <h5
            class="block mb-2 text-sm font-semibold leading-snug tracking-normal text-blue-gray-900 text-cyan-700"
          >
            Orden: #{{ item.id }}
          </h5>
          <CartTotal :productsFromCart="item" />

          <div class="flex mt-5 items-end justify-end">
            <p class="block text-sm">
              {{ item.status }}
            </p>
            <span class="mx-2 text-sm text-gray-700">|</span>
            <p class="block text-sm">
              {{ timePassed(item.created_at) }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { timePassed } from "@/helpers/time.js";
import CartTotal from "@/components/Order/CartTotal.vue";

export default {
  components: {
    CartTotal,
  },
  props: {
    orders: {
      type: Array,
      required: true,
    },
  },
  computed: {
    reactiveOrders() {
      return this.orders.slice();
    },
  },
  data() {
    return {
      selectedOrder: null,
    };
  },
  methods: {
    timePassed,
    selectOrder(order) {
      
      this.selectedOrder = order;
      this.$emit("selected_order", order);
    },
  },
};
</script>
