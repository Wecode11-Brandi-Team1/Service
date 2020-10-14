<template>
  <div>
    <div class="order-container">
      <div class="page-title">
        <h1>주문하기</h1>
      </div>
      <order-info :orderlist="orderList"></order-info>
      <orderer-info :ordererlist="ordererList"></orderer-info>
      <ship-info :ordererlist="ordererList"></ship-info>
      <pay-info :orderlist="orderList"></pay-info>
    </div>
    <div class="purchase-wrap">
      <button @click="pushData" class="purchase">결제하기</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {config} from "../../api/apiConfig"
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
  }),
  computed: {
    getDiscountPrice() {
      let result = [];
      if (this.getData().length > 0) {
        for (let i = 0; i < this.getData().length; i++) {
          result.push(this.getData()[i].discount_price);
        }
      }
      return result;
    },
    getOptionId() {
      let result = [];
      if (this.getData().length > 0) {
        for (let i = 0; i < this.getData().length; i++) {
          result.push(this.getData()[i].option_id);
        }
      }
      return result;
    },
    getQuantity() {
      let result = [];
      if (this.getData().length > 0) {
        for (let i = 0; i < this.getData().length; i++) {
          result.push(this.getData()[i].quantity);
        }
      }
      return result;
    },
    getPrice() {
      let result = [];
      if (this.getData().length > 0) {
        for (let i = 0; i < this.getData().length; i++) {
          result.push(this.getData()[i].price);
        }
      }
      return result;
    },
    getFinalPrice() {
      let result = [];
      if (this.getData().length > 0) {
        for (let i = 0; i < this.getData().length; i++) {
          result.push(this.getData()[i].final_price);
        }
      }
      return result;
    },
    totalPrice() {
      let sum = 0;
      for (let i = 0; i < this.getData().length; i++) {
        sum +=
          (this.getData()[i].price) *
          (this.getData()[i].quantity);
      }
      return sum;
    },
  },
  methods: {
    getData() {
      return JSON.parse(localStorage.getItem("data"));
    },
    pushData() {

      const accessToken = this.$cookies.get('accesstoken')
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
        name: this.$store.state.shipList.name,
        phone_number:
          this.$store.state.shipList.phone1 +
          "-" +
          this.$store.state.shipList.phone2 +
          "-" +
          this.$store.state.shipList.phone3,
        zip_code: this.$store.state.shipList.address.zonecode,
        address: this.$store.state.shipList.address.address,
        detail_address: this.$store.state.shipList.address_detail,
        shipping_memo: this.$store.state.shipList.memo,
        option_id: this.getOptionId,
        quantity: this.getQuantity,
        price: this.getPrice,
        coupon_id: [1, 1],
        discount_price: this.getDiscountPrice,
        final_price: this.getFinalPrice,
        total_price: this.totalPrice
      };
      axios
        .post(`${config.API}purchase`, list, headers)
        .then((response) => {this.$router.push('/order/result')});
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
