<template>
  <div>
    <div class="bg-white">
      <div class="pt-6">
        <div
          class="mx-auto max-w-2xl px-4 pb-16 pt-10 sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:grid-rows-[auto,auto,1fr] lg:gap-x-8 lg:px-8 lg:pb-24 lg:pt-16"
        >
          <div class="lg:col-span-2 lg:border-r lg:border-gray-200 lg:pr-8">
            <h1
              class="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl"
            >
              Orden #{{ order.id }}
            </h1>
            <p class="font-bold">status: {{ order.status }}</p>
            <p class="text-sm">Pedido realizado el {{ formattedCreatedAt }}</p>
          </div>

          <!-- Options -->
          <div class="mt-4 lg:row-span-3 lg:mt-0">
            <p class="text-3xl tracking-tight text-gray-900">
              Total {{ totalPriceQuantity }}
            </p>
            <h1 class="font-semibold text-gray-900 mt-5">
              Dirección de envío
            </h1>
            <AddressDetail :order="order" />
          </div>

          <div
            class="py-10 lg:col-span-2 lg:col-start-1 lg:border-r lg:border-gray-200 lg:pb-16 lg:pr-8 lg:pt-6"
          >
            <ul role="list" class="-my-6 divide-y divide-gray-200 border-b">
              <div
                v-for="item_order in items_order"
                :key="item_order.id"
                class="flex py-6"
              >
                <ProductItem :item_order="item_order" />
              </div>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProductItem from "@/components/Products/ProductItemOrder.vue";
import AddressDetail from "@/components/Address/AddressDetail.vue";
import moment from "moment";
import "moment/locale/es";

export default {
  components: {
    ProductItem,
    AddressDetail
  },
  props: {},
  data() {
    return {
      order: [],
      items_order: [],
      order_id: null,
      
    };
  },
  mounted() {
    window.scrollTo({ top: 0, behavior: "smooth" });
    this.fetchOrder();
  },
  methods: {
    async fetchOrder() {
      try {
        const response = await this.$axios.get(
          `compra/${this.$route.params.id}`
        );
        this.order = response.data;
        this.items_order = response.data.items;

      } catch (error) {
        console.error("Error Order list:", error);
      }
    },
    formattedPrice(price) {
      return price.toLocaleString("es-MX", {
        style: "currency",
        currency: "MXN",
        minimumFractionDigits: 2,
      });
    },
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
