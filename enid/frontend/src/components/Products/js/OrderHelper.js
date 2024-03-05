export default class OrderHelper {
  constructor(items_order) {
    this.items_order = items_order;
  }

  totalPriceQuantity() {
    const total = this.items_order.reduce((acc, item_order) => {
      let total_quantity = item_order.price * item_order.quantity;
      return acc + total_quantity;
    }, 0);
    return this.formattedPrice(total);
  }

  formattedPrice(price) {
    return price.toLocaleString("es-MX", {
      style: "currency",
      currency: "MXN",
      minimumFractionDigits: 2,
    });
  }
}
