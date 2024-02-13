<template>
  <div>
    <div>
      <p        
        class="tracking-tight  text-gray-800 mb-2 font-bold"
      >
        {{ product.specific_name }}
      </p>
     
    </div>
    <div class="mt-2 mb-2">
      <p
        v-if="formattedTotalWeight < 0.5"
        class="tracking-tight text-base font-medium leading-4 text-gray-800"
      >
        Peso total {{ product.formatted_weight }}
      </p>
      
      <p
        v-if="formattedTotalWeight > 0"
        class="tracking-tight text-base font-medium leading-4 text-gray-800"
      >
        Peso total de los discos {{ formattedTotalWeight.toFixed(2) }} Kg
      </p>
       <p class="tracking-tight text-xs leading-3 text-gray-800 mt-3">
        Codigo: {{ product.code }}
      </p>
    </div>
    <div v-if="products_variant.length > 0">
      <ul>
        <li
          v-for="(variant, index) in products_variant"
          :key="index"
          class="tracking-tight text-sm leading-3 text-gray-800 mt-1"
        >
          <span class="font-semibold mr-3"> {{ variant.pieces }} </span>
          <span> {{ variant.variant.name }}</span>
        </li>
      </ul>
    </div>
    <div class="mt-6" >
      <p class="leading-4 text-gray-900">
        <span class="font-bold text-1xl">
        {{ product.formatted_price }}
        </span>
        
        <span class=" text-slate-600 line-through">
          ${{ normalizedPrice }}
        </span>
      </p>
      <p
        class="tracking-tight mt-1 text-sm font-medium leading-4 text-gray-900"
      >
        <span class=""> Envío gratis </span>
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
  computed: {
    formattedTotalWeight() {
      return this.calculate_total_disc_weight();
    },
    normalizedPrice() {
      return (this.product.price * 1.2).toFixed(2);
    },
      
  },
  async mounted() {
      
    await this.fetch_products_variant();
    
  },
  watch: {    
    'product.id': {
      handler: 'fetch_products_variant',
      immediate: true, 
    },
  },
  methods: {
    async fetch_products_variant() {
      try {
        if (!this.product.id) {
          console.error("Error: Product ID is undefined");
          return;
        }      
        const response = await this.$axios.get(
          `/producto-variante/producto/${this.product.id}/variantes/`
        );
        this.products_variant = response.data;

      } catch (error) {
        console.error("Error fetching FAQ list:", error);
      }
    },
    calculate_total_disc_weight() {
      let total_weight = 0;

      if (this.product.count_discs) {
        total_weight = this.products_variant.reduce((total, item) => {
          const { disc, weight } = item.variant;
          return total + (disc ? item.pieces * weight : 0);
        }, 0);
      }

      return total_weight;
    },    
  },
};
</script>
