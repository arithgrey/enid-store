<template>
  <div>
    <div class="border-b p-4 border-cyan-700" v-if="lead">
      <h5 class="block mb-2 text-xl font-bold text-blue-gray-900">
        {{ lead.name }}
      </h5>
      <p class="text-sm">{{ lead.email }}</p>
      <p class="text-sm">{{ lead.phone_number }}</p>
      <p class="text-sm text-right">{{ lead.status }}</p>
      <p class="block text-sm text-right">
        {{ timePassed(lead.created_at) }}
      </p>
    </div>
    <div v-if="lead && lead.products">
      <div class="font-semibold mt-5">
        Articulos que desea!
      </div>
      <div v-for="id_product in lead.products" :key="id_product">                
        <ProductItemId :id="id_product" :key="id_product" />
      </div>
    </div>
  </div>
</template>
<script>
import { timePassed } from "@/helpers/time.js";
import ProductItemId from "@/components/Products/ProductItemId.vue";

export default {
  props: {
    lead: {
      type: Object,
      required: true,
    },
  },
  components: {
    ProductItemId,
  },
  data() {
    return {};
  },
  methods: {
    timePassed,
  },
  watch: {
    'lead.products': function(newProducts, oldProducts) {
    }
  }
};
</script>
