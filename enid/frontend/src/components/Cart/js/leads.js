export function chargeUserLead() {

    this.sendUserLead = false;

    const products = this.$store.getters.getProductsFromCart;
    const productIds = products.map(product => product.id);

    const userLead = this.form;
    const user_data = {
        name: userLead.name,
        email: userLead.email,
        phone_number: userLead.phone_number,
        lead_type: 2,
        products_interest: productIds
    }

    this.$axios.post(`/lead/existence/`, user_data)
        .then(response => {

            if (response.status === 201) {

                console.log("User was joined!")
                this.sendUserLead = true;
            }            
        })
        .catch(error => {

            console.error("Error al realizar la solicitud de logout:", error);
        });

}
