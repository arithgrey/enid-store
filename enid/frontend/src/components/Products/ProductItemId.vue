<template>
  <li v-if="product" class="flex py-6">
    <div
      class="h-24 w-24 flex-shrink-0 overflow-hidden rounded-md border border-gray-200"
    >
    <router-link
    
          :to="{
            name: 'product-detail',
            params: {
              categorySlug: product.category.slug,
              productSlug: product.slug,
            },
          }"
        >
        <img class="h-full w-full object-cover object-center" v-if="product.images" 
        :src="getMainImage(product)"/>
    </router-link>
    </div>

    <div class="ml-4 flex flex-1 flex-col">
      <div>
        <div class="flex justify-between text-base font-medium text-gray-900">
          <h3>
            <a v-if="product.name">{{ product.name }}</a>
          </h3>
          <p class="ml-4">
            {{ formattedPrice(product.price) }}
          </p>
        </div>
      </div>
      
    </div>
  </li>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      product: null,
    };
  },
  watch: {
    id: {
      immediate: true,
      handler(newVal, oldVal) {
        if (newVal !== oldVal) {
          this.fetchProduct();
        }
      },
    },
  },
  mounted() {
        
    this.fetchProduct();
  
  },
  methods: {
    async fetchProduct() {
    
      try {
        const response = await this.$axios.get(
          `productos/${this.id}`
        );
    
        this.product = response.data;

      } catch (error) {
        console.error("Error Order list:", error);
      }
    },
    getMainImage(product) {
      const mainImage = product.images.find((img) => img.is_main);
      return mainImage ? mainImage.get_image_url : "";
    },
    formattedPrice(price) {
      return price.toLocaleString("es-MX", {
        style: "currency",
        currency: "MXN",
        minimumFractionDigits: 2,
      });
    },
  },    
};
</script>
