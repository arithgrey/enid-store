import { createStore } from 'vuex';

export default createStore({
  state: {    
    user: localStorage.getItem('user') || null,
    token: localStorage.getItem('token') || null,
    refresh_token: localStorage.getItem('refresh_token') || null,
    profile: localStorage.getItem('profile') || null,
    storeId:1,
    cart: JSON.parse(localStorage.getItem('cart')) || [],
    showDialog: false,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
      localStorage.setItem('user', user);
    },
    setToken(state, token) {
      state.token = token;
      localStorage.setItem('token', token);
    },
    setRefreshToken(state, refresh_token) {
      state.refresh_token = refresh_token;
      localStorage.setItem('refresh_token', refresh_token);
    },
    setProfile(state, profile) {
      state.profile = profile;
      localStorage.setItem('profile', profile);
    },
    clearToken(state) {
      state.token = null;
      localStorage.removeItem('token');
      localStorage.removeItem('refresh_token');      
    },
    addToCart(state, product) {
      const existingItem = state.cart.find(item => item.product.id === product.id);
      if (existingItem) {
        existingItem.quantity++;
      } else {
        state.cart.push({ product: product, quantity: 1 });
      }
      localStorage.setItem('cart', JSON.stringify(state.cart));
    },
    removeFromCart(state, product) {
      state.cart = state.cart.filter(item => item.product.id !== product.id);
      localStorage.setItem('cart', JSON.stringify(state.cart));
    },
    updateQuantity(state, { productId, quantity }) {
      const item = state.cart.find(item => item.product.id === productId);
      if (item) {
        item.quantity = quantity;
      }
    },
    clearCart(state) {
      state.cart = [];
      localStorage.removeItem('cart');
    },
  },
  getters: {
    storeId(state){
      return state.storeId;
    },
    user(state) {
      return state.user;
    },
    isAuthenticated(state) {
      return state.token !== null;
    },
    totalItemsInCart: (state) => {
      return state.cart.reduce((total, item) => total + item.quantity, 0);
    },
    getProductsFromCart: (state) => {
      return state.cart.map(item => ({
        ...item.product,
        quantity: item.quantity
      }));
    }
  },
  actions: {

  },
});
