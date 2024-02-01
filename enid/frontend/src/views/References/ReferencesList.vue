<template>
  <div>
    <div class="overflow-y-hidden bg-cyan-700">
      <div
        class="mx-auto container flex justify-center items-center py-2 sm:px-2"
      >
        <div class="flex flex-col lg:flex-row justify-center items-center">
          <div
            class="w-full lg:w-3/4 sm:w-80 flex flex-col justify-start items-start"
          >
            <div>
              <p
                class="text-3xl xl:text-4xl font-semibold leading-9 text-white"
              >                
                NUESTRA HISTORIA: CONTADA POR USTEDES
              </p>
            </div>
          </div>

       
        </div>
      </div>
    </div>
    <div
      ref="imageContainer"
      class="max-h-screen overflow-y-auto p-5"
      @scroll="handleScroll"
    >
      <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
        <div v-for="(image, index) in images" :key="index" class="grid gap-4">
          <div class="relative overflow-hidden" style="padding-top: 100%">
            <img
              class="absolute inset-0 w-full h-full object-cover"
              :src="image.get_image_url"
              :alt="image.name"
            />
          </div>
        </div>
      </div>

      <div v-if="loading" class="text-center py-4">
        <i class="animate-spin text-gray-500 fas fa-spinner fa-2x"></i>
        Cargando...
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      images: [],
      next: null,
      loading: false,
    };
  },
  mounted() {
    this.fetchImagesReferences();
  },
  methods: {
    async fetchImagesReferences() {
      try {
        const response = await this.$axios.get(
          "business/enid-service/imagenes-referencia/"
        );
        this.images = response.data.results;
        this.next = response.data.next;
      } catch (error) {
        console.error("Error references list:", error);
      }
    },
    async loadMoreImages() {
      try {
        const response = await this.$axios.get(this.next);
        this.images = [...this.images, ...response.data.results];
        this.next = response.data.next;
      } catch (error) {
        console.error("Error loading more images:", error);
      } finally {
        this.loading = false;
      }
    },
    handleScroll() {
      const container = this.$refs.imageContainer;
      const bottomOfContainer =
        container.scrollHeight - container.scrollTop === container.clientHeight;

      if (bottomOfContainer && this.next && !this.loading) {
        this.loading = true;
        this.loadMoreImages();
      }
    },
  },
};
</script>
