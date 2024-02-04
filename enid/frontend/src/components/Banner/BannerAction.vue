<template>
  <div>
    <p
      class="flex h-7 items-center uppercase justify-center bg-slate-950 px-4 text-xs font-medium text-white sm:px-6 lg:px-8"
    >
      {{ currentText }}
    </p>
    <p
      class="h-5 text-center bg-gray-100 px-4 text-sm sm:px-6 lg:px-8"
    >
      Pide y recibe hoy y hasta 12 Meses sin intereses 
    </p>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    const textosAlternativos = [
      "+ GRATIS envíos a todo México",
      "Cambios y devoluciones gratis",
      'Recibe el mismo día',
      "Pago contra entrega en CDMX",
      "Garantía extendida",
      "OFERTAS FESTIVAS: HASTA 50% + DESCUENTOS EXTRA",
    ];

    const currentIndex = ref(0);

    const currentText = ref(textosAlternativos[0]);

    const alternarTexto = () => {
      currentIndex.value = (currentIndex.value + 1) % textosAlternativos.length;
      currentText.value = textosAlternativos[currentIndex.value];
    };

    // Inicia la rotación cuando el componente está montado
    onMounted(() => {
      setInterval(alternarTexto, 1500); // Change text every second
    });

    return {
      currentText,
    };
  },
};
</script>
