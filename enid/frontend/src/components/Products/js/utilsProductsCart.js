export function totalPriceQuantity(items_order) {

    const total = items_order.reduce((acc, item_order) => {
        let total_quantity = item_order.price * item_order.quantity;
        return acc + total_quantity;
    }, 0);

    return formattedPrice(total);
}

export function formattedPrice(price) {

    return price.toLocaleString("es-MX", {
        style: "currency",
        currency: "MXN",
        minimumFractionDigits: 2,
    });
}
