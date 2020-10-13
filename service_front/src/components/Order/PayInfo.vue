<template>
  <div class="pay-info-wrap">
    <h2 class="pay-info-title">최종 결제 금액</h2>
    <div class="pay-info-table">
      <div class="pay-row">
        <span class="total-price">총 상품 금액</span>
        <span v-if="orderlist.price === undefined" class="total-price-value"
          >{{ this.totalPrice.toLocaleString() }}원</span
        >
      </div>
      <div class="pay-row">
        <span class="shipping-fee">총 배송비</span>
        <span class="shipping-fee-value">0원</span>
      </div>
      <div class="pay-row">
        <span class="last-price">예상 금액</span>
        <span class="last-price-value"
          >{{ this.totalPrice.toLocaleString() }}원</span
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["orderlist"],
    computed: {
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
  },
};
</script>

<style lang="scss" scoped>
.pay-info-wrap {
  .pay-info-title {
    margin-top: 90px;
    padding-bottom: 10px;
    font-size: 1.8em;
    border-bottom: 1px solid black;
  }
  .pay-info-table {
    padding: 20px 0;
    border-bottom: 1px solid black;
    span {
      margin: auto 0;
    }
    .pay-row {
      display: flex;
      justify-content: space-between;
      padding: 10px 20px;
      .last-price {
        font-size: 1.7em;
        font-weight: bold;
      }
      .last-price-value {
        font-size: 1.7em;
        font-weight: bold;
        color: red;
      }
    }
  }
}
</style>
