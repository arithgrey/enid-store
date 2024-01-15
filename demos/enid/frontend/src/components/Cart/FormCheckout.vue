<template>
  <div>
    <form class="mt-8" @submit.prevent="submitForm">
      <div>
        <h5 class="text-1xl font-bold tracking-tight text-gray-900 sm:tc mb-5">
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
            />
            <label for="floating_email" class="label-input-cart">
              Correo electrónico*
            </label>
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
              required
            />
            <label for="floating_name" class="label-input-cart">
              Nombre*
            </label>
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
              required
            />
            <label for="floating_name_phone_number" class="label-input-cart">
              Teléfono*
            </label>
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
        <h5
          class="text-1xl font-bold tracking-tight text-gray-900 sm:tc mb-5 mt-5"
        >
          Dirección de envío
        </h5>

        <div class="relative z-0 w-full mb-5 mt-5 group">
          <input
            v-model="form.postal_code"
            type="text"
            name="name"
            id="floating_postal_code"
            class="peer input-cart"
            placeholder=""
            @input="formatPostalCode"
            required
          />
          <label for="floating_postal_code" class="label-input-cart">
            Código postal*
          </label>
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
            placeholder=""
            required
            @input="v$?.form.street.$touch()"
          />
          <label for="floating_street" class="label-input-cart"> Calle* </label>
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
                placeholder=""
                @input="formatNumber"
                required
              />
              <label for="floating_number" class="label-input-cart">
                Número exterior*
              </label>
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
                placeholder=""
                @input="formatInteriorNumber"
              />
              <label for="floating_interior_number" class="label-input-cart">
                Número interior*
              </label>
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
          />
          <label for="floating_colony" class="label-input-cart">
            Colonia*
          </label>
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
          />
          <label
            for="floating_delegation_or_municipality"
            class="label-input-cart"
          >
            Delegación o Municipio*
          </label>
          <span
            class="text-red-500 text-sm"
            v-if="
              this.errors &&
              this.errors.delegation_or_municipality
            "
            >{{
              formatError(this.errors.delegation_or_municipality)
            }}</span
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
          />
          <label for="floating_city" class="label-input-cart"> Ciudad * </label>
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
          />
          <label for="floating_additional_details" class="label-input-cart">
            ¿Alguna referencia?
          </label>
        </div>

        <h5 class="text-1xl font-bold tracking-tight text-gray-900 sm:tc">
          Estado
        </h5>
        <select
          v-model="form.state"
          class="block py-2.5 px-4 w-full text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
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
          class="text-1xl font-bold tracking-tight text-gray-900 sm:tc mb-5 mt-5"
        >
          Datos del pago
        </h5>
        <button
          type="submit"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium text-sm w-full px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          Confirmar
        </button>
      </div>
    </form>
  </div>
</template>


<script>
import {
  minLength,
  maxLength,
  alphaNum,
  numeric,
  between,
} from "@vuelidate/validators";
import { helpers } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import { required, email } from "@vuelidate/validators";

const rules = {
 
 name: {
    minLength: helpers.withMessage(
      "El nombre debe tener al menos 10 caracteres.",
      minLength(10)
    ),
    maxLength: helpers.withMessage(
      "Hey ese nombre es muy largo",
      maxLength(150)
    ),
    required: helpers.withMessage("El nombre es obligatorio.", required),
  },
  
  email: {
    required: helpers.withMessage("Hey ingresa un email!", required),
    email: helpers.withMessage("Hey ingresa un email válido!", email),
  },

  phone_number: {
    required: helpers.withMessage("Hey ingresa tu número tefónico!", required),
    minLength: helpers.withMessage(
      "El teléfono debe tener al menos 10 números!",
      minLength(10)
    ),
    maxLength: helpers.withMessage(
      "El teléfono no puede tener más de 12 números!",
      maxLength(12)
    ),
    numeric: helpers.withMessage("Hey ingresa un teléfono correcto!", numeric),
  },
  
  postal_code: {
    required: helpers.withMessage("Hey ingresa tu código postal!", required),
    minLength: helpers.withMessage(
      "El código postal es muy corto!",
      minLength(4)
    ),
    maxLength: helpers.withMessage(
      "El código postal es muy largo!",
      maxLength(8)
    ),
    numeric: helpers.withMessage("Hey ingresa solo números!", numeric),
  },

  street: {
    required: helpers.withMessage("Ingresa el nombre de tu calle!", required),
    minLength: helpers.withMessage(
      "El nombre de tu calle es tan corto?",
      minLength(4)
    ),
    maxLength: helpers.withMessage(
      "El nombre de tu calle es tan largo?",
      maxLength(100)
    ),
  },

  number: {
    required: helpers.withMessage("Hey falta tu número de casa!", required),
    between: helpers.withMessage(
      "Hey ingresa solo números correctos!",
      between(1, 1000000)
    ),
  },

  interior_number: {
    integer: helpers.withMessage("Hey ingresa solo números!", required),
    numeric: helpers.withMessage("Hey ingresa solo números!", numeric),
    between: helpers.withMessage(
      "Hey ingresa solo números correctos !",
      between(1, 1000000)
    ),
  },

  colony: {
    required: helpers.withMessage("Indica cual es tu colonia!", required),
    minLength: helpers.withMessage(
      "Registra el nombre de tu colonia!",
      minLength(4)
    ),
    maxLength: helpers.withMessage(
      "Es tan largo el nombre de tu colonia?",
      maxLength(50)
    ),
  },

  delegation_or_municipality: {
    required: helpers.withMessage("Falta tu Delegación!", required),
    minLength: helpers.withMessage("Ingresa tu delegación!", minLength(4)),
    maxLength: helpers.withMessage(
      "Es tan largo el nombre de tu delegación?",
      maxLength(50)
    ),
  },

  city: {
    required: helpers.withMessage("Ingresa tu ciudad!", required),
    minLength: helpers.withMessage(
      "Ingresa el nombre de tu ciudad!",
      minLength(3)
    ),
    maxLength: helpers.withMessage(
      "Es tan largo el nombre de tu ciudad?",
      maxLength(50)
    ),
  },
};

export default {
  data() {
    return {
      states: [],
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
        this.scrollToShippingAddress();
      }
      return status;
    },
  },
  methods: {
    scrollToShippingAddress() {
      this.$nextTick(() => {
        /*
        const section = this.$refs.shippingAddressSection;        
        if (section) {
          section.scrollIntoView({ behavior: "smooth" });
        }
        */
      });
    },

    formatName() {
      this.v$?.form.name.$touch();
      this.form.name = this.cleanNonChars(this.form.name);
    },

    formatInteriorNumber() {
      this.form.interior_number = this.cleanNonNumericChars(
        this.form.interior_number
      );
    },

    formatNumber() {
      this.form.number = this.cleanNonNumericChars(this.form.number);
      this.v$?.form.number.$touch();
    },

    formatPostalCode() {
      this.v$?.form.postal_code.$touch();
      this.form.postal_code = this.cleanNonNumericChars(this.form.postal_code);
    },

    formatPhoneNumber() {
      this.v$?.form.phone_number.$touch();

      this.form.phone_number = this.cleanNonNumericChars(
        this.form.phone_number
      );

      if (this.form.phone_number.length > 12) {
        this.form.phone_number = this.form.phone_number.slice(0, 12);
      }
    },

    cleanNonNumericChars(str) {
      return str.replace(/[^0-9]/g, "");
    },

    cleanNonChars(str) {
      return str.replace(/[^a-zA-Z\s]/g, "");
    },

    async submitForm() {
      /*
      const result = await this.v$.$validate();

      if (!result) {
        return;
      }*/

      try {
        this.cleanErrors();
        this.form.products = this.$store.getters.getProductsFromCart;

        const response = await this.$axios.post("orden/compra/", this.form, {
          headers: {
            "Content-Type": "application/json",
          },
        });
      } catch (error) {
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
        //console.error("Error fetching estados list:", error);
      }
    },
    formatError(error) {
      return error[0];
    },
    cleanErrors() {
      for (let section in this.errors) {
        for (let field in this.errors[section]) {
          this.errors[section][field] = "";
        }
      }
    },
  },
};
</script>
