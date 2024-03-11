export default class OrderHelper {
  constructor(order) {
    this.order = order || { items: [] };
  }

  totalPriceQuantity() {
    if (!this.order || !this.order.items) {
      return 0;
    }

    const total = this.order.items.reduce((acc, item_order) => {
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

  totalItems() {
    if (!this.order || !this.order.items) {
      return 0;
    }

    return this.order.items.reduce((acc, item_order) => acc + item_order.quantity, 0);
  }
}
