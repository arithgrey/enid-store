<template>
  <div>
    <form class="mt-8" @submit.prevent="submitForm">
      <div class="flex">
        <div>
          <input
            v-model="form.q"
            class="peer input-cart"
            placeholder="Buscar..."
            type="text"
            inputmode="text"
          />
        </div>

        <button
          type="submit"
          class="relative flex items-center px-3 mt-1 font-medium tracking-wide text-white bg-black hover:bg-gray-900 focus:outline-none transition duration-300 transform active:scale-95 ease-in-out"
        >
          <span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"
              />
            </svg>
          </span>
        </button>
      </div>
      <span class="text-red-500 text-sm" v-if="v$?.form.q.$error">
        {{ v$?.form.q.$errors[0].$message }}
      </span>
    </form>
    <div class="flex mt-3">
      <button
        aria-label="show menu"
        @click="toggleFilters()"
        class="mt-4 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-800 py-2.5 px-2 bg-gray-800 text-white hover:text-gray-400"
      >
        <svg
          v-if="showFilters"
          class="fill-stroke"
          width="10"
          height="6"
          viewBox="0 0 10 6"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M9 5L5 1L1 5"
            stroke="currentColor"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
        <svg
          v-else
          class="fill-stroke"
          width="10"
          height="6"
          viewBox="0 0 10 6"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M1 1L5 5L9 1"
            stroke="currentColor"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </button>

      <div v-if="showFilters" class="ml-5">
        <div class="mt-5 w-full">
          <p class="font-bold">Lo más buscado</p>
        </div>
      </div>
    </div>
     <div v-if="showFilters" class="mt-4">
        <div class="w-full">
          <CategoryList @close_filters="handlerFilterCategory"/>
        </div>
      </div>
  </div>
</template>

<script>
import { useVuelidate } from "@vuelidate/core";
import { minLength } from "@vuelidate/validators";
import { helpers } from "@vuelidate/validators";
import { required } from "@vuelidate/validators";
import CategoryList from "@/components/Category/CategoryList.vue";


export const rules = {
  q: {
    minLength: helpers.withMessage(
      "Ingresa el nombre de algun artículo.",
      minLength(1)
    ),
    required: helpers.withMessage(
      "Ingresa el nombre de algun artículo.",
      required
    ),
  },
};

export default {
  components: {
    CategoryList
  },
  data() {
    return {
      showFilters: false,
      form: {
        q: "",
      },
    };
  },
  setup: () => ({ v$: useVuelidate() }),
  validations() {
    return {
      form: rules,
    };
  },
  methods: {
    toggleFilters() {
      this.showFilters = !this.showFilters;
    },
    async submitForm() {
      const result = await this.v$.$validate();
      if (!result) {
        return;
      }

      this.$router.push({ name: "search-product", params: { q: this.form.q } });
      this.$emit("close_search_form");
    },
    handlerFilterCategory(){
      this.$emit("close_search_form");
    }
  },
};
</script>