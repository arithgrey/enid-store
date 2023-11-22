<!-- FaqList.vue -->
<template>
  <div>
    <h2>Preguntas Frecuentes</h2>
    <ul>
      <li v-for="faq in faqList" :key="faq.id">
        <router-link :to="{ name: 'FaqDetail', params: { id: faq.id } }">
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
