import { passwordCommonRule, emailCommonRule } from "@/rules/commonRules.js";

export const rules = {  
  email: {
    ...emailCommonRule
  },

  password: {
    ...passwordCommonRule,
  },  
};
