<template>
  <div class="grid pt-8 text-left border-t border-gray-200 md:gap-16 dark:border-gray-900 md:grid-cols-2">
    <div v-for="item in returnsList" :key="item.id">
      <div class="mb-10">
        <h3 class="flex items-center mb-4 text-lg font-medium text-gray-900 dark:text-white">
          <svg class="flex-shrink-0 mr-2 w-5 h-5 text-gray-500 dark:text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd"></path>
          </svg>
          {{ item.ask }}
        </h3>
        <p class="text-gray-500 dark:text-gray-400">
          {{ item.short_answer }}
          <div v-if="item.call_to_action" class="mt-5 text-black">
            <!-- Verifica si item.path_seccion existe y renderiza el enlace correspondiente -->
            <router-link v-if="item.path_seccion" :to="{ name: item.path_seccion, params:{} }" 
            class="px-8 py-2 border font-medium rounded-md text-white bg-gray-900 hover:bg-blue-700">
              {{ item.call_to_action }}
            </router-link>
            <!-- Si item.path_seccion no existe, renderiza el enlace para 'cambios-y-devoluciones' -->
            <router-link v-else :to="{ name: 'cambios-y-devoluciones', params: { id: item.id } }" 
            class="px-8 py-2 border font-medium rounded-md text-white bg-gray-900 hover:bg-blue-700">
              {{ item.call_to_action }}
            </router-link>
          </div>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      returnsList: [],
    };
  },
  mounted() {
    this.fetchReturnsList();    
  },
  methods: {
    async fetchReturnsList() {
      try {
        const response = await this.$axios.get("devoluciones");
        this.returnsList = response.data;
        console.log("________TOTAL______:", this.returnsList.length);
        

      } catch (error) {
        console.error("Error fetching devoluciones list:", error);
      }
    },
  },
};
</script>
