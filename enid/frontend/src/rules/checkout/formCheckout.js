import { minLength, maxLength, numeric, between } from "@vuelidate/validators";
import { helpers } from "@vuelidate/validators";
import { required, email } from "@vuelidate/validators";
export const rules = {
    name: {
      minLength: helpers.withMessage(
        "El nombre debe tener al menos 10 caracteres.",
        minLength(10)
      ),
      maxLength: helpers.withMessage(
        "Hey ese nombre es muy largo",
        maxLength(150)
      ),
      required: helpers.withMessage("El nombre es obligatorio.", required),
    },
  
    email: {
      required: helpers.withMessage("Hey ingresa un email!", required),
      email: helpers.withMessage("Hey ingresa un email válido!", email),
    },
  
    phone_number: {
      required: helpers.withMessage("Hey ingresa tu número tefónico!", required),
      minLength: helpers.withMessage(
        "El teléfono debe tener al menos 10 números!",
        minLength(10)
      ),
      maxLength: helpers.withMessage(
        "El teléfono no puede tener más de 12 números!",
        maxLength(12)
      ),
      numeric: helpers.withMessage("Hey ingresa un teléfono correcto!", numeric),
    },
  
    postal_code: {
      required: helpers.withMessage("Hey ingresa tu código postal!", required),
      minLength: helpers.withMessage(
        "El código postal es muy corto!",
        minLength(4)
      ),
      maxLength: helpers.withMessage(
        "El código postal es muy largo!",
        maxLength(8)
      ),
      numeric: helpers.withMessage("Hey ingresa solo números!", numeric),
    },
  
    street: {
      required: helpers.withMessage("Ingresa el nombre de tu calle!", required),
      minLength: helpers.withMessage(
        "El nombre de tu calle es tan corto?",
        minLength(4)
      ),
      maxLength: helpers.withMessage(
        "El nombre de tu calle es tan largo?",
        maxLength(100)
      ),
    },
    
    number: {
      required: helpers.withMessage("Hey falta tu número de casa!", required),
      between: helpers.withMessage(
        "Hey ingresa solo números correctos!",
        between(1, 1000000)
      ),
    },

    interior_number: {
      required: helpers.withMessage(
        "Hey falta tu número de casa por ejemplo 1!",
        required
      ),
      between: helpers.withMessage(
        "Hey ingresa solo números correctos!",
        between(1, 9999)
      ),
    },
    
    colony: {
      required: helpers.withMessage("Indica cual es tu colonia!", required),
      minLength: helpers.withMessage(
        "Registra el nombre de tu colonia!",
        minLength(4)
      ),
      maxLength: helpers.withMessage(
        "Es tan largo el nombre de tu colonia?",
        maxLength(50)
      ),
    },
  
    delegation_or_municipality: {
      required: helpers.withMessage("Falta tu Delegación!", required),
      minLength: helpers.withMessage("Ingresa tu delegación!", minLength(4)),
      maxLength: helpers.withMessage(
        "Es tan largo el nombre de tu delegación?",
        maxLength(50)
      ),
    },
  
    city: {
      required: helpers.withMessage("Ingresa tu ciudad!", required),
      minLength: helpers.withMessage(
        "Ingresa el nombre de tu ciudad!",
        minLength(3)
      ),
      maxLength: helpers.withMessage(
        "Es tan largo el nombre de tu ciudad?",
        maxLength(50)
      ),
    },
  };
  