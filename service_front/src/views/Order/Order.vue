<template>
  <div>
    <nav-bar></nav-bar>
    <div class="order-container">
      <div class="page-title">
        <h1>주문하기</h1>
      </div>
      <order-info :orderlist="orderList"></order-info>
      <orderer-info :ordererlist="ordererList"></orderer-info>
      <ship-info :ordererlist="ordererList" :shiplist="shipList"></ship-info>
      <pay-info :orderlist="orderList"></pay-info>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavBar from "../../components/Nav/Nav.vue";
import OrderInfo from "../../components/Order/OrderInfo.vue";
import OrdererInfo from "../../components/Order/OrdererInfo.vue";
import ShipInfo from "../../components/Order/ShipInfo.vue";
import PayInfo from "../../components/Order/PayInfo.vue";

export default {
  components: {
    NavBar,
    OrderInfo,
    OrdererInfo,
    ShipInfo,
    PayInfo,
  },
  data: () => ({
    orderList: [],
    ordererList: {
      name: "",
      phone1: "",
      phone2: "",
      phone3: "",
      vertifynum: "",
      email1: "",
      email2: "",
    },
    shipList: {
      name: "",
      phone1: "",
      phone2: "",
      phone3: "",
      address: "",
      memo: "",
    },
  }),
  created: function () {
    if (localStorage.length > 0) {
      this.orderList.push(localStorage.key("data"));
    }
  },
};
</script>

<style lang="scss">
.page-title {
  display: flex;
  justify-content: center;
  margin: 30px 0 50px 0;
  padding: 40px 0 20px 0;
  h1 {
    font-size: 1.9em;
    font-weight: 600;
  }
}
.order-container {
  display: flex;
  flex-direction: column;
  justify-items: center;
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 20px;
  outline: none;
  :focus {
    outline: none;
  }
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
