<template>
    <div class="grid grid-cols-2 gap-x-4">
    <div class="group relative text-sm">
      <router-link :to="{ name: 'product-list', hash: '#top-sellers' }">
        <div
          class="aspect-h-1 aspect-w-1 overflow-hidden rounded-lg bg-gray-100 group-hover:opacity-75"
        >
          <img
            src="https://enidservices.com/imgs/04.jpg"
            alt="Las fotos de referencias, nuestros clientes"
            class="object-cover object-center"
          />
        </div>

        <span class="absolute inset-0 z-10" aria-hidden="true" />
        Ya sabes los top
      </router-link>
    </div>
    <div class="group relative text-sm">
      <router-link :to="{ name: 'referencias' }">
        <div
          class="aspect-h-1 aspect-w-1 overflow-hidden rounded-lg bg-gray-100 group-hover:opacity-75"
        >
          <img
            src="https://enidservices.com/imgs/05.jpg"
            alt="Las fotos de referencias, nuestros clientes"
            class="object-cover object-center"
          />
        </div>

        <span class="absolute inset-0 z-10" aria-hidden="true" />
        Las referencias
      </router-link>
    </div>
    </div>
</template>