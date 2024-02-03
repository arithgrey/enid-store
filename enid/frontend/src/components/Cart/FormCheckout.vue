<template>
  <div>
    <form class="mt-8" @submit.prevent="submitForm">
      <div>
        <h5 class="text-2xl font-bold tracking-tight text-gray-900 sm:tc mb-10">
          Contacto
        </h5>

        <div>
          <div class="relative z-0 w-full mb-5 mt-5 group">
            <input
              v-model="form.email"
              name="floating_email"
              @input="v$?.form.email.$touch()"
              id="floating_email"
              class="peer input-cart"
              placeholder="Correo electrónico*"
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
              v-model="form.phone_number"
              @input="formatPhoneNumber"
              type="tel"
              id="floating_name_phone_number"
              class="peer input-cart"
              placeholder="Teléfono*"
              required
            />

            <span
              class="text-red-500 text-sm"
              v-if="this.errors && this.errors.phone_number"
              >{{ formatError(this.errors.phone_number) }}</span
            >
            <span
              class="text-red-500 text-sm"
              v-if="v$?.form.phone_number.$error"
            >
              {{ v$?.form.phone_number.$errors[0].$message }}
            </span>
          </div>
        </div>
      </div>

      <div v-if="isContactInfo" ref="shippingAddressSection">
        <h5 class="text-2xl font-bold tracking-tight text-gray-900 sm:tc mb-10">
          Dirección de envío
        </h5>

        <div class="relative z-0 w-full mb-5 mt-5 group">
          <input
            v-model="form.postal_code"
            type="text"
            name="name"
            id="floating_postal_code"
            class="peer input-cart"
            @input="formatPostalCode"
            required
            placeholder="Código postal*"
          />
          <span
            class="text-red-500 text-sm"
            v-if="this.errors && this.errors.postal_code"
            >{{ formatError(this.errors.postal_code) }}</span
          >
          <span class="text-red-500 text-sm" v-if="v$?.form.postal_code.$error">
            {{ v$?.form.postal_code.$errors[0].$message }}
          </span>
        </div>

        <div class="relative z-0 w-full mb-5 mt-5 group">
          <input
            v-model="form.street"
            type="text"
            name="street"
            id="floating_street"
            class="peer input-cart"
            placeholder="Calle*"
            required
            @input="v$?.form.street.$touch()"
          />
          <span
            class="text-red-500 text-sm"
            v-if="this.errors && this.errors.street"
            >{{ formatError(this.errors.street) }}</span
          >
          <span class="text-red-500 text-sm" v-if="v$?.form.street.$error">
            {{ v$?.form.street.$errors[0].$message }}
          </span>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div class="">
            <div class="relative z-0 w-full mb-5 mt-5 group">
              <input
                v-model="form.number"
                type="text"
                name="number"
                id="floating_number"
                class="peer input-cart"
                placeholder="Número exterior*"
                @input="formatNumber"
                required
              />

              <span
                class="text-red-500 text-sm"
                v-if="this.errors && this.errors.number"
                >{{ formatError(this.errors.number) }}</span
              >
              <span class="text-red-500 text-sm" v-if="v$?.form.number.$error">
                {{ v$?.form.number.$errors[0].$message }}
              </span>
            </div>
          </div>
          <div>
            <div class="relative z-0 w-full mb-5 mt-5 group">
              <input
                v-model="form.interior_number"
                type="interior_number"
                name="interior_number"
                id="floating_interior_number"
                class="peer input-cart"
                placeholder="Número interior*"
                @input="formatInteriorNumber"
              />

              <span
                class="text-red-500 text-sm"
                v-if="this.errors.interior_number"
                >{{ formatError(this.errors.interior_number) }}</span
              >

              <span
                class="text-red-500 text-sm"
                v-if="v$?.form.interior_number.$error"
              >
                {{ v$?.form.interior_number.$errors[0].$message }}
              </span>
            </div>
          </div>
        </div>

        <div class="relative z-0 w-full mb-5 mt-5 group">
          <input
            @input="v$?.form.colony.$touch()"
            v-model="form.colony"
            type="text"
            name="colony"
            id="floating_colony"
            class="peer input-cart"
            required
            placeholder="Colonia*"
          />

          <span
            class="text-red-500 text-sm"
            v-if="this.errors && this.errors.colony"
          >
            {{ formatError(this.errors.colony) }}
          </span>
          <span class="text-red-500 text-sm" v-if="v$?.form.colony.$error">
            {{ v$?.form.colony.$errors[0].$message }}
          </span>
        </div>

        <div class="relative z-0 w-full mb-5 mt-5 group">
          <input
            @input="v$?.form.delegation_or_municipality.$touch()"
            v-model="form.delegation_or_municipality"
            name="delegation_or_municipality"
            id="floating_delegation_or_municipality"
            class="peer input-cart"
            required
            placeholder="Delegación o Municipio*"
          />
          <span
            class="text-red-500 text-sm"
            v-if="this.errors && this.errors.delegation_or_municipality"
            >{{ formatError(this.errors.delegation_or_municipality) }}</span
          >
          <span
            class="text-red-500 text-sm"
            v-if="v$?.form.delegation_or_municipality.$error"
          >
            {{ v$?.form.delegation_or_municipality.$errors[0].$message }}
          </span>
        </div>
        <div class="relative z-0 w-full mb-5 mt-5 group">
          <input
            v-model="form.city"
            type="text"
            name="city"
            id="floating_city"
            class="peer input-cart"
            required
            placeholder="Ciudad *"
          />

          <span class="text-red-500 text-sm" v-if="v$?.form.city.$error">
            {{ v$?.form.city.$errors[0].$message }}
          </span>
        </div>
        <div class="relative z-0 w-full mb-5 mt-5 group">
          <input
            v-model="form.additional_details"
            name="additional_details"
            id="floating_additional_details"
            class="peer input-cart"
            placeholder="¿Alguna referencia?"
          />
        </div>

        <h5 class="text-1xl font-bold tracking-tight text-gray-900 sm:tc">
          Estado
        </h5>
        <select
          v-model="form.state"
          class="block py-2.5 px-4 w-full text-gray-900 bg-transparent border-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
        >
          <option class="p-0" value="" disabled selected>
            Selecciona un estado
          </option>
          <option
            v-for="state in states"
            :key="state.id"
            :value="state.id"
            class="p-0"
          >
            {{ state.name }}
          </option>
        </select>
        <span
          class="text-red-500 text-sm"
          v-if="this.errors && this.errors.state"
          >{{ formatError(this.errors.state) }}</span
        >

        <h5
          class="text-2xl font-bold tracking-tight text-gray-900 sm:tc mb-1 mt-10"
        >
          Pago
        </h5>
        <div class="text-gray-800 text-sm mb-5">
          Todas las transacciones son seguras y están cifradas.
        </div>

        <div id="card-element" class="input-cart placeholder-gray-900"></div>
        <div v-if="this.stripe_message_error" class="text-red-500 mt-3 font-bold">
          {{ this.stripe_message_error }} Intenta de nuevo!
        </div>
        <div
          class="text-red-500 text-sm mt-3 font-bold"
          v-if="this.errors && this.errors.stripe_error"
          >{{ this.errors.stripe_error }} Intenta de nuevo!</div
        >

        <button
          type="submit"
          class="text-white mt-5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium text-sm w-full px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          Confirmar
        </button>
      </div>
    </form>
  </div>
</template>


<script>
import { useVuelidate } from "@vuelidate/core";
import { loadStripe } from "@stripe/stripe-js";
import { rules } from "@/rules/checkout/formCheckout.js";
import * as utilities from "@/rules/checkout/utilities.js";


export default {
  data() {
    return {
      states: [],
      stripe: null,
      card: null,
      stripe_message_error: "",
      form: {
        email: "",
        name: "",
        postal_code: "",
        street: "",
        number: "",
        interior_number: "",
        colony: "",
        delegation_or_municipality: "",
        city: "",
        state: "",
        additional_details: "",
        phone_number: "",
        products: [],
        stripe_token: "",
      },
      errors: {
        email: "",
        name: "",
        postal_code: "",
        street: "",
        number: "",
        interior_number: "",
        colony: "",
        delegation_or_municipality: "",
        city: "",
        additional_details: "",
        phone_number: "",
        stripe_error: "",
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
    this.fetchStates().then(() => {
      this.form.state = 7;
    });
  },
  watch: {},
  computed: {
    isContactInfo() {
      let status =
        !this.v$?.form.email.$error &&
        !this.v$?.form.name.$error &&
        !this.v$?.form.phone_number.$error &&
        this.form.email.length > 0 &&
        this.form.name.length > 0 &&
        this.form.phone_number.length > 0;
      if (status) {
        this.$nextTick(() => {
          this.initializeStripe();
          this.scrollToShippingAddress();
        });
      }
      return status;
    },
  },
  methods: {
    ...utilities,
    async initializeStripe() {
      try {
        this.stripe = await loadStripe(import.meta.env.VITE_APP_STRIPE);
        const elements = this.stripe.elements();

        const style = {
          base: {
            color: "#32325d",
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: "antialiased",
            fontSize: "20px",
            "::placeholder": {
              color: "#253d74",
            },
          },
          invalid: {
            color: "#fa755a",
            iconColor: "#fa755a",
          },
        };

        this.card = elements.create("card", { style });
        this.card.mount("#card-element");
      } catch (error) {
        console.error("Error during Stripe initialization:", error);
      }
    },
    scrollToShippingAddress() {
      const section = this.$refs.shippingAddressSection;
      if (section) {
        section.scrollIntoView({ behavior: "smooth" });
      }
    },
    
    async submitForm() {
      const result = await this.v$.$validate();
      if (!result) {
        return;
      }
      this.cleanErrors();

      try {
        const { token, error } = await this.stripe.createToken(this.card);
        if (error) {
          this.stripe_message_error = error.message;
          return;
        }

        this.stripe_message_error = "";
        this.form.stripe_token = token.id;
        await this.processPayment();
      } catch (error) {
        console.log(error);
      }
    },
    async processPayment() {
      try {
        this.form.products = this.$store.getters.getProductsFromCart;
        const response = await this.$axios.post("orden/compra/", this.form);
        this.nextToSaveOrder(response);
      } catch (error) {
        console.error("Error during payment processing:", error);
        if (error.response && error.response.data) {
          this.errors = error.response.data;
        }
      }
    },
    async fetchStates() {
      try {
        const response = await this.$axios.get("estado");
        this.states = response.data;
      } catch (error) {
        console.error("Error fetching estados list:", error);
      }
    },
    
    async nextToSaveOrder(response) {
      if (response.status === 201) {
        this.cleanFields();

        const clearCartPromise = new Promise((resolve) => {
          this.$store.commit("clearCart");
          resolve();
        });

        await clearCartPromise;
        let order_id = response.data.id;
        this.$router.push({ name: "order-detail", params: { id: order_id } });
      } else {
        this.stripe_message_error = response.data.stripe_error;
      }
    },
  },
};
</script>
