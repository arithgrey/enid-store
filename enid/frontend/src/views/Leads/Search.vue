<template>
  <div class="container mx-auto px-4 flex flex-col items-center min-h-screen mb-10">
    <div class="mb-5">
      <SearchForm ref="searchForm" @list_leads="handlerLeads" />
    </div>
    <div class="border-t w-full mb-5 flex">
      <div class="search-leads w-1/4 mr-4 mt-5 overflow-y-auto max-h-90">
        <ItemListLead :leads="leads"  @selected_lead="handleSelectedLead"/>
      </div>

      <div class="description-lead w-3/4 mt-5 border p-5" ref="descriptionLead">
        <DetailLead :lead="selectedLead"/>
      </div>
    </div>
  </div>
</template>

<script>
import SearchForm from "@/components/Leads/SearchForm.vue";
import DetailLead from  "@/components/Leads/DetailLead.vue";
import ItemListLead from "@/components/Leads/ItemListLead.vue";
import {timePassed}  from "@/helpers/time.js";


export default {
  components: {
    SearchForm,
    DetailLead,
    ItemListLead
  },
  data() {
    return {
      leads: null,
      selectedLead: null,
    };
  },
  methods: {
    timePassed,
    handlerLeads(leads) {      
        
      this.leads = leads;
    },   
    handleSelectedLead(lead) {
      
      this.selectedLead = lead;
      this.$refs.descriptionLead.scrollIntoView({ behavior: 'smooth' });

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
