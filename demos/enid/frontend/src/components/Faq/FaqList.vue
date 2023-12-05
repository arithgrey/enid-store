<template>
  <div
    class="block p-6 bg-white border-b mt-5 border-gray-200 shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700"
    v-for="faq in faqList"
    :key="faq.id"
  >
    <h1
      class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
    >
      <router-link :to="{ params: { id: faq.id } }">
        {{ faq.ask }}
      </router-link>
    </h1>
    <p class="font-normal text-gray-700 dark:text-gray-400">
      {{ faq.answer }}
    </p>

    <div v-if="faq.we_mean" class="mt-4">
      <p
        class="mb-2 text-1xl font-bold tracking-tight text-gray-900 dark:text-white"
      >
        Lo que en verdad te queremos decir:
      </p>
      <p class="font-normal text-gray-700 dark:text-gray-400">
        {{ faq.we_mean }}
      </p>
    </div>
    <img
      v-if="faq.url_img && isImageValid(faq.url_img)"
      :src="faq.url_img"
      alt=""
      class="mt-3 w-full"
    />
  </div>
</template>

<script>

export default {
  data() {
    return {
      faqList: [],
    };
  },
  mounted() {
    this.fetchFaqList();
  },
  methods: {
    async fetchFaqList() {
      try {
        const response = await this.$axios.get("faq");
        this.faqList = response.data;
      } catch (error) {
        console.error("Error fetching FAQ list:", error);
      }
    },

    isImageValid(url) {
      if (!url) {
        return false; // Si no hay URL, no es válida
      }

      return new Promise((resolve) => {
        const img = new Image();
        img.onload = () => resolve(true);
        img.onerror = () => resolve(false);
        img.src = url;
      });
    },
  },
};
</script>
