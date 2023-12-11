<template>
  <body class="overflow-y-hidden">
    <div
      class="mx-auto container px-4 md:px-6 2xl:px-0 py-12 flex justify-center items-center"
    >
      <div class="flex flex-col jusitfy-start items-start">
        <div class="mt-3">
          <h1
            class="text-3xl lg:text-4xl tracking-tight font-semibold leading-8 lg:leading-9 text-gray-800"
          >
            Lo más pedido
          </h1>
        </div>
        <div class="mt-4">
          <p class="text-2xl tracking-tight leading-6 text-gray-600">
            03 items
          </p>
        </div>
        <ProductList />
      </div>
    </div>
  </body>
</template>
<script>
import ProductList from "@/components/Products/ProductList.vue";

export default {
  components: {
    ProductList,
  },
};
</script>
