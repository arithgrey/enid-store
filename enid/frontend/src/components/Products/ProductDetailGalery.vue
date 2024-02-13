<template>
  <div v-if="product && product.category">
    <div class="lg:flex lg:items-start">
      <div class="lg:order-2 lg:ml-5">
        <div class="max-w-xl overflow-hidden rounded-lg">

          <img
            v-if="!selectedImage"
            class="h-full w-full max-w-full object-cover"
            :src="getMainImage(product)"
            alt=""
          />
          
          <img
            v-if="selectedImage"
            class="h-full w-full max-w-full object-cover"
            :src="selectedImage"
            alt=""
          />
        </div>
      </div>

      <div class="mt-2 w-full lg:order-1 lg:w-32 lg:flex-shrink-0">
        <div class="flex flex-row items-start lg:flex-col">          
          <button v-for="item in product.images" :key="item.name"
            type="button"
            class="flex-0 aspect-square mb-3 h-20 overflow-hidden rounded-lg border-2 border-gray-900 text-center"
          >
            <img
              @click="selectImage(item.get_image_url)"
              class="h-full w-full object-cover"
              :src="item.get_image_url"
              :alt="item.name"
            />
          </button>          
        </div>
      </div>
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
      selectedImage: null,
    };
  },
  methods: {
    getMainImage(item) {
      const mainImage = item.images.find((img) => img.is_main);
      return mainImage ? mainImage.get_image_url : "";
    },
    selectImage(imageUrl) {
      this.selectedImage = imageUrl;
    },
  },
  watch: {    
    product: {
      handler(newVal, oldVal) {        
        this.selectedImage = null;
      },
      deep: true,
    },
  },
};

</script>

