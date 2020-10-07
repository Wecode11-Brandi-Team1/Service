<template>
  <div>
    <div class="order-container">
      <div class="page-title">
        <h1>주문하기</h1>
      </div>
      <order-info :orderlist="orderList"></order-info>
      <orderer-info :ordererlist="ordererList"></orderer-info>
      <ship-info :ordererlist="ordererList" :shiplist="shipList"></ship-info>
      <pay-info :orderlist="orderList"></pay-info>
    </div>
    <div class="purchase-wrap">
      <button @click="pushData" class="purchase">결제하기</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import OrderInfo from "../../components/Order/OrderInfo.vue";
import OrdererInfo from "../../components/Order/OrdererInfo.vue";
import ShipInfo from "../../components/Order/ShipInfo.vue";
import PayInfo from "../../components/Order/PayInfo.vue";

export default {
  components: {
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
      phone_number: "",
      address: "",
      address_detail: "",
      memo: "",
    },
  }),
  created: function () {
    // this.orderList.push(localStorage.data);
    // console.log(this.orderList);
    // axios
    //   .get("public/data/mockData/order.json")
    //   .then((res) => (this.orderList = res.data));
  },
  methods: {
    pushData() {
      const accessToken =
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mn0.YHNEVqI1PLALLTpPVComx3VMQZkV0z4CzT_SQk88yY0";
      const headers = {
        headers: { Authorization: accessToken },
      };
      const list = {
        option_id: "1",
        orderer_name: this.ordererList.name,
        orderer_phone_number:
          this.ordererList.phone1 +
          "-" +
          this.ordererList.phone2 +
          "-" +
          this.ordererList.phone3,
        orderer_email: this.ordererList.email1 + "@" + this.ordererList.email2,
        name: this.shipList.name,
        phone_number:
          this.shipList.phone1 +
          "-" +
          this.shipList.phone2 +
          "-" +
          this.shipList.phone3,
        zip_code: this.shipList.address.zonecode,
        address: this.shipList.address.address,
        detail_address: this.shipList.address_detail,
        shipping_memo: this.shipList.memo,
        final_price: 32000,
        quantity: 1,
        price: 32000,
        discount_price: 0,
      };
      axios
        .post("http://10.251.1.174:5000/purchase", list, headers)
        .then((response) => {});
    },
  },
};
</script>

<style lang="scss" scoped>
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
.purchase-wrap {
  display: flex;
  justify-content: center;
  margin: 50px 0;
  .purchase {
    width: 290px;
    height: 79px;
    padding: 25px;
    font-size: 1.25em;
    color: white;
    background-color: black;
  }
}
</style>
