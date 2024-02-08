<template>
  <div class="text-center">
    <div class="text-2xl">
      <span class="font-bold"> Enid </span>
      service
    </div>

    <form v-if="searching" @submit.prevent="submitForm">
      <div class="mt-5">
        <p class="font-bold uppercase">Tus beneficios te esperan!</p>
      </div>
      <div>
        <p class="text-sm">Inicia sesión o regístrate</p>
      </div>

      <div class="mb-3 mt-5">
        <div class="relative z-0 w-full mb-5 mt-5 group">
          <input
            v-model="form.email"
            name="floating_email"
            @input="formatEmail"
            v-model.trim="form.email"
            id="floating_email"
            class="peer input-cart"
            placeholder="Correo electrónico*"
            type="email"
            inputmode="email"
          />

          <span
            class="text-red-500 text-sm"
            v-if="this.errors && this.errors.email"
          >
            {{ formatError(this.errors.email) }}
          </span>
          <span class="text-red-500 text-sm" v-if="v$?.form.email.$error">
            {{ v$?.form.email.$errors[0].$message }}
          </span>
        </div>

        <button
          type="submit"
          class="mx-auto relative flex justify-center items-center px-5 py-2.5 font-medium tracking-wide text-white bg-black rounded-md hover:bg-gray-900 focus:outline-none transition duration-300 transform active:scale-95 ease-in-out"
        >
          <span class="pl-2 mx-1">Continuar</span>
        </button>
      </div>
    </form>
    <LoginAccess v-if="user_exists && !searching" :email="form.email" />
    <LoginRegister v-if="!user_exists && !searching" 
    :email="form.email" @singup_success="handler_success_singup" />
  </div>
</template>

<script>
import { useVuelidate } from "@vuelidate/core";
import LoginAccess from "@/components/Login/LoginAccess.vue";
import LoginRegister from "@/components/Login/LoginRegister.vue";
import { emailCommonRule } from "@/rules/commonRules.js";



export default {
  components: {
    LoginAccess,
    LoginRegister,
  },
  data() {
    return {
      user_exists: false,
      searching: true,
      form: {
        email: "",
      },
      errors: {
        email: "",
      },
    };
  },
  setup: () => ({ v$: useVuelidate() }),
  validations() {
    return {
      form: {email:{...emailCommonRule}},
    };
  },
  methods: {
    handler_success_singup(email){
      this.form.email  = email;
      this.user_exists = true;
      this.searching = false;
    },
    async submitForm() {
      const result = await this.v$.$validate();
      if (!result) {
        return;
      }
      this.searching = false;

      try {
        const response = await this.$axios.get(
          `user/exists/${this.form.email}`
        );

        this.user_exists = response.data.exists;
      } catch (error) {
        console.error("Error during user existence check:", error);
        this.searching = true;
      }
    },
    formatError(error) {
      return error[0];
    },
    formatEmail() {
      this.v$?.form.email.$touch();
      this.form.email = this.form.email.toLowerCase();
    },

  },
};
</script>
  