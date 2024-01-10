<template>
  <div>
    <Banner />
    <BannerOffert />
    <div class="mx-auto xs:w-full md:w-10/12">
      <ProductList @open_shopping_cart_product_list="handleOpenCartProductList" />
    </div>
    <div class="mx-auto xs:w-full">
      <TrusthHome />
      <Community />      
    </div>
    <div class="mx-auto xs:w-full md:w-10/12  lg:mt-20">
      <SpecialsAndReleases/>
    </div>
  </div>
</template>

<script >
import ProductList from "@/components/Products/ProductList.vue";
import Banner from "@/components/Banner/Banner.vue";
import BannerOffert from "@/components/Banner/BannerOffert.vue";
import TrusthHome from "@/components/Trusth/TrusthHome.vue";
import Community from "@/components/Trusth/Community.vue";
import SpecialsAndReleases from "@/components/Collections/SpecialsAndReleases.vue";


export default {
  components: {
    ProductList,
    Banner,
    BannerOffert,
    TrusthHome,
    Community,
    SpecialsAndReleases
  },
  methods: {
    handleOpenCartProductList() {      
      this.$emit("open_shopping_cart_product_list");
    },
  },
};
</script>
