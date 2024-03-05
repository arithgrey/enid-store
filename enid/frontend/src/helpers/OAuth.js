export default class OAuthHelper {
    constructor(store) {
      this.store = store;
    }
  
    isAuthenticated() {
      return this.store.getters.isAuthenticated;
    }
  
  }