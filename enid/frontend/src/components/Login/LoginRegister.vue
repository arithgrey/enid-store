<template>
  <div>
    <div class="text-center mt-5">Crea tu cuenta fácil, como todo aquí 😎</div>
    <form @submit.prevent="submitForm" :disabled="isSubmitting">
      <div class="mb-3 mt-5">
        <div class="relative z-0 w-full mb-5 mt-5 group">
          <input
            v-model="form.email"
            name="floating_email"
            @input="formatEmail"
            id="floating_email"
            class="peer input-cart"
            placeholder="Correo electrónico*"
            type="email"
            inputmode="email"
            readonly
          />

          <span
            class="text-red-500 text-sm"
            v-if="this.errors && this.errors.email"
          >
            {{ this.errors.email }}
          </span>
          <span class="text-red-500 text-sm" v-if="v$?.form.email.$error">
            {{ v$?.form.email.$errors[0].$message }}
          </span>
        </div>
        <div class="relative z-0 w-full mb-5 mt-5 group">
          <input
            v-model="form.name"
            @input="formatName"
            type="text"
            name="name"
            id="floating_name"
            class="peer input-cart"
            placeholder="Nombre"
            required
            :readonly="isSubmitting"
          />

          <span
            class="text-red-500 text-sm"
            v-if="this.errors && this.errors.name"
            >{{ formatError(this.errors.name) }}</span
          >
          <span class="text-red-500 text-sm" v-if="v$?.form.name.$error">
            {{ v$?.form.name.$errors[0].$message }}
          </span>
        </div>

        <div class="relative z-0 w-full mb-5 mt-5 group">
          <input
            v-model="form.password"
            @input="formatPassword"
            name="password"
            id="password"
            class="peer input-cart"
            placeholder="password *"
            type="password"
            required
            :readonly="isSubmitting"
          />

          <span
            class="text-red-500 text-sm"
            v-if="this.errors && this.errors.password"
            >{{ formatError(this.errors.password) }}</span
          >
          <span class="text-red-500 text-sm" v-if="v$?.form.password.$error">
            {{ v$?.form.password.$errors[0].$message }}
          </span>
        </div>

        <div class="relative z-0 w-full mb-5 mt-5 group">
          <input
            v-model="form.password_confirm"
            @input="formatPasswordConfirm"
            name="password_confirm"
            id="password_confirm"
            class="peer input-cart"
            placeholder="De nuevo tu password *"
            type="password"
            required
            :readonly="isSubmitting"
          />

          <span
            class="text-red-500 text-sm"
            v-if="this.errors && this.errors.password_confirm"
            >{{ this.errors.password_confirm }}</span
          >
          <span
            class="text-red-500 text-sm"
            v-if="v$?.form.password_confirm.$error"
          >
            {{ v$?.form.password_confirm.$errors[0].$message }}
          </span>
        </div>

        <button
          :disabled="isSubmitting"
          type="submit"
          class="mx-auto relative flex justify-center items-center px-5 py-2.5 font-medium 
          tracking-wide text-white bg-black rounded-md hover:bg-gray-900 focus:outline-none
           transition duration-300 transform active:scale-95 ease-in-out">
          <span class="pl-2 mx-1">Registrar</span>
        </button>
        
      </div>
    </form>
  </div>
</template>

<script>
import { useVuelidate } from "@vuelidate/core";
import { rules } from "@/rules/Login/register.js";
import sha256 from 'sha256'; 
import {
  formatName,
  formatError,
  formatEmail,
  formatPassword,
  formatPasswordConfirm,
  cleanNonChars
} from "@/rules/utilities.js";

export default {
  props: {
    email: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      isSubmitting:false,
      user_exists: false,
      form: {
        email: "",
        name: "",
        password: "",
        password_confirm: "",
      },
      errors: {
        email: "",
        name: "",
        password: "",
        password_confirm: "",
      },
    };
  },
  setup: () => ({ v$: useVuelidate() }),
  validations() {
    return {
      form: rules,
    };
  },
  mounted() {
    this.form.email = this.email;
  },
  methods: {
    formatName,
    formatError,
    formatEmail,
    formatPassword,
    formatPasswordConfirm,
    cleanNonChars,
    async submitForm() {
      
      if (this.isSubmitting) return;
      const result = await this.v$.$validate();
      if (!result) {
        this.isSubmitting = false;
        return;
      }
      
      const hashedPassword =  await new Promise((resolve, reject)=>{
          const hash = sha256(this.form.password);
          resolve(hash)
      });
      
      
      this.singUp(hashedPassword)

    },
    async singUp(hashedPassword){
      
      this.isSubmitting  = true;                   
      try {
        
        const user  = {
          password:hashedPassword,
          name:this.form.name,
          email:this.form.email,
        }
      
        const response = await this.$axios.post(`/login/signup/`, user);
        this.singupHandler(response);
      

      } catch (error) {
        
        this.errors = error.response.data;
        this.isSubmitting  = false;
        console.error("Error on sinagup user:", error);
      }
    },
    singupHandler(response){
      
      this.isSubmitting  = false;  
      if(response.status === 201){
        this.$emit("singup_success", this.email)
      }        
    }
  },
};
</script>
  