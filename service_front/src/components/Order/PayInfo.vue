<template>
  <div class="pay-info-wrap">
    <h2 class="pay-info-title">최종 결제 금액</h2>
    <div class="pay-info-table">
      <div class="pay-row">
        <span class="total-price">총 상품 금액</span>
        <span class="total-price-value"
          >{{ (orderlist.price * orderlist.count).toLocaleString() }}원</span
        >
      </div>
      <div class="pay-row">
        <span class="shipping-fee">총 배송비</span>
        <span class="shipping-fee-value">0원</span>
      </div>
      <div class="pay-row">
        <span class="last-price">예상 금액</span>
        <span class="last-price-value"
          >{{ (orderlist.price * orderlist.count).toLocaleString() }}원</span
        >
      </div>
    </div>
    <div class="purchase-wrap">
      <button class="purchase">결제하기</button>
    </div>
  </div>
</template>

<script>
export default {
  props: ["orderlist"],
};
</script>

<style lang="scss">
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
