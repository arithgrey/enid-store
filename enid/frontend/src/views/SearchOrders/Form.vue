<template>
  <div class="flex h-screen">
    <div class="m-auto  xs:w-full md:w-1/3 p-5">
      <div id="busqueda">
        <h2 class="font-bold text-gray-900 text-3xl sm:tracking-tight">
          Rastrea tu pedido
        </h2>

        <div class="mb-3 mt-5">
          <div class="relative mb-4 flex w-full flex-wrap items-stretch">
            <input
              placeholder="Número de orden"
              class="text-black placeholder-gray-600 w-full px-4 py-2.5 mt-2 text-base transition duration-500 ease-in-out transform border-transparent rounded-lg bg-gray-200 focus:border-blueGray-500 focus:bg-white dark:focus:bg-gray-800 focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2 ring-gray-400"
            />
          </div>
          <button
            type="button"
            class="relative w-full flex justify-center items-center px-5 py-2.5 font-medium tracking-wide text-white bg-black rounded-md hover:bg-gray-900 focus:outline-none transition duration-300 transform active:scale-95 ease-in-out"
          >
            <span class="pl-2 mx-1">Rastrea tu pedido</span>
          </button>
        </div>
      </div>
      <div class="text-right pt-3">
        <label class="block ml-2 text-sm">
          El tiempo de entrega en CDMX de 1 hora a 4 horas a partir de que nos
          envías tu pedido, envíos a otros estados de 1 a 2 días
        </label>
      </div>
      
    </div>
  </div>
</template>

<script>
export default {  
  mounted() {    
    window.scrollTo({ top: 0, behavior: "smooth" });
  },
  
};
</script>