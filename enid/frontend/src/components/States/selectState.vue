<template>
  <div>
    <select
      v-model="selectedState"
      class="block py-2.5 px-4 w-full text-black bg-transparent border-2 border-gray-300 dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600"
      ref="stateSelect"
      @change="validateState"
    >
      <option class="p-0" value="" disabled>Selecciona un estado</option>
      <option
        v-for="stateItem in states"
        :key="stateItem.id"
        :value="stateItem.id"
        class="p-0 text-black"
      >
        {{ stateItem.name }}
      </option>
    </select>
    <span v-if="stateErrors.length" class="text-red-500">{{ stateErrors[0] }}</span>
  </div>
</template>

<script>
import { required } from "@vuelidate/validators";
import { helpers } from "@vuelidate/validators";

export default {
  props: {
    value: String,
  },
  data() {
    return {
      selectedState: "",
      states: [],
      stateErrors: [],
    };
  },
  mounted() {
    this.fetchStates();
  },
  methods: {
    async fetchStates() {
      try {
        const response = await this.$axios.get("estado");
        this.states = response.data;
        this.selectedState = this.value;
        const selectElement = this.$refs.stateSelect;
        if (selectElement) {
          selectElement.value = 7;
        }
        this.validateState();
      } catch (error) {
        console.error("Error fetching estados list:", error);
      }
    },
    validateState() {
      this.stateErrors = [];
      if (!this.selectedState) {
        this.stateErrors.push("Selecciona un estado");
      }
    },
  },
  watch: {
    selectedState() {
      this.validateState();
      this.$emit("input", this.selectedState);
    },
  },
};
</script>
