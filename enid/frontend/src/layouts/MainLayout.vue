<template>
  <div>
    <div class="fixed top-0 left-0 right-0 z-50 bg-white">
      <ShippingAndReturns
        v-if="!isAuthenticated"
        @open_shopping_cart="handleOpenCart"
        @open_seccion_login="handleOpenLogin"
        @open_search_products="handleOpenSearchProducts"
      />
      <AccountMenu
        v-if="isAuthenticated"
        @open_shopping_cart="handleOpenCart"
        @open_seccion_login="handleOpenLogin"
        @open_search_products="handleOpenSearchProducts"
      />
    </div>
    <div class="relative mt-32 mb-8">
      <!-- Contenido de la página aquí -->
      <div class="relative">
        <router-view
          @open_shopping_cart_product_list="handleOpenCartOnViews"
          @open_seccion_login="handleOpenLogin"
        />
      </div>
      <ShoppingCartList ref="shoppingCartList" />
      <LoginForm ref="loginForm" />
      <SearchFormProduct ref="searchFormProduct" />
      <div class="flex-shrink-0">
        <Footer v-if="display_footer" @open_seccion_login="handleOpenLogin" />
      </div>
    </div>
  </div>
</template>

<script>
import ShippingAndReturns from "@/components/Banner/ShippingAndReturns.vue";
import AccountMenu from "@/components/Banner/AccountMenu.vue";
import ShoppingCartList from "@/components/Cart/ShoppingCartList.vue";
import LoginForm from "@/components/Login/LoginForm.vue";
import SearchFormProduct from "@/components/Search/ProductsForm.vue";
import Footer from "@/layouts/Footer.vue";

export default {
  components: {
    ShippingAndReturns,
    ShoppingCartList,
    LoginForm,
    Footer,
    SearchFormProduct,
    AccountMenu,
  },
  data() {
    return {
      display_footer: true,
    };
  },
  methods: {
    handleOpenSearchProducts() {
      this.$refs.searchFormProduct.openSearch();
    },
    handleOpenCart() {
      this.$refs.shoppingCartList.openCart();
    },
    handleOpenCartOnViews() {
      this.$refs.shoppingCartList.openCart();
    },
    handleOpenLogin() {
      this.$refs.loginForm.openForm();
    },

    redirectToLoginPageIfNecessary(to, from, next) {
      const requiresAuth = to.meta && to.meta.requiresAuth;
      const isAuthenticated = this.$store.getters.isAuthenticated;

      if (requiresAuth && !isAuthenticated) {
        this.$router.push("/");
      } else {
        next();
      }
    },
  },
  beforeRouteEnter(to, from, next) {
    next((vm) => {
      vm.redirectToLoginPageIfNecessary(to, from, next);
    });
  },
  beforeRouteUpdate(to, from, next) {
    next((vm) => {
      vm.redirectToLoginPageIfNecessary(to, from, next);
    });
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
  },
  watch: {
    "$store.getters.isAuthenticated"(newValue, oldValue) {
      if (!newValue) {
        this.$router.push("/");
      }
    },
  },
};
</script>
