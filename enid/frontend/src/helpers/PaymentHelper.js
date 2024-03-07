import { loadStripe } from "@stripe/stripe-js";

export default class PaymentHelper {
  constructor(component) {
    this.component = component;
    this.stripe = null;
    this.card = null;
    this.stripeInitialized = false;    
  }

  async initializeStripe() {
    if (this.stripeInitialized) {
      return;
    }
    try {
      this.stripe = await loadStripe(import.meta.env.VITE_APP_STRIPE);
      this.stripeInitialized = true;
    } catch (error) {
      console.error("Error initializing Stripe:", error);
      throw new Error("Stripe initialization failed: " + error.message);
    }
  }

  async createCardElement() {
    try {
      if (!this.stripeInitialized) {
        await this.initializeStripe();
      }
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
      await this.card.mount("#card-element");
      return this.card;
    } catch (error) {
      console.error("Error creating card element:", error);
      throw new Error("Error creating card element: " + error.message);
    }
  }
  
  async processPayment(form, apiUrl) {
    try {
      if (!this.stripeInitialized) {
        await this.initializeStripe();
      }
      if (!this.card) {
        await this.createCardElement();
      }

      const { token, error } = await this.stripe.createToken(this.card);

      if (error) {
        return { stripe_error: error.message };
      }

      form.stripe_token = token.id;
      const response = await this.component.$axios.post(apiUrl, form);
      return { response };

    } catch (error) {

      
      return { error: error }

    }
  }
}
