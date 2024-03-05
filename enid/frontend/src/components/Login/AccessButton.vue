<template>
  <div>
    <button
      v-if="!isAuthenticated"
      type="submit"
      class="mx-auto px-5 py-2.5 font-medium tracking-wide text-white bg-black rounded-md hover:bg-gray-900 focus:outline-none transition duration-300 transform active:scale-95 ease-in-out"      
    >
      <span class="pl-2 mx-1">Inicia sesión o regístrate</span>
    </button>
  </div>
</template>

<script>
import OAuthHelper from "@/helpers/OAuth.js";

export default {  
  data() {
    return {
      oauthHelper: new OAuthHelper(this.$store)          
    };
  },  
  computed: {
    isAuthenticated() {
      return this.oauthHelper.isAuthenticated()
    },
  },
};
</script>