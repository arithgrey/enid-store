class CartHelper {
    constructor(store) {
      this.store = store;
    }
  
    formattedPrice(price) {
      return price.toLocaleString("es-MX", {
        style: "currency",
        currency: "MXN",
        minimumFractionDigits: 2,
      });
    }
  
    getTotalPriceQuantity() {
      const total = this.store.getters.getProductsFromCart.reduce((acc, product) => {
        let total_quantity = product.price * product.quantity;
        return acc + total_quantity;
      }, 0);
  
      return this.formattedPrice(total);
    }
  }
  
  export default CartHelper;
  