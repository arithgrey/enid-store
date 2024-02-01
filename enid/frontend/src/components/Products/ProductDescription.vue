<template>
  <div>
    <div class="border-b border-gray-300">
      <nav class="flex gap-4">
        <a
          href="#"
          title=""
          class="border-b-2 border-gray-900 py-4 text-sm font-medium text-gray-900 hover:border-gray-400 hover:text-gray-800"
        >
          Description
        </a>

        <a
          href="#"
          title=""
          class="inline-flex items-center border-b-2 border-transparent py-4 text-sm font-medium text-gray-600"
        >
          Reseñas
          <span
            class="ml-2 block rounded-full bg-gray-500 px-2 py-px text-xs font-bold text-gray-100"
          >
            1,209
          </span>
        </a>
      </nav>
    </div>

    <div class="mt-8 flow-root sm:mt-12">
      <h1 class="text-3xl font-bold mb-5">Entregado a tu puerta</h1>
      <ProductVarianList :product="product" />
    </div>
  </div>
</template>
<script>
import ProductVarianList from "@/components/Variants/ProductVarianList.vue";
export default {
  components: {
    ProductVarianList,
  },
  props: {
    product: {
      type: Object,
      required: true,
    },
  },
};
</script>

