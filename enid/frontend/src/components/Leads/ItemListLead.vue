<template>
  <div>
    <div v-if="leads.length === 0">
      <p>No se encontraron resultados.</p>
    </div>
    <div v-else>
      <div
        v-for="item in leads"
        :key="item.id"
        @click="selectLead(item)"
        :class="{
          'border-cyan-700': selectedLead && selectedLead.id === item.id,
        }"
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
  </div>
</template>

<script>
import { timePassed } from "@/helpers/time.js";
export default {
  props: {
    leads: {
      type: Array,
      required: true,
    },
  },
  computed: {
    reactiveLeads() {      
      return this.leads.slice();
    },
  },
  data() {
    return {
      selectedLead: null,
    };
  },
  methods: {
    timePassed,
    selectLead(lead) {
      this.selectedLead = lead;      
      this.$emit("selected_lead", lead);
    },
  },
};
</script>
