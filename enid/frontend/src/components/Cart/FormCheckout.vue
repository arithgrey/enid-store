<template>
  <div>
    <form class="mt-8" @submit.prevent="submitForm" :disabled="loading">
      <div>
        <h5 class="text-2xl font-bold tracking-tight text-gray-900 sm:tc mb-10">
          ¿Dónde enviamos tu pedido?
        </h5>

        <div>
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

      <div
        :class="{ hidden: !isContact, block: isContact }"
        ref="shippingAddressSection"
      >
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
                inputmode="numeric"
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
                type="text"
                name="interior_number"
                id="floating_interior_number"
                class="peer input-cart"
                placeholder="Número interior*"
                @input="formatInteriorNumber"
                required
                inputmode="numeric"
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

        <selectState v-model="form.state"  @input="form.state = $event"/>

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
        <div
          v-if="this.stripe_message_error"
          class="text-red-500 mt-3 font-bold"
        >
          {{ this.stripe_message_error }} Intenta de nuevo!
        </div>
        <div
          class="text-red-500 text-sm mt-3 font-bold"
          v-if="this.errors && this.errors.stripe_error"
        >
          {{ this.errors.stripe_error }} Intenta de nuevo!
        </div>

        <button
          :disabled="loading"
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
import PaymentHelper from "@/helpers/PaymentHelper.js";
import { fields } from "@/components/Cart/js/checkoutFields.js";
import { rules } from "@/rules/checkout/checkoutValidator.js";
import selectState from "@/components/States/selectState.vue";
import * as utilities from "@/rules/utilities.js";
import * as utilitiesLeads from "@/components/Cart/js/leads.js";

export default {
  components: { selectState },
  data() {
    return {
      ...fields,
    };
  },
  setup: () => ({ v$: useVuelidate() }),
  validations() {
    return {
      form: rules,
    };
  },
  computed: {
    isContact() {
      
      let status = (
        !this.v$?.form.email.$error &&
        !this.v$?.form.name.$error &&
        !this.v$?.form.phone_number.$error &&
        this.form.email.length > 0 &&
        this.form.name.length > 0 &&
        this.form.phone_number.length > 0 
      );

      if(status && !this.sendUserLead){
          
        this.chargeUserLead()                   
      }
      return status;

    },
  },
  methods: {
    ...utilities,
    ...utilitiesLeads,

    async submitForm() {
      try {

        this.loading = true;
        const isValid = await this.validateForm();
        if (!isValid) return;

        const { response, stripe_error, error } = await this.processPayment();

        if (stripe_error) {
          this.stripe_message_error = stripe_error;
          return;
        }

        if (error) {
          this.handleSubmissionError(error);
          return;
        }

        if (response) {
          this.nextToSaveOrder(response);
        }
        
        
      } catch (error) {
        this.handleSubmissionError(error);
      } finally {
        this.loading = false;
      }
    },

    async validateForm() {
      const result = await this.v$.$validate();
      if (!result) {
        this.cleanErrors();
        return false;
      }
      return true;
    },

    async processPayment() {
      this.cleanErrors();
      this.form.products = this.$store.getters.getProductsFromCart;      
      return await this.paymentHelper.processPayment(this.form,  "orden/compra/");
    },

    async nextToSaveOrder(response) {

      if (response.status === 201) {
        this.cleanFields();
        await this.clearCart();
        this.$router.push({ name: "order-detail", params: { id: response.data.id } });
      } else {
        this.stripe_message_error = response.data.stripe_error;
      }
    },

    async clearCart() {
      await this.$store.commit("clearCart");
    },

    handleSubmissionError(error) {      
      console.error("Error during form submission:", error);
      if (error.response && error.response.data) {
        this.errors = error.response.data;
      }
      
    },
  },
  async created() {
    this.paymentHelper = new PaymentHelper(this);
    try {
      await this.paymentHelper.initializeStripe();
      await this.paymentHelper.createCardElement();
    } catch (error) {
      console.error("Error initializing PaymentHelper:", error);
    }
  },
};
</script>
