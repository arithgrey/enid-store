import { createStore } from 'vuex';

export default createStore({
  state: {
    cart: JSON.parse(localStorage.getItem('cart')) || [],    
    showDialog: false,
  },
  mutations: {
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
