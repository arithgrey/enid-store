import { minLength, maxLength, numeric, between } from "@vuelidate/validators";
import { helpers } from "@vuelidate/validators";
import { required, email } from "@vuelidate/validators";

export const nameCommonRule = {

    minLength: helpers.withMessage(
        "El nombre debe tener al menos 10 caracteres.",
        minLength(10)
    ),
    maxLength: helpers.withMessage(
        "Hey ese nombre es muy largo",
        maxLength(150)
    ),
    required: helpers.withMessage("El nombre es obligatorio.", required),

};

export const passwordCommonRule = {
    minLength: helpers.withMessage(
        "El password debe tener al menos 8 caracteres.",
        minLength(8)
    ),
    maxLength: helpers.withMessage(
        "El password debe tener máximo 20 caracteres.",
        maxLength(40)
    ),
    required: helpers.withMessage("Hey ingresa una contraseña!", required),
};


export const emailCommonRule = {
    required: helpers.withMessage("Hey ingresa un email!", required),
    email: helpers.withMessage("Hey ingresa un email válido!", email),
};