<template>
  <div class="pt-6">
    <section class="py-12 sm:py-16">
      <div class="container mx-auto px-4">
        <div
          class="lg:col-gap-12 xl:col-gap-16 mt-8 grid grid-cols-1 gap-12 lg:mt-12 lg:grid-cols-5 lg:gap-16"
        >
          <div class="lg:col-span-3 lg:row-end-1">
            <ProductBreadcrumb :product="product" />
            <ProductDetailGalery :product="product" />
          </div>

          <div class="lg:col-span-2 lg:row-span-2 lg:row-end-2">
            <ProductAddToCart :product="product" @open_shopping_cart_product="handle_open_shoping_cart" />
          </div>

          <div class="lg:col-span-3">
            <ProductDescription :product="product" />
          </div>
          <ProductVarianList :product="product"  />
        </div>
      </div>
    </section>

    

    
    
  </div>
</template>

<script>

import ProductBreadcrumb from "@/components/Products/ProductBreadcrumb.vue";
import ProductDetailGalery from "@/components/Products/ProductDetailGalery.vue";
import ProductAddToCart from "@/components/Products/ProductAddToCart.vue";
import ProductDescription from "@/components/Products/ProductDescription.vue";

export default {
  components: {    
    ProductBreadcrumb,
    ProductDetailGalery,
    ProductAddToCart,
    ProductDescription,
  },
  data() {
    return {
      product:[],
      
    };
  },
  mounted() {
    this.fetchProduct();
    window.scrollTo({ top: 0, behavior: "smooth" });
  },
  methods: {
    async fetchProduct() {
      const categorySlug = this.$route.params.categorySlug;
      const productSlug = this.$route.params.productSlug;

      try {
        const response = await this.$axios.get(
          `productos/${categorySlug}/${productSlug}/`
        );
        this.product = response.data;
        this.mainImagePreview()
      } catch (error) {
        console.error("Error al obtener los datos:", error);
      }
    },
    handle_open_shoping_cart(){
      
      this.$emit("open_shopping_cart_product");
    },
    mainImagePreview() {
      
      const mainImage = this.product.images.find((img) => img.is_main);
      const imageURL = mainImage ? mainImage.get_image_url : "https://enidservices.com/imgs/04.jpg";
      const ogImageMetaTag = document.querySelector('meta[property="og:image"]');  
      
      const specific_name = this.product.specific_name;
      document.title = specific_name;
      if (ogImageMetaTag) {
        ogImageMetaTag.setAttribute('content', imageURL);
      }
    
    },
  },
  watch: {
    '$route': 'fetchProduct'
  },
};
</script>