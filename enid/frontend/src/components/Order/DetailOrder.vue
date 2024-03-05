<template>
  <div>
    <div class="border-b p-4 border-cyan-700 flex flex-col" v-if="order">
      <h5 class="block mb-2 text-xl font-bold text-blue-gray-900">
        {{ order.id }}
      </h5>

      <p class="text-sm text-right">{{ order.status }}</p>
      <p class="block text-sm text-right">
        {{ timePassed(order.created_at) }}
      </p>

      <div class="flex">
        <ul role="list" class="-my-6 divide-y divide-gray-200 flex-3">
          <div
            v-for="item_order in order.items"
            :key="item_order.id" 
            class="flex py-6"
          >
            <ProductItem :item_order="item_order" />
          </div>
        </ul>
        
        <div class="flex-1 border-l ml-4 p-5">
          <div class="mt-4 lg:row-span-3 lg:mt-0">
            <p class="text-3xl tracking-tight text-gray-900">
              Total {{ totalPriceQuantity }}
            </p>
            <h1 class="font-semibold text-gray-900 mt-5">
              Dirección de envío
            </h1>
            <AddressDetail :order="order" />
          </div>
          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { timePassed } from "@/helpers/time.js";
import ProductItem from "@/components/Products/ProductItemOrder.vue";
import AddressDetail from "@/components/Address/AddressDetail.vue";

export default {
  components: {
    ProductItem,
    AddressDetail
  },
  props: {
    order: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {};
  },
  methods: {
    timePassed,
  },
  computed: {
    totalPriceQuantity() {
      const total = this.items_order.reduce((acc, item_order) => {
        let total_quantity = item_order.price * item_order.quantity;
        return acc + total_quantity;
      }, 0);

      return this.formattedPrice(total);
    },
    formattedCreatedAt() {
      moment.locale("es");
      return moment(this.order.created_at).format("LLLL");
    },
  },
};
</script>
