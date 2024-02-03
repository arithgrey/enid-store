<template>
  <div v-if="address">
    <p class="mt-3 text-sm">
      {{ address.street }} #{{ address.number }} int
      {{ address.interior_number }}, {{ address.colony }},
      {{ address.city }}, {{ address.delegation_or_municipality }}
      {{ address.country }}, C.p. {{ address.postal_code }}
    </p>

    <h1 class="font-semibold text-gray-900 mt-5 mb-3">Contacto</h1>
    <p class="text-sm">{{ formatPhoneNumber(address.phone_number) }}</p>
  </div>
</template>

<script>
export default {
  props: {
    order: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      address: [],
    };
  },
  watch: {
    "order.shipping_address": function (newVal, oldVal) {
      if (newVal && newVal > 0) {
        this.fetchAddress();
      }
    },
  },
  mounted() {
    if (
      this.order &&
      this.order.shipping_address &&
      this.order.shipping_address > 0
    ) {
      this.fetchAddress();
    }
  },
  methods: {
    async fetchAddress() {
      try {
        const response = await this.$axios.get(
          `direccion/${this.order.shipping_address}`
        );
        this.address = response.data;
      } catch (error) {
        console.error("Error Addresslist:", error);
      }
    },
    formatPhoneNumber(number) {
      
            return `(${String(number).slice(0, 3)}) ${String(number).slice(3, 6)}-${String(number).slice(6)}`;

    },
  },
};
</script>

