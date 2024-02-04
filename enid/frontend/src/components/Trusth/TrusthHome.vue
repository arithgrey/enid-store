<template>
  <div class="border-t" id="tiempos-entrega">
    <div
      class="grid min-h-[140px] w-full place-items-center overflow-x-scroll rounded-lg p-6 lg:overflow-visible"
    >
      <h2
        class="block font-sans text-3xl antialiased font-semibold leading-tight tracking-normal text-inherit mt-10"
      >
        ¿Cuanto tiempo tarda en llegar un pedido?
      </h2>

      <h6
        class="block font-sans text-base antialiased  leading-relaxed tracking-normal text-inherit mb-10 mt-5"
      >
        <span class="font-bold">
          Hoy mismo 
        </span>
        en CDMX y 2-3 Días hábiles en los estados
      </h6>
    </div>
    <div class="">
      <div
        class="bg-gray-900 grid lg:grid-cols-4 md:grid-cols-2 grid-cols-1 lg:gap-8 md:gap-12 gap-14 lg:px-20 lg:py-12 py-10 md:px-12 px-4"
      >
        <div class="">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6 text-white"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M8.25 18.75a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h6m-9 0H3.375a1.125 1.125 0 01-1.125-1.125V14.25m17.25 4.5a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h1.125c.621 0 1.129-.504 1.09-1.124a17.902 17.902 0 00-3.213-9.193 2.056 2.056 0 00-1.58-.86H14.25M16.5 18.75h-2.25m0-11.177v-.958c0-.568-.422-1.048-.987-1.106a48.554 48.554 0 00-10.026 0 1.106 1.106 0 00-.987 1.106v7.635m12-6.677v6.677m0 4.5v-4.5m0 0h-12"
            />
          </svg>
          <h3
            class="text-xl leading-5 dark:text-white font-semibold text-white lg:mt-10 mt-8"
          >
            Entrega
          </h3>
          <p
            class="text-base leading-6 font-normal dark:text-gray-300 text-gray-100 mt-4 lg:w-full md:w-9/12 w-full"
          >
            Envíos 
            <span class="font-bold">
            gratis
            </span>
            a todo México
          </p>
        </div>

        <!-- customer Grid Card -->

        <div class="" id="atencion-al-cliente">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6 text-white"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M8.625 9.75a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 01.778-.332 48.294 48.294 0 005.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z"
            />
          </svg>

          <h3
            class="text-xl leading-5 dark:text-white font-semibold text-white lg:mt-10 mt-8"
          >
            Atención al cliente
          </h3>
          <p
            class="text-base leading-6 font-normal dark:text-gray-300 text-gray-100 mt-4 lg:w-full md:w-9/12 w-full"
          >
            Nuestro servicio de atención al cliente está disponible, los 7 días
            de la semana al
            <span class="font-semibold cursor-pointer">55 5296 - 7027</span> o
            <span class="font-semibold cursor-pointer"
              >enidservice@gmail.com</span
            >
          </p>
        </div>

        <!-- Recycle Grid Card -->

        <div class="">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6 text-white"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>

          <h3
            class="text-xl leading-5 dark:text-white font-semibold text-white lg:mt-10 mt-8"
          >
            Piedes hoy y recibes hoy
          </h3>
          <p
            class="text-base leading-6 font-normal dark:text-gray-300 text-gray-100 mt-4 lg:w-full md:w-9/12 w-full"
          >
            <span class="font-bold">
              Llegan HOY 
            </span>
            en CDMX y área metropolitana y de uno a dos días en los
            estados
          </p>
        </div>

        <!-- Secure Payment Card -->

        <div class="">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6 text-white"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z"
            />
          </svg>

          <h3
            class="text-xl leading-5 dark:text-white font-semibold text-white lg:mt-10 mt-8"
          >
            Pago seguro
          </h3>
          <p
            class="text-base leading-6 font-normal dark:text-gray-300 text-gray-100 mt-4 lg:w-full md:w-9/12 w-full"
          >
            90 días para 
            <span class="font-bold">
              devoluciones 
            </span>
            y pago contra entrega en CDMX
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>