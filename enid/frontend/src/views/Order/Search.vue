<template>
  <div class="container mx-auto px-4 flex flex-col items-center min-h-screen mb-10">
    <div class="mb-5">
      <SearchForm ref="searchForm" :api="api" @list_orders="handlerOrders" />
    </div>
    <div class="border-t w-full mb-5 flex">
      <div class="search-orders w-1/4 mr-4 mt-5 overflow-y-auto max-h-90">
        <ItemListOrder :orders="orders"  @selected_order="handleSelectedOrder"/>
      </div>

      <div class="description-order w-3/4 mt-5 border p-5" ref="descriptionOrder">
        <DetailOrder :order="selectedOrder"/>
      </div>
    </div>
  </div>
</template>

<script>
import SearchForm from "@/components/Order/SearchForm.vue";
import DetailOrder from  "@/components/Order/DetailOrder.vue";
import ItemListOrder from "@/components/Order/ItemListOrder.vue";
import {timePassed}  from "@/helpers/time.js";

export default {
  components: {
    SearchForm,
    DetailOrder,
    ItemListOrder
  },
  data() {
    return {
      orders: null,
      selectedOrder: null,
      api:'/order-search/',
    };
  },
  methods: {
    timePassed,
    handlerOrders(orders) {      
            
      this.orders = orders;
    },   
    handleSelectedOrder(order) {      
      this.selectedOrder = order;
      this.$refs.descriptionOrder.scrollIntoView({ behavior: 'smooth' });

    },    
    callSubmitForm() {
      
      this.$refs.searchForm.submitForm();
    },
  },
  mounted() {
    
    this.callSubmitForm();
  },
  
};
</script>
