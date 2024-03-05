<template>
  <div class="border-t" v-if="show">
    <div
      class="grid min-h-[140px] w-full place-items-center overflow-x-scroll rounded-lg p-6 lg:overflow-visible"
    >
      <h2
        class="block font-sans text-2xl antialiased font-semibold leading-tight tracking-normal text-inherit mt-10"
      >
        {{message}}
      </h2>
    </div>
    <p v-if="show_buy" class="text-center">
      <router-link
        type="button"
        class="font-medium text-blue-600 hover:text-blue-500"
        to="/"
      >
        Sigue Comprando
        <span aria-hidden="true"> &rarr;</span>
      </router-link>
    </p>
  </div>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      default: "Ups! aún no haz agregado productos a tu carrito de compras",
    },
    show_buy: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    show() {
      return this.$store.getters.totalItemsInCart < 1;
    },
  },
};
</script>

