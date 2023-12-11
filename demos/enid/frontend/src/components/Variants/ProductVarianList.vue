<template>
  <div>
    <div>
      <p class="tracking-tight text-xs leading-3 text-gray-800">
        Codigo: {{ product.code }}
      </p>
    </div>
    <div class="mt-2 mb-2">
      <p class="tracking-tight text-base font-medium leading-4 text-gray-800">
        Peso total {{ product.formatted_weight }}
      </p>
    </div>
    <div v-if="products_variant.length > 0">  
      <ul>
        <li v-for="(variant, index) in products_variant" :key="index" class="tracking-tight text-sm leading-3 text-gray-800 mt-1">
          <span class="font-semibold mr-3"> {{ variant.pieces}} </span>
          <span> {{variant.variant.name}}</span>
          
        </li>
      </ul>
    </div>
    <div class="mt-6">
      <p class="tracking-tight text-base font-medium leading-4 text-gray-800">
        {{ product.formatted_price }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    product: {
      type: Object,
      required: true,
    },
  },  
  data() {
    return {
      products_variant: [],       
    };
  },
  mounted() {
    this.fetch_products_variant();
  },
  methods: {  
    async fetch_products_variant() {
      try {
        
        const response = await this.$axios.get(`/producto-variante/producto/${this.product.id}/variantes/`);
        this.products_variant = response.data;

      } catch (error) {
        console.error("Error fetching FAQ list:", error);
      }
    }
  }
};
</script>
