import ValidationRules from "@/rules/ValidationRules.js";

export const rules = {
    name: ValidationRules.nameRules(),
    email: ValidationRules.emailRules(),
    phone_number: ValidationRules.phoneNumberRules(),
    postal_code: ValidationRules.postalCodeRules(),
    street: ValidationRules.streetRules(),
    number: ValidationRules.numberRules(),
    interior_number: ValidationRules.interiorNumberRules(),
    colony: ValidationRules.colonyRules(),
    delegation_or_municipality: ValidationRules.delegationOrmunicipalityRules(),
    city: ValidationRules.cityRules()
};

export const rulesSigned = {
    phone_number: ValidationRules.phoneNumberRules(),
    postal_code: ValidationRules.postalCodeRules(),
    street: ValidationRules.streetRules(),
    number: ValidationRules.numberRules(),
    interior_number: ValidationRules.interiorNumberRules(),
    colony: ValidationRules.colonyRules(),
    delegation_or_municipality: ValidationRules.delegationOrmunicipalityRules(),
    city: ValidationRules.cityRules()
};