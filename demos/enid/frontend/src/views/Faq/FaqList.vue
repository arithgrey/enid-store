<template>
  <div class="bg-white -xl sm:mx-auto sm:max-w-lg sm:px-10">
    <div>
      <h2
        class="font-bold text-gray-900 sm:text-3xl sm:tracking-tight text-center"
      >
        FAQ QUE NADIE TE DIÓ 🫡😎
      </h2>
      <h3 class="text-gray-950 text-center">(NO PARA FRÁGILES)</h3>
    </div>
    <div class="pt-3 mt-5 border-t text-base leading-7 mx-auto p-5 sm:p-0 lg:p-0">
      <p class="text-gray-800">
        Si eres sensible y las quieres, haz tu pedido, NO leas esto
      </p>
      <p>
        <a href="/" class="text-sky-500 hover:text-sky-600 font-semibold"
          >Actuar &rarr;</a
        >
      </p>
    </div>
  </div>
  <div class="md:w-1/2 mx-auto xs:w-full">
    <FaqList />
  </div>
  <div class="w-1/2 mx-auto mt-10">
    <h2 class="font-bold text-gray-900 sm:text-2xl sm:tracking-tight text-center ">
      ¿INCLUIMOS TU FAQ?
    </h2>
    <h2 class="font-bold text-gray-900 sm:text-2xl sm:tracking-tight text-center mt-5">
      #FFFENIDS
    </h2>
  </div>
</template>

<script>
import FaqList from "@/components/Faq/FaqList.vue";

export default {
  components: {
    FaqList,
  },
};
</script>

<style>
</style>