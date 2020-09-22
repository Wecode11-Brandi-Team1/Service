<template>
  <div class="order-info-wrap">
    <h2 class="order-info-title">브랜디 배송 상품</h2>
    <div class="order-info-table">
      <div class="order-row">
        <span class="normal-delivery">
          <img
            alt="normal delivery"
            src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-seller-xl@3x.png"
          />
          상품
        </span>
        <span></span>
      </div>
      <div class="order-row">
        <span class="brand">{{ orderlist.brand }}</span>
        <span class="price">주문금액</span>
      </div>
      <div class="order-row">
        <div class="product-wrap">
          <span class="product-img">
            <img alt="product image" :src="orderlist.img" />
          </span>
          <span class="product-info">
            <ul>
              <li>{{ orderlist.name }}</li>
              <li class="grey">{{ orderlist.option }}</li>
              <li class="grey">{{ orderlist.count }}개</li>
            </ul>
          </span>
        </div>
        <span class="price-value"
          >{{ (orderlist.price * orderlist.count).toLocaleString() }}원</span
        >
      </div>
    </div>
    <div class="total-price-wrap">
      <span class="total-price">총 주문금액&nbsp;</span>
      <span class="total-price-value"
        >{{ (orderlist.price * orderlist.count).toLocaleString() }}원</span
      >
    </div>
  </div>
</template>

<script>
export default {
  props: ["orderlist"],
};
</script>

<style lang="scss">
.order-info-wrap {
  .order-info-title {
    margin-top: 25px;
    padding-bottom: 20px;
    font-size: 1.8em;
    font-weight: bold;
    border-bottom: 1px solid black;
  }
  .order-info-table {
    border-bottom: 1px solid black;
    span {
      margin: auto 0;
      padding: 18px;
    }
    .order-row {
      display: flex;
      justify-content: space-between;
      border-bottom: 1px solid #e1e1e1;
      .quick-delivery,
      .normal-delivery {
        padding: 15px 0;
        font-size: 1.4em;
        font-weight: bold;
        img {
          position: relative;
          top: -3px;
          width: 112px;
        }
      }
      .arrival-date {
        font-size: 1.4em;
        color: #1e88e5;
      }
      .brand {
        font-size: 1.1em;
        font-weight: bold;
      }
      .product-wrap {
        display: flex;
        margin: auto 0;
        ul {
          margin: 0;
          padding: 0;
        }
        img {
          width: 95px;
          height: 95px;
        }
        .grey {
          color: #9e9e9e;
        }
      }
      .price {
        padding-right: 60px;
        font-size: 1.05em;
      }
      .price-value {
        padding-right: 60px;
        font-weight: bold;
      }
    }
  }
}
.total-price-wrap {
  display: flex;
  justify-content: flex-end;
  margin-top: 30px;
  font-size: 1.8em;
  font-weight: bold;
  .total-price-value {
    color: #ff204b;
  }
}
</style>
