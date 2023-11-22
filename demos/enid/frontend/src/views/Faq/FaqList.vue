<!-- FaqList.vue -->
<template>
<figure class="bg-slate-100 rounded-xl dark:bg-slate-800">
  <img class="w-24 h-24" src="/sarah-dayan.jpg" alt="" width="384" height="512">
  <div class="pt-6 space-y-4">
    <blockquote>
      <p class="text-lg">
        “Tailwind CSS is the only framework that I've seen scale
        on large teams. It’s easy to customize, adapts to any design,
        and the build size is tiny.”
      </p>
    </blockquote>
    <figcaption>
      <div>
        Sarah Dayan
      </div>
      <div>
        Staff Engineer, Algolia
      </div>
    </figcaption>
  </div>
</figure>
  <div>
    <h2>Preguntas Frecuentes</h2>
    <ul>
      <li v-for="faq in faqList" :key="faq.id">
        <router-link :to="{  params: { id: faq.id } }">
          {{ faq.ask }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

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
        const response = await axios.get('http://127.0.0.1:8000/faq/');
        this.faqList = response.data;
      } catch (error) {
        console.error('Error fetching FAQ list:', error);
      }
    },
  },
};
</script>
