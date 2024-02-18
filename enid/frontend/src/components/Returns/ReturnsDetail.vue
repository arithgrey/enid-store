<template>
  <div class="p-5">
  <h2 class="font-bold text-gray-900 sm:text-3xl sm:tracking-tight">
    {{ returnItem.ask }}
  </h2>
  <h2 class="text-gray-700 dark:text-gray-400 mt-5  border p-3">
    {{ returnItem.short_answer }}
  </h2>

  <h2 class="mb-2 font-semibold text-gray-900 dark:text-white mt-10">
    1) Tu pedido debe estar nuevo, con etiquetas/empaque original.
  </h2>
  <ul class="space-y-1 text-gray-700 list-disc list-inside dark:text-gray-400">
    <li class="list-none text-sm">
      - Los accesorios deben ser devueltos en su estado original, sin ninguna
      alteración o daño.
    </li>
  </ul>
  <h2 class="mb-2 font-semibold text-gray-900 dark:text-white mt-10">
    2) Identifica qué tipo de solicitud deseas realizar:
  </h2>
  <ul class="space-y-1 text-gray-700 list-disc list-inside dark:text-gray-400">
    <li class="list-none text-sm">
      - Devolución de producto para reembolso (Retracto de compra)
    </li>
    <li class="list-none text-sm">- Cambio</li>
  </ul>
  <h2 class="mb-2 font-semibold text-gray-900 dark:text-white mt-10">
    3) Selecciona la forma para devolver tu paquete de acuerdo a tus
    necesidades.
  </h2>
  <ul class="space-y-1 text-gray-700 list-disc list-inside dark:text-gray-400">
    <li class="list-none text-sm">
      - Pick up: nuestro socio logístico acudirá a tu domicilio para recoger el
      paquete(Tendrá un costo de 100 pesos) o
    </li>
    <li class="list-none text-sm">
      - Drop off: podrás llevarlo directamente a la sucursal de nuestro socio
      logístico más cercana
    </li>
  </ul>
  <h2 class="mb-2 font-semibold text-gray-900 dark:text-white mt-10">
    4) Una vez el socio logístico reciba tu devolución, será enviada a nuestro
    almacén para validar las condiciones del artículo(s), en caso den o cumplir
    con las condiciones te retornaremos tu artículo.
  </h2>

  <h2 class="mb-2 font-semibold text-gray-900 dark:text-white mt-10">
    5) Si tu devolución es autorizada, recibirás una notificación de que tu
    devolución fue exitosamente procesada.
  </h2>
  <ul class="space-y-1 text-gray-700 list-disc list-inside dark:text-gray-400">
    <li class="list-none text-sm">
      - Si elegiste el reembolso de tu dinero, este será gestionado de acuerdo
      al método de pago utilizado en tu compra original.
    </li>
    <li class="list-none text-sm">
      - Si elegiste cambio, este será enviado a tu domicilio en un periodo de
      entre 1 y 2 días después de tu solicitud
    </li>
  </ul>
  </div>
</template>
<script>
export default {
  data() {
    return {
      returnItem: [],
    };
  },
  mounted() {
    this.fetchItem();
  },
  methods: {
    async fetchItem() {
      try {
        const response = await this.$axios.get(
          `/devoluciones/${this.$route.params.id}`
        );
        this.returnItem = response.data;
      } catch (error) {
        console.error("Error fetching FAQ list:", error);
      }
    },
  },
};
</script>
