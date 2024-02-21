<template>
  <div class="text-center">
    <div class="mt-5">
      <p class="font-bold uppercase">Tus beneficios te esperan!</p>
      <div>
        <p class="text-sm">Inicia sesión!</p>
      </div>
    </div>
    <form @submit.prevent="submitFormAccess" :disabled="isSubmitting">
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
          <span
            class="text-red-500 text-sm"
            v-if="this.errors && this.errors.error && !v$?.form.password.$error"
            >{{ this.errors.error }}</span
          >
          
        </div>

        <button
          :disabled="isSubmitting"
          type="submit"
          class="mx-auto relative flex justify-center items-center px-5 py-2.5 
          font-medium tracking-wide text-white bg-black rounded-md hover:bg-gray-900 
          focus:outline-none transition duration-300 transform active:scale-95 ease-in-out"
        >
          <span class="pl-2 mx-1">Acceder</span>          
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { useVuelidate } from "@vuelidate/core";
import { rules } from "@/rules/Login/access.js";
import { formatError, formatEmail, formatPassword } from "@/rules/utilities.js";
import sha256 from "sha256";

export default {
  props: {
    email: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      isSubmitting: false,
      form: {
        email: "",
        password: "",
      },
      errors: {
        email: "",
        password: "",
        error:"",
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
    formatError,
    formatEmail,
    formatPassword,
    async submitFormAccess() {
      if (this.isSubmitting) return;
      const result = await this.v$.$validate();
      if (!result) {
        this.isSubmitting = false;
        return;
      }

      const hashedPassword = await new Promise((resolve, reject) => {
        const hash = sha256(this.form.password);
        resolve(hash);
      });
      this.singIn(hashedPassword);
    },
    async singIn(hashedPassword) {
      this.isSubmitting = true;
      try {

        const user = { password: hashedPassword, email: this.form.email };
        const response = await this.$axios.post(`/login/sigin/`, user);
        this.singinHandler(response);

      } catch (error) { 
        
        this.errors = error.response.data;
        this.isSubmitting = false;
                
      }
    },
    singinHandler(response){
      
      if(response.status === 200){
        
        const token = response.data.token;
        const refresh_token = response.data.refresh_token;        
        const user = response.data.user;

        this.$store.commit('setUser', user); 
        this.$store.commit('setToken', token); 
        this.$store.commit('setRefreshToken', refresh_token); 
        this.$store.commit('setProfile', user.profile); 
        
         switch (profile) {
          case 'ecommerce':
            this.$router.push({name:"ecommerce-user"});
            break;
          case 'administrador':
            this.$router.push({name:"admin-user"});
            break;
         
          default:        
            this.$router.push({name:"product-list"});
            break;
        }

      }
    }
  },
};
</script>
  