<template>
  <div class="container mx-auto px-4 flex flex-col items-center h-screen">
    <div class="mb-5">
      <SearchForm ref="searchForm" @list_leads="handlerLeads" />
    </div>
    <div class="border-t w-full mb-5 flex">
      <div class="search-leads w-1/4 mr-4 mt-5">
        <div
          v-for="item in leads"
          :key="item.id"
          @click="selectLead(item)"
          :class="{ 'border-cyan-700': selectedLead && selectedLead.id === item.id }"
          class="shadow-md bg w-full border cursor-pointer"
        >
          <div class="p-6">
            <h5
              class="block mb-2 text-xl font-semibold leading-snug tracking-normal text-blue-gray-900"
            >
              {{ item.name }}
            </h5>
            <p class="block text-sm">
              {{ item.phone_number }}              
            </p>
            <p class="block text-sm text-right">
              {{ item.status }}
            </p>
            <p class="block text-sm text-right">
              {{ timePassed(item.created_at) }}
            </p>
          </div>
        </div>
      </div>

      <div class="description-lead w-3/4 mt-5 border p-5">
        <DetailLead :lead="selectedLead"/>
      </div>
    </div>
  </div>
</template>

<script>
import SearchForm from "@/components/Leads/SearchForm.vue";
import DetailLead from  "@/components/Leads/DetailLead.vue";
import {timePassed}  from "@/helpers/time.js";


export default {
  components: {
    SearchForm,
    DetailLead
  },
  data() {
    return {
      leads: [],
      selectedLead: null,

    };
  },
  methods: {
    timePassed,
    handlerLeads(leads) {      
        
      this.leads = leads;
    },   
    selectLead(lead) {
      
      this.selectedLead = lead;
    },
    callSubmitForm() {
      
      this.$refs.searchForm.submitForm();
    },
  },
  mounted() {
    
    this.callSubmitForm();
  },
  
};
</script>
