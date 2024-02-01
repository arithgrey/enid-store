<template>
  <nav aria-label="Breadcrumb">
    <ol
      role="list"
      class="flex max-w-2xl items-center space-x-2 mb-3 w-full"
    >
    
      <li>
        <div class="flex items-center">
          <a
            class="mr-2 text-sm font-medium text-gray-900"
            v-if="product && product.category"
          >
            {{ product.category.name }}</a
          >
          <svg
            width="16"
            height="20"
            viewBox="0 0 16 20"
            fill="currentColor"
            aria-hidden="true"
            class="h-5 w-4 text-gray-300"
          >
            <path d="M5.697 4.34L8.98 16.532h1.327L7.025 4.341H5.697z" />
          </svg>
        </div>
      </li>
      <li class="text-sm">
        <a
          aria-current="page"
          class="font-medium text-gray-500 hover:text-gray-600"
          >{{ product.name }}</a
        >
      </li>
    </ol>
  </nav>
</template>
<script>
export default {
  props: {
    product: {
      type: Object,
      required: true,
    },
  },
};
</script>
