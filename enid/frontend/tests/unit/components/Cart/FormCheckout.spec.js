import { mount, shallowMount } from '@vue/test-utils';
import FormComponent from '@/components/Cart/FormCheckout.vue';


let fieldNamesAddress = {
  "phone_number": {
    "message": "Hey ingresa tu número tefónico!",
    "minLength": 10,
    "maxLength": 12,
  },
  "postal_code": {
    "message": "Hey ingresa tu código postal!",
    "minLength": 4,
    "maxLength": 8,
  },
  "street": {
    "message": "Ingresa el nombre de tu calle!",
    "minLength": 4,
    "maxLength": 100,
  },
  "number": {
    "message": "Hey falta tu número de casa!"
  },
  "colony": {
    "message": "Indica cual es tu colonia!",
    "minLength": 4,
    "maxLength": 50,
  },
  "delegation_or_municipality": {
    "message": "Falta tu Delegación!",
    "minLength": 4,
    "maxLength": 50,
  },
  "city": {
    "message": "Ingresa tu ciudad!",
    "minLength": 3,
    "maxLength": 50,
  }
};

describe('Max Lengths', () => {
  Object.entries(fieldNamesAddress).forEach(([key, value]) => {
    it(`mark an error on maxLength input- ${key}`, () => {

      const wrapper = mount(FormComponent);
      if (typeof value === 'object' && 'maxLength' in value) {
        let minLengthwrong = value["maxLength"] + 1;
        const validator = wrapper.vm.v$.form[key];

        wrapper.setData({
          form: {
            [key]: 'a'.repeat(minLengthwrong)
          }
        });

        validator.$touch();
        expect(validator.$errors[0].$validator).toBe("maxLength");
      }

    });
  });


});

describe('Min Lengths', () => {

  Object.entries(fieldNamesAddress).forEach(([key, value]) => {
    it(`mark an error on minLength input- ${key}`, () => {

      const wrapper = mount(FormComponent);
      if (typeof value === 'object' && 'minLength' in value) {
        let minLengthwrong = value["minLength"] - 1;
        const validator = wrapper.vm.v$.form[key];

        wrapper.setData({
          form: {

            [key]: 'a'.repeat(minLengthwrong)

          }
        });

        validator.$touch();
        expect(validator.$errors[0].$validator).toBe("minLength");
      }

    });
  });


});



describe('Requireds', () => {

  let fieldNamesUser = {
    "email": "Hey ingresa un email!",
    "name": "El nombre es obligatorio."
  };

  Object.entries(fieldNamesUser).forEach(([key, value]) => {
    it(`mark an error on required  - ${key}`, () => {

      const wrapper = mount(FormComponent);

      const validator = wrapper.vm.v$.form[key];
      validator.$touch();
      expect(validator.$errors[0].$validator).toBe("required");
      expect(validator.$errors[0].$message).toEqual(value);

    });
  });


  Object.entries(fieldNamesAddress).forEach(([key, value]) => {
    it(`mark an error on required - ${key}`, () => {

      const wrapper = mount(FormComponent);
      const validator = wrapper.vm.v$.form[key];
      validator.$touch();
      expect(validator.$errors[0].$validator).toBe("required");
      expect(validator.$errors[0].$message).toEqual(value["message"]);

    });
  });

});


describe('Email Validation', () => {


  it('formats email correct', () => {

    const wrapper = mount(FormComponent);
    const emailValidator = wrapper.vm.v$.form.email;

    wrapper.setData({
      form: {

        email: 'arithgrey@gmail.com'

      }
    });

    emailValidator.$touch();
    expect(emailValidator.$error).toBeFalsy();

  });


  it('mark an error on blank', () => {

    const wrapper = mount(FormComponent);
    const emailValidator = wrapper.vm.v$.form.email;

    wrapper.setData({
      form: {
        email: ''
      }
    });

    emailValidator.$touch();
    expect(emailValidator.$errors[0].$validator).toBe("required");
    expect(emailValidator.$errors[0].$message).toBe("Hey ingresa un email!");

  });

  it('marks an error on false email', () => {

    const wrapper = mount(FormComponent);
    const emailValidator = wrapper.vm.v$.form.email;

    wrapper.setData({
      form: { email: 'arithgrey@slsl¿' }
    });

    emailValidator.$touch();
    expect(emailValidator.$error).toBeTruthy();
    expect(emailValidator.$errors[0].$validator).toBe('email');

  });

});



describe('Phone Number Formatting', () => {

  it('formats phone number by removing non-numeric characters', () => {
    const wrapper = mount(FormComponent);
    wrapper.setData({
      form: {

        phone_number: '123,-4qQ@56-7890'

      }
    });

    wrapper.vm.formatPhoneNumber();
    expect(wrapper.vm.form.phone_number).toBe('1234567890');

  });


  it('return phone number wite 12 numbers not more', () => {
    const wrapper = mount(FormComponent);
    wrapper.setData({
      form: {

        phone_number: '123,-4qQ@56-78911111110'

      }
    });

    wrapper.vm.formatPhoneNumber();
    expect(wrapper.vm.form.phone_number.length).toBe(12);

  });



});



describe('number house big or small number', () => {

  it('Mark error on big number', () => {
    const wrapper = mount(FormComponent);
    const validator = wrapper.vm.v$.form.number;

    wrapper.setData({
      form: {

        number: 11111111111111

      }
    });

    validator.$touch();
    expect(validator.$errors[0].$validator).toEqual('between');

  });

  it('Mark error on small number', () => {
    const wrapper = mount(FormComponent);
    const validator = wrapper.vm.v$.form.number;

    wrapper.setData({
      form: {

        number: 0

      }
    });

    validator.$touch();
    expect(validator.$errors[0].$validator).toEqual('between');

  });

  it('Mark error on big interior_number ', () => {
    const wrapper = mount(FormComponent);
    const validator = wrapper.vm.v$.form.interior_number;

    wrapper.setData({
      form: {
        interior_number: 11111111111111
      }
    });

    validator.$touch();
    expect(validator.$errors[0].$validator).toEqual('between');

  });

  it('Mark error on small interior_number', () => {
    const wrapper = mount(FormComponent);
    const validator = wrapper.vm.v$.form.interior_number;

    wrapper.setData({
      form: {

        interior_number: 0

      }
    });

    validator.$touch();
    expect(validator.$errors[0].$validator).toEqual('between');

  });


});

describe('Utility Functions', () => {

  it('should remove non-numeric characters', () => {
    const wrapper = shallowMount(FormComponent);
    expect(wrapper.vm.cleanNonNumericChars('123-456-7890')).toBe('1234567890');
    expect(wrapper.vm.cleanNonNumericChars('abc123def456')).toBe('123456');
  });

  it('should remove non-characters numeric ', () => {
    const wrapper = shallowMount(FormComponent);
    expect(wrapper.vm.cleanNonChars('a12b3-4c56-7d890')).toBe('abcd');
    expect(wrapper.vm.cleanNonChars('abc123def456 ef g')).toBe('abcdef ef g');
  });

});


describe('Rendering', () => {
  it('renders correctly', () => {
    const wrapper = mount(FormComponent);
    expect(wrapper.exists()).toBe(true);
  });
});

describe('Computeds', () => {

  it('computes isContactInfo correctly when all fields are valid', async () => {

    const wrapper = shallowMount(FormComponent);
    const validator = wrapper.vm.v$.form.email;
    wrapper.setData({
      form: {
        email: 'test@example.com',
        name: 'John Doe',
        phone_number: '1234567890'

      }
    });

    validator.$touch();
    expect(wrapper.vm.isContactInfo).toBe(true);

  });

  it('computes isContactInfo false when one field are not valid', async () => {

    const wrapper = shallowMount(FormComponent);
    const validator = wrapper.vm.v$.form.email;
    wrapper.setData({
      form: {

        email: 'test@exampl..e.com',
        name: 'John Doe',
        phone_number: '1234567890'

      }
    });

    validator.$touch();
    expect(wrapper.vm.isContactInfo).toBe(false);

  });

  it('computes isContactInfo false when one field is black', async () => {

    const wrapper = shallowMount(FormComponent);
    const validator = wrapper.vm.v$.form.email;
    wrapper.setData({
      form: {
        email: 'test@example.com',
        name: '',
        phone_number: '1234567890'
      }
    });

    validator.$touch();
    expect(wrapper.vm.isContactInfo).toBe(false);

  });


});