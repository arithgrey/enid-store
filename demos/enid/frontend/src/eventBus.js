import { reactive, provide } from 'vue';

const eventBus = reactive({
  listeners: {},
  
  $on(event, callback) {
    if (!this.listeners[event]) {
      this.listeners[event] = [];
    }
    this.listeners[event].push(callback);
  },
  
  $off(event, callback) {
    const index = this.listeners[event]?.indexOf(callback);
    if (index > -1) {
      this.listeners[event].splice(index, 1);
    }
  },
  
  $emit(event, ...args) {
    if (this.listeners[event]) {
      this.listeners[event].forEach(callback => {
        callback(...args);
      });
    }
  }
});

provide('eventBus', eventBus);

export default eventBus;
