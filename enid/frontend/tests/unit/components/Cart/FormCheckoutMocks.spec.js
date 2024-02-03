import { mount, shallowMount } from '@vue/test-utils';
import FormComponent from '@/components/Cart/FormCheckout.vue';

describe('FormCheckout.vue', () => {
  it('should call $store.commit when status is 201 and navigate to the correct page', async () => {
    
    const mocks = {
      $store: {
        commit: jest.fn(),
      },
      $router: {
        push: jest.fn(),
      },
    };

    const wrapper = shallowMount(FormComponent, {
      global: {
        mocks,
      },
    });

    
    let response = { status: 201, data: { id: 1 } };    
    await wrapper.vm.nextToSaveOrder(response);
    await wrapper.vm.$nextTick();

    expect(mocks.$store.commit).toHaveBeenCalledWith('clearCart');

    expect(mocks.$router.push).toHaveBeenCalledWith({
      name: 'order-detail',
      params: { id: response.data.id }, 
    });

  });
});



describe('FormCheckout.vue', () => {
  it('should call $store.commit when status is 201 and navigate to the correct page', async () => {
    
    const mocks = {
      $store: {
        commit: jest.fn(),
      },
      $router: {
        push: jest.fn(),
      },
    };

    const wrapper = shallowMount(FormComponent, {
      global: {
        mocks,
      },
    });

    
    let response = { status: 400, data: {"stripe_error":"error con stripe"} };    
    await wrapper.vm.nextToSaveOrder(response);
    await wrapper.vm.$nextTick();
   
    expect(wrapper.vm.stripe_message_error).toBe(response.data.stripe_error);
    expect(mocks.$store.commit).not.toHaveBeenCalled();
    expect(mocks.$router.push).not.toHaveBeenCalled();


  });
});