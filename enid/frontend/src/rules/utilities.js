export function formatPassword() {
    
    this.v$?.form.password.$touch()
}
export function formatPasswordConfirm() {
    
    this.v$?.form.password_confirm.$touch()    
}

export function formatEmail() {
    
    this.v$?.form.email.$touch()
    this.form.email = this.form.email.toLowerCase();
}


export function formatName() {
    this.v$?.form.name.$touch();
    this.form.name = this.cleanNonChars(this.form.name);
}


export function formatInteriorNumber() {
    this.form.interior_number = this.cleanNonNumericChars(
        this.form.interior_number
    );

    if (this.form.interior_number.length > 4) {
        this.form.interior_number = this.form.interior_number.slice(0, 4);
    }
}

export function formatNumber() {
    this.form.number = this.cleanNonNumericChars(this.form.number);
    this.v$?.form.number.$touch();

    if (this.form.number.length > 4) {
        this.form.number = this.form.number.slice(0, 5);
    }
}

export function formatPostalCode() {
    this.v$?.form.postal_code.$touch();
    this.form.postal_code = this.cleanNonNumericChars(this.form.postal_code);

    if (this.form.postal_code.length > 8) {
        this.form.postal_code = this.form.postal_code.slice(0, 8);
    }
}

export function formatPhoneNumber() {
    this.v$?.form.phone_number.$touch();

    this.form.phone_number = this.cleanNonNumericChars(
        this.form.phone_number
    );

    if (this.form.phone_number.length > 12) {
        this.form.phone_number = this.form.phone_number.slice(0, 12);
    }
}

export function cleanNonNumericChars(str) {
    return str.replace(/[^0-9]/g, "");
}

export function cleanNonChars(str) {
    
    let currentStr = str.replace(/[^a-zA-Z\s]/g, "");
    return currentStr.toLowerCase();
}

export function formatError(error) {
    return error[0];
}
export function cleanErrors() {
    
    this.stripe_message_error = "";
    Object.keys(this.errors).forEach((field) => {
        this.errors[field] = "";
    });
    
}

export function cleanFields() {
    Object.keys(this.form).forEach((field) => {
        if (field != "products") {
            this.form[field] = "";
        } else {
            this.form[field] = [];
        }
    });

    this.cleanErrors("clearCart");
}