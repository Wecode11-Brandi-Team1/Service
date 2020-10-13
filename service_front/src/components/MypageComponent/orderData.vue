<template>
  <div class="delivery-wrap">
    <div class="order-item">
      <dl>
        <dt><a>{{ propsdata.seller_name }}</a></dt>
        <dt></dt>
        <dt>주문금액</dt>
        <dt>진행상황</dt>
      </dl>
      <dl class="order-info">
        <dd>
          <img :src="propsdata.images" />
        </dd>
        <dd>
          <span class="item-title">{{ propsdata.product_name }}</span>
          <span>{{ propsdata.color }}/{{ propsdata.size }}</span>
          <span>{{ propsdata.quantity }} 개</span>
        </dd>
        <dd>
          <strong>{{ Number(propsdata.final_price).toLocaleString() }} 원</strong>
        </dd>
        <dd>
          <strong v-if="propsdata.order_detail_statuses_id === 1">결제완료</strong>
          <strong v-else-if="propsdata.order_detail_statuses_id=== 2">상품준비중</strong>
          <strong v-else-if="propsdata.order_detail_statuses_id === 3">배송중</strong>
          <strong v-else-if="propsdata.order_detail_statuses_id === 4">배송완료</strong>
          <strong v-else-if="propsdata.order_detail_statuses_id === 5">구매확정</strong>
          <strong v-else-if="propsdata.order_detail_statuses_id === 6">주문취소완료</strong>
          <strong v-else-if="propsdata.order_detail_statuses_id === 7">환불요청</strong>
          <strong v-else-if="propsdata.order_detail_statuses_id === 8">환불완료</strong>
        </dd>
      </dl>
    </div>
    <dl class="buttons-box" v-if="propsdata.order_detail_statuses_id === 1 || propsdata.order_detail_statuses_id=== 2 || propsdata.order_detail_statuses_id === 3 || propsdata.order_detail_statuses_id === 4">
        <dd>
          <button class="refundBtn" @click="refundBtn" v-if="propsdata.order_detail_statuses_id === 3 || propsdata.order_detail_statuses_id=== 4">환불요청</button>
          <button class="cancelBtn" @click="cancelBtn" v-if="propsdata.order_detail_statuses_id === 1 || propsdata.order_detail_statuses_id === 2">주문취소</button>
        </dd>
      </dl>
  </div>
</template>

<script>
import { axios } from '../../plugins/axios'

export default {
  data:()=>({

  }),
  props:['propsdata', 'date'],
  methods:{
    refundBtn(){
      if (confirm('선택하신 주문을 환불하시겠습니까?')) {
        localStorage.setItem('refundData', JSON.stringify(this.propsdata));
        localStorage.setItem('date', JSON.stringify(this.date));
        this.$router.push({path: '/mypage/refund'});
      }
    },
    cancelBtn(){
      if (confirm('선택하신 주문을 취소하시겠습니까?')) {
        localStorage.setItem('cancelData', JSON.stringify(this.propsdata));
        localStorage.setItem('date', JSON.stringify(this.date));
        this.$router.push({path: '/mypage/cancel'});
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.delivery-wrap{
  .delivery-title{
    font-size: 26px;
    font-weight: bold;
    border-bottom: 1px solid #000;
    padding-top: 20px;
    padding-bottom: 20px;
  }

  .delivery-icon{
    font-size: 21px;
    font-weight: bold;
    padding: 21px 0px;

    img{
      height: 27px;
      vertical-align: text-bottom;
      margin-bottom: 2px;
      margin-right: 2px;
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
        border-top: 1px solid #e1e1e1;
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

        &:last-child{
          width: 215px;
        }
      }
    }
  }

  .buttons-box{
    width: 100%;
    border-top: 1px solid #ddd;
    padding: 10px 0;
    margin: 0;

    dd{
      width: 100% !important;
      text-align: end;
      margin: 0;
      
      .refundBtn{
        height: 42px;
        font-size: 13px;
        color: #000;
        border: 1px solid #000;
        background: #fff;
        padding: 10px 25px;

        &:focus{
          outline: none;
        }
      } 

      .cancelBtn{
        height: 42px;
        font-size: 13px;
        color: #fff;
        border: 1px solid #000;
        background: #000;
        padding: 10px 25px;

        &:focus{
          outline: none;
        }
      }
    }
  }  
}
</style>