<template>
  <div class="order-detail-wrap">
    <div class="detail-title">
      <h1>주문상세조회</h1>
    </div>
    <div class="detail-box">
      <div class="order-list-box">
          <h2>주문 정보</h2>
          <div class="order-list">
            <dl>
              <dt>주문번호</dt>
              <dd>20200924000035000</dd>
            </dl>
            <dl>
              <dt>주문일자</dt>
              <dd>2020.09.24</dd>
            </dl>
            <dl>
              <dt>주문자</dt>
              <dd>이효정</dd>
            </dl>
            <dl>
              <dt>결제금액</dt>
              <dd>460 원</dd>
            </dl>
            <dl>
              <dt>적립예정포인트</dt>
              <dd>4 원</dd>
            </dl>
          </div>
        </div>
    </div>
    <div class="detail-box">
      <div class="delivery-box">
        <h2>주문 상품</h2>
        <orderData></orderData>
        <div class="delivery-line"></div>
      </div>
    </div>
    <div class="detail-box">
      <div class="payment-box">
          <h2>결제정보</h2>
          <div class="order-list">
            <dl>
              <dt>결제수단</dt>
              <dd>네이버페이</dd>
              <dt>총 상품금액</dt>
              <dd>460 원</dd>
              <dt class="order-totalpay-title">총 주문금액</dt>
              <dd class="order-totalpay-title red">460 원</dd>
            </dl>
          </div>
        </div>
    </div>
    <div class="detail-box">
      <div class="order-list-box">
          <h2>배송지 정보</h2>
          <div class="order-list">
            <dl>
              <dt>수령인</dt>
              <dd>이효정</dd>
            </dl>
            <dl>
              <dt>휴대폰</dt>
              <dd>01063794933</dd>
            </dl>
            <dl>
              <dt>우편번호</dt>
              <dd>10082</dd>
            </dl>
            <dl>
              <dt>주소</dt>
              <dd>경기 김포시 청송로 19</dd>
            </dl>
            <dl>
              <dt>나머지주소</dt>
              <dd>4 원</dd>
            </dl>
            <dl>
              <dt>배송메모</dt>
              <dd>문 앞에 놓아주세요 </dd>
            </dl>
          </div>
        </div>
    </div>
    <div class="btn-wrap">
        <button @click="mypagedBtn">주문/배송조회로 이동</button>
      </div>
</div>
</template>

<script>
import OrderData from '../../../components/MypageComponent/orderData.vue'

export default {
  components:{
    OrderData
  },
  methods:{
    mypagedBtn(){
      this.$router.replace({path: '/mypage'});
    }
  }
}
</script>

<style lang="scss" scoped>
.order-detail-wrap{
  .detail-title{
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 40px 0px 20px 0px;
    margin-bottom: 30px;

    h1{
      font-size: 28px;
      text-align: center;
      margin-bottom: 15px;
    }
  }

  .order-list-box{
    h2{
      font-size: 26px;
      font-weight: 400;
      border-bottom: 1px solid #000;
      margin-top: 50px;
      padding-bottom: 15px;
    } 

    .order-list{
      width: 100%;
      font-size: 1.2em;
      display: table;
      overflow: hidden;
      border-top: 1px solid #000;
      border-bottom: 1px solid #000;
      margin-bottom: 50px;

      dl{
        display: table-row;

        dt{
          width: 20%;
          font-weight: 700;
          display: table-cell;
          vertical-align: middle;
          padding: 10px 15px;
          border-bottom: 1px solid #bdbdbd;
        }

        dd{
          width: 80%;
          font-size: 15px;
          line-height: 39px;
          display: table-cell;
          border-bottom: 1px solid #bdbdbd;
          padding: 10px 15px;
        }
      }
    }
  }

  .delivery-box{
    h2{
      font-size: 26px;
      font-weight: 400;
      border-bottom: 1px solid #000;
      margin-top: 50px;
      padding-bottom: 15px;
    }

    .delivery-line{
      width: 100%;
      border-top: 1px solid #000;
    }
  }

  .detail-box{
    width: 100%;
    padding: 0px 20px;
    margin: 0px auto;
  }

  .payment-box{
    h2{
      font-size: 26px;
      font-weight: 400;
      border-bottom: 1px solid #000;
      margin-top: 50px;
      padding-bottom: 15px;
    } 

    .order-list{
      width: 100%;
      overflow: hidden;
      border-top: 1px solid #000;
      border-bottom: 1px solid #000;
      margin-bottom: 50px;
      padding: 20px 0;

      dl{
        dt{
          width: 50%;
          font-weight: 700;
          float: left;
          padding: 10px 20px;
        }

        dd{
          width: 50%;
          font-size: 15px;
          float: left;
          text-align: right;
          padding: 10px 20px;
        }

        .order-totalpay-title{
          font-size: 26px;
          font-weight: bold;
        }

        .red{
          color: #FF204B;
        }
      }
    }
  }
  

  .btn-wrap{
    display: flex;
    justify-content: center;
    align-items: center;

    button{
      width: 170px;
      height: 50px;
      font-size: 17px;
      text-align: center;
      line-height: 46px;
      color: #ffffff;
      display: block;
      background: #000000;
      border: 1px solid #000000;
      border-radius: 4px;
      padding: 0;

      &:focus{
        outline: none;
      }
    }
  }
}

@media screen and (min-width: 769px){
  .refund-wrap{
    max-width: 1300px;
    margin: 0 auto;
  }
}
</style>