<template>
  <ul role="list" class="-my-6 divide-y divide-gray-200 border-b">
    <li
      v-for="product in displayedCartProducts"
      :key="product.id"
      class="flex py-6"
    >
      <div
        class="h-24 w-24 flex-shrink-0 overflow-hidden rounded-md border border-gray-200"
      >
        <router-link
          :to="{
            name: 'product-detail',
            params: {
              categorySlug: product.category.slug,
              productSlug: product.slug,
            },
          }"
        >
          <img
            :src="getMainImage(product)"
            class="h-full w-full object-cover object-center"
          />
        </router-link>
      </div>

      <div class="ml-4 flex flex-1 flex-col">
        <div>
          <div class="flex justify-between text-base font-medium text-gray-900">
            <h3>
              <a :href="product.href">{{ product.name }}</a>
            </h3>
            <p class="ml-4">
              {{ this.formattedPrice(product.price) }}
            </p>
          </div>
        </div>
        <div class="flex flex-1 items-end justify-between text-sm">
          <p class="text-gray-500">Cant {{ product.quantity }}</p>
          <div class="flex">
            <button
              @click="removeFromCart(product)"
              type="button"
              class="font-medium text-indigo-600 hover:text-indigo-500"
            >
              Quitar
            </button>
          </div>
        </div>
      </div>
    </li>
  </ul>
</template>

<script>
export default {
  components: {},
  data() {
    return {};
  },
  methods: {
    getMainImage(product) {
      const mainImage = product.images.find((img) => img.is_main);
      return mainImage ? mainImage.get_image_url : "";
    },
    removeFromCart(product) {
      this.$store.commit("removeFromCart", product);
    },
    formattedPrice(price) {
      return price.toLocaleString("es-MX", {
        style: "currency",
        currency: "MXN",
        minimumFractionDigits: 2,
      });
    },
  },
  computed: {
    displayedCartProducts() {
      return this.$store.getters.getProductsFromCart;
    },
    totalPriceQuantity() {
      const total = this.displayedCartProducts.reduce((acc, product) => {
        let total_quantity = product.price * product.quantity;
        return acc + total_quantity;
      }, 0);

      return this.formattedPrice(total);
    },
  },
};
</script>
