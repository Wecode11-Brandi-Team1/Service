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
      </div>
      <div class="product-list" v-for="item in getData()" :key="item.option_id">
        <div class="order-row">
          <span class="brand">{{ item.seller_name }}</span>
          <span class="blank"></span>
          <span class="blank"></span>
          <span class="coupon">쿠폰적용</span>
          <span class="price">주문금액</span>
        </div>
        <div class="order-row">
          <div class="product-wrap">
            <span class="product-img">
              <img alt="product image" :src="item.img_url" />
            </span>
            <span class="product-info">
              <ul>
                <li>{{ item.orderer_name }}</li>
                <li class="grey">{{ item.select_option }}</li>
                <li class="grey">{{ item.quantity }}개</li>
              </ul>
            </span>
          </div>
          <span class="blank"></span>
          <span class="coupon-label">
            <span class="coupon-list"
              ><select>
                <option value="">쿠폰을 선택하세요</option>
                <option>회원가입 축하쿠폰(2,000원 할인)</option>
                <option>회원가입 축하쿠폰(2,000원 할인)</option>
              </select></span
            >
          </span>
          <span class="price-value"
            >{{ (item.price * item.quantity).toLocaleString() }}원</span
          >
        </div>
      </div>
    </div>
    <div class="total-price-wrap">
      <span class="total-price">총 주문금액&nbsp;</span>
      <span class="total-price-value"
        >{{ this.totalPrice.toLocaleString() }}원</span
      >
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    totalPrice() {
      let sum = 0;
      for (let i = 0; i < this.getData().length; i++) {
        sum +=
          parseFloat(this.getData()[i].price) *
          parseFloat(this.getData()[i].quantity);
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
    .coupon-label {
      padding: 0;
      background-color: #f5f5f5;
      background-image: url("https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-arrow-bl-down@3x.png");
      background-size: 13px;
      background-position: 95% 50%;
      span {
        margin: 0;
        padding: 0;
        select {
          padding: 10px 30px;
          font-size: 0.8em;
          color: #9e9e9e;
        }
      }
    }
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
