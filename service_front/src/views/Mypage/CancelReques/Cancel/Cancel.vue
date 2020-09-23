<template>
  <div class="cancel-wrap">
    <div class="cancel-title">
      <h1>주문취소</h1>
    </div>
    <div class="cancel-box">
      <h2>{{ productData.data ? productData.data[0].created_at : '' }} <span></span>{{ productData.data ? productData.data[0].order_detail_id : '' }} <a class="btn-order">주문상세보기<img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-titleic-detailpage-moreaction@3x.png" /></a></h2>
      <div class="order-item">
        <dl>
          <dt><a>{{ productData.data ? productData.data[0].korean_name : '' }}</a></dt>
          <dt></dt>
          <dt>주문금액</dt>
          <dt>진행상황</dt>
        </dl>
        <dl class="order-info">
          <dd>
            <img :src="productData.data ? productData.data[0].main_img : ''" />
          </dd>
          <dd>
            <span class="item-title">{{ productData.data ? productData.data[0].name : '' }}</span>
            <span>{{ productData.data ? productData.data[0].option_color : '' }}/{{ productData.data ? productData.data[0].option_size : '' }}</span>
            <span>{{ productData.data ? productData.data[0].units : '' }} 개</span>
          </dd>
          <dd>
            <strong>{{ productData.data ? Number(productData.data[0].price).toLocaleString() : '' }} 원</strong>
          </dd>
          <dd>
            <strong>상품준비중</strong>
          </dd>
        </dl>
      </div>
    </div>
    <div class="totalpay-box">
    <h2>주문 취소 정보</h2>
      <dl class="order-totalpay">
        <dd class="order-totalpay-title">총 주문취소금액</dd>
        <dd class="order-totalpay-title red order-rigth">{{ productData.data ? Number(productData.data[0].price).toLocaleString() : '' }} 원</dd>
      </dl>
    </div>
    <div class="btn-wrap">
      <button @click="cancelResultBtn">주문취소하기</button>
    </div>
</div>
</template>

<script>
import { axios } from '../../../../plugins/axios';

export default {
  data:() => ({
    productData:[],
  }),
  methods:{
    cancelResultBtn(){
      if (confirm('선택하신 주문을 취소하시겠습니까?')) {
        this.$store.state.cancelTotal = this.productData.data[0].price;
        this.$router.push({path: '/mypage/cancel/result'});
      }
    }
  },
  mounted: function () {
    axios({
      url: 'http://10.251.1.113:5000/api/order/item',
      method: 'GET',
      headers: { 
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozMTZ9.S9rb5I0Z7Ud5hEbaYhKqqnUZpKNkwFQbkrjoM6grtX0'
      }
    })
    .then((response) => {
      console.log(response.data.data);
      this.productData = response.data;
    })
    .catch((error) => {
      console.log(error);
      alert('주문한 내역이 없습니다. 상품을 확인해주세요.');
      this.$router.replace({path: '/mypage'});
    })
  }
}
</script>

<style lang="scss" scoped>
.cancel-wrap{
  padding: 0px 20px;

  .cancel-title{
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

  .cancel-box{
    h2{
    font-size: 26px;
    padding-bottom: 16px;
    margin-top: 50px;

    span{
      border-right: solid 2px #000;
      margin: 0 10px;
      padding-top: 19px;
      font-size: 0;
      line-height: 0;
    }

    a{
      font-weight: bold;
    }
  }

  .btn-order{
      font-size: 24px;
      float: right;
      margin-top: 3px;

      img{
        width: 10px;
        height: 27px;
        max-height: 20px;
        vertical-align: text-bottom;
        margin-left: 4px;
        margin-bottom: 4px;
      }
    } 
  }

  .order-item{
    width: 100%;
    display: table;

    dl{
      width: 100%;
      display: table-row;

      dt{
        display: table-cell;
        vertical-align: middle;
        text-align: center;
        font-weight: 400;
        border-top: 1px solid #1e1e1e;
        padding: 10px;

        &:first-child{
          text-align: left;
          padding: 19px 10px;
          a{
            font-weight: bold;
          }
        }
      }

      dd{
        display: table-cell;
        text-align: center;
        border-top: 1px solid #e1e1e1;
        border-bottom: 1px solid #1e1e1e;
        vertical-align: middle;

        &:first-child{
          width: 10%;
          padding: 15px 10px;

          img{
            width: 95px;
            height: 95px;
            display: block;
          }
        }

        &:nth-child(2){
          text-align: left;
        }

        .item-title{
          font-weight: 400;
          font-size: 16px;
          color:#000;
          display: block;
          margin-bottom: 4px;
        }

        span{
          font-size: 16px;
          font-weight: 300;
          color: #9e9e9e;
          display: block;
        }

        strong{
          font-size: 19px;
          color: #1e1e1e;
        }
      }
    }
  }

  .totalpay-box{
    h2{
      font-size: 26px;
      padding-bottom: 16px;
      margin-top: 50px;
    }

    .order-totalpay{
      font-size: 15px;
      overflow: hidden;
      border-top: 1px solid #000;
      border-bottom: 1px solid #000;
      margin-bottom: 50px;
      padding: 20px 0;

      dd{
        width: 50%;
        text-align: left;
        float: left;
        padding: 10px 20px;
      }

      .order-totalpay-title{
        font-size: 26px;
        font-weight: bold;
      }

      .red{
        color: #FF204B;
      }

      .order-rigth{
        text-align: right;
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
  .cancel-wrap{
    max-width: 1300px;
    margin: 0 auto;
  }
}

</style>