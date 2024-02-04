<template>
  <div class="mt-10">
  <div class="bg-white p-5 w-full md:w-1/2 mx-auto mt-10 mb-10">
    <h2 class="font-bold text-gray-900 text-3xl sm:tracking-tight">
      Cambios y devoluciones
    </h2>

    <div
      class="p-2 mt-5 border-gray-900 shadow dark:bg-gray-900 dark:border-gray-900"
    >
      <h5 class="mb-2 text-gray-900 dark:text-white">
        Si no te satisface tu compra, ofrecemos garantía de devolución durante
        los primeros 30 días y cambios hasta por 12 meses.
      </h5>
    </div>

    <section class="bg-white dark:bg-gray-900 mt-10">
      <div class="">
        <h2 class="mb-8 text-2xl tracking font-extrabold dark:text-white text-blue-700">
          Preguntas relacionadas
        </h2>
        <returns-list />
      </div>
    </section>
  </div>
  </div>
</template>

<script>
import ReturnsList from "@/components/Returns/ReturnsList.vue";
export default {
  components: {
    ReturnsList,
  },
  mounted(){
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
};
</script>

