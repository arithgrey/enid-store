export function chargeUserLead() {

    this.sendUserLead = true;

    const userLead = this.form;
    const user_data = {
        name: userLead.name,
        email: userLead.email,
        phone_number: userLead.phone_number,
        lead_type:2
    }

    this.$axios.post(`/lead/existence/`, user_data)
        .then(response => {

            if(response.status === 201){
                
                console.log("User was joined!")
            }else{
                
                this.sendUserLead = true;
            }            
            
        })
        .catch(error => {
            this.sendUserLead = false;
            console.error("Error al realizar la solicitud de logout:", error);
        });

}
