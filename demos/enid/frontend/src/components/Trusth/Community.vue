<template>
  <div>
    <div class="overflow-y-hidden bg-gray-900">
      <div class="container py-12 px-4 sm:px-6 2xl:px-0">
        <div>
          <p class="text-3xl xl:text-4xl font-semibold leading-9 text-white">
            CONSIGUE ESCULPIRTE EN TU HOGAR
          </p>
        </div>
      </div>
    </div>
    <div class="slider-container">
      <div
        class="slider"
        :style="{ transform: `translateX(${translateValue}px)` }"
      >
        <div v-for="(image, index) in images" :key="index" class="slide flex-shrink-0 w-1/8">
          <img :src="image" alt="Slide" class="w-full h-full object-cover" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      images: [
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWY4b3p5dTBxcnJtbnpjdXFpMmJ2Mm9qaWFyYjVyYmxrMjlkeGIwZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/I3HUZ8nuhetHypdZRB/giphy-downsized-large.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjAycjdlaGI3ZWd4emNoMG40NTkzMWkwc29nNXk1bnV5aGx5M2N2cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HVUt9iX4PKKlO/giphy.gif",
        "https://media.giphy.com/media/3HFcLK4IXKoviqvwve/giphy.gif",
        "https://media.giphy.com/media/TidtDukYTD0lO/giphy.gif",
        "https://media.giphy.com/media/dsskR2ah7Ozlu/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2pneXFrYmE4eGVsMTg0OWdqZHcza2c3eTR0MmR3aXZ2NHc1ejg3ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dB5IAEzRvi3W3R2t16/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjdvOWZhZHM4OGswbnV4dWhldmlyaGpmem0xYXQ5bjIwajgyM3pnZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GbWf0u65MHCIU/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHpkMm0zaDc4YjY4eXI5d3AxaXE0a2pzbmZzMGxkYzQ5bzRhb3prdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EgkNhBeY289z2/giphy.gif",
      ],
      currentIndex: 0,
      translateValue: 0,
    };
  },
  mounted() {
    this.startSlider();
  },
  methods: {
    startSlider() {
      setInterval(() => {
        this.nextSlide();
      }, 1000);
    },
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
      this.translateValue = -this.currentIndex * (100 / 8);
    },
  },
};
</script>

<style scoped>
.slider-container {
  overflow: hidden;
  width: 100%;
}

.slider {
  display: flex;
  transition: transform 0.5s ease;
}
</style>
