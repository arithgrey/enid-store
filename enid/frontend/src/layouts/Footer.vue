<template>
  <footer v-if="show && !isAuthenticated">
    <div
      class="flex flex-col items-center bg-neutral-950 text-center text-white"
    >
      <div class="container px-6 pt-6">
        <!-- Newsletter sign-up form -->
        <div>
          <div
            class="gird-cols-1 grid items-center justify-center gap-4 md:grid-cols-3"
          >
            <div class="md:mb-6 md:ml-auto">
              <p class="">
                <strong>¿Las pedirás después?</strong>
              </p>
            </div>

            <!-- Newsletter sign-up submit button -->
            <div class="mb-6 md:ml-auto">
              <button
                type="button"
                @click="openJoin"
                class="inline-block rounded border-2 border-neutral-50 px-6 pb-[6px] pt-2 text-xs font-medium uppercase leading-normal text-neutral-50 transition duration-150 ease-in-out hover:border-neutral-100 hover:bg-neutral-500 hover:bg-opacity-10 hover:text-neutral-100 focus:border-neutral-100 focus:text-neutral-100 focus:outline-none focus:ring-0 active:border-neutral-200 active:text-neutral-200 dark:hover:bg-neutral-100 dark:hover:bg-opacity-10 border-teal-600"
              >
                Sigamos en contacto!
              </button>
            </div>
          </div>
        </div>

        <!-- Copyright information -->

        <!-- Links section -->
      </div>
    </div>

    <div class="mt-10 p-5 relative z-50 bg-white md:px-8 md:pt-12 pb-6">
      <div class="container">
        <div class="flex flex-wrap">
          <div class="w-full md:w-4/12 border-b ">
            <h4
              class="block antialiased tracking-normal md:text-3xl text-2xl font-semibold leading-snug text-inherit mb-2 !font-semibold !text-primary"
            >
              ¿NECESITAS AYUDA?
            </h4>
            <p
              class="block antialiased text-inherit text-md "
            >
              (55) 5296 - 7027
            </p>
            <div class="md:mt-2 mb-10">
              <a
                href="https://www.facebook.com/enidservicemx/"
                target="_blank"
                rel="noreferrer"
                ><i
                  class="fab fa-facebook-square font-xl align-center mr-2 inline-block items-center justify-center rounded-full 
                  border-[1.5px] border-blue-gray-50  text-center text-primary outline-none focus:outline-none"
                  aria-hidden="true"
                ></i></a
              ><a
                href="https://www.instagram.com/enid_service/"
                target="_blank"
                rel="noreferrer"
                ><i
                  class="fab fa fa-instagram font-xl align-center mr-2 inline-block items-center justify-center rounded-full border-[1.5px] border-blue-gray-50 p-3 text-center text-primary outline-none focus:outline-none"
                  aria-hidden="true"
                ></i></a
              ><a
                href="https://www.youtube.com/watch?v=uLGFEMczLMI&list=PLkKe5-0MzYemmcbj4fR1bgxzJl72M9CPK"
                target="_blank"
                rel="noreferrer"
                ><i
                  class="fab fa fa-youtube font-xl align-center mr-2 inline-block items-center justify-center rounded-full border-[1.5px] border-blue-gray-50 p-3 text-center text-primary outline-none focus:outline-none"
                  aria-hidden="true"
                ></i></a
              ><a
                href="https://www.pinterest.es/enid_service/"
                target="_blank"
                rel="noreferrer"
                ><i
                  class="fab fa fa-pinterest font-xl align-center mr-2 inline-block items-center justify-center rounded-full border-[1.5px] border-blue-gray-50 p-3 text-center text-primary outline-none focus:outline-none"
                  aria-hidden="true"
                ></i
              ></a>
            </div>
          </div>
          <div class="w-full px-4 md:w-7/12">
            <div class="items-top mb-6 flex flex-wrap">
             
              <div class="w-6/12 pt-6  md:px-4 md:pt-0 xl:w-3/12">
                <span class="md:text-center text-md mb-4 block font-bold text-primary text-1xl"
                  >FRECUENTES</span
                >
                <ul class="list-none p-0 m-0">
                  <li>
                    <a
                      href="rastreo"
                      rel="noreferrer"
                      class="md:text-center block py-2 text-sm leading-relaxed text-gray-600 hover:text-primary hover:bg-black hover:text-white transition"
                    >
                      Rastrea tu pedido
                    </a>
                  </li>
                  <li>
                    <a
                      href="/#atencion-al-cliente"
                      rel="noreferrer"
                      class="md:text-center block py-2 text-sm leading-relaxed text-gray-600 hover:text-primary hover:bg-black hover:text-white transition"
                    >
                      Formas de pago
                    </a>
                  </li>
                  <li>
                    <a
                      href="referencias"
                      rel="noreferrer"
                      class="md:text-center block py-2 text-sm leading-relaxed text-gray-600 hover:text-primary hover:bg-black hover:text-white transition"
                    >
                      Las referencias
                    </a>
                  </li>
                  
                </ul>
              </div>
              <div class="w-6/12 pt-6 md:px-4 md:pt-0 xl:w-3/12">
                <span class="md:text-center text-md mb-4 block font-bold text-primary"
                  >PRODUCTOS</span
                >
                <ul class="list-unstyled">
                  <li>
                    <a
                      rel="noreferrer"
                      class="block md:text-center pb-2 text-sm leading-relaxed text-gray-600 hover:text-primary hover:bg-black hover:text-white transition-colors hover:text-primary"
                      href="/"
                      >Novedades</a
                    >
                  </li>
                  <li>
                    <a
                      rel="noreferrer"
                      class="block md:text-center pb-2 text-sm leading-relaxed text-gray-600 hover:text-primary hover:bg-black hover:text-white transition-colors hover:text-primary"
                      href="/#top-sellers"
                      >Lo más pedido</a
                    >
                  </li>
                 
                </ul>
              </div>
              <div class="w-6/12 pt-6 md:px-4 md:pt-0 xl:w-3/12">
                <span
                  class="text-md mb-4 block font-medium font-bold text-primary md:text-center"
                  >OPORTUNIDADES</span
                >
                <ul class="list-unstyled">
                  <li>
                    <a
                      rel="noreferrer"
                      target="_self"
                      class="block py-2 text-sm leading-relaxed text-gray-600 hover:text-white hover:bg-black transition-colors hover:text-primary 
                      md:text-center"
                      href="https://enidservices.com/kits-pesas-barras-discos-mancuernas-fit/simulador-utilidad/"
                      >Simulador de ganancias</a
                    >
                  </li>
                  <li>
                    <a
                      rel="noreferrer"
                      class="block py-2 text-sm leading-relaxed text-gray-600 hover:text-white hover:bg-black md:text-center 
                      transition-colors hover:text-primary "
                      href="https://enidservices.com/kits-pesas-barras-discos-mancuernas-fit/sobre_ventas/"
                    >
                      Programa de afiliados</a
                    >
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="border-t-2">
    <div class="text-gray-950 text-xs mx-auto text-center bg-stone-100 mt-8">
      Sur 16 139, Agrícola Oriental, Iztacalco, 08500 Ciudad de México, CDMX
    </div>
    <p
      class="flex h-7 items-center justify-center text-sm font-extrabold bg-stone-100"
    >
      Todos los derechos reservados ENID SERVICE © 2023
    </p>
  </div>
  </footer>
</template>

<script>
export default {  
  data(){
    return {
      show:true,
    }
  },  
  methods:{
    openJoin(){
      this.$emit("open_seccion_login");
    }
  },
  computed:{
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
  },
  watch: {
    '$route'(newVal, oldVal) {
      this.show = true;
      if(newVal.path.includes('checkout')){
        this.show = false;
      }
    }
  },    
};
</script>
