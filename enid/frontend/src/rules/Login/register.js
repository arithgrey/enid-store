import { helpers } from "@vuelidate/validators";
import { nameCommonRule, passwordCommonRule, emailCommonRule } from "@/rules/commonRules.js";

export const rules = {
  name: {
    ...nameCommonRule,
  },

  email: {
    ...emailCommonRule
  },

  password: {
    ...passwordCommonRule,
  },

  password_confirm: {
    ...passwordCommonRule,
    sameAsPassword: helpers.withMessage(
      "Las contraseñas no coinciden",
      (value, vm) => {

        return value === vm.password;
      }
    ),
  },
};
