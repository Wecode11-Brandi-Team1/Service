<template>
  <div class="delivery-wrap">
    <div class="delivery-title">브랜디 배송 상품</div>
    <div class="delivery-icon"><img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-seller-xl@3x.png" />상품</div>
    <div class="order-item">
      <dl>
        <dt><a>{{ propsdata.data ? propsdata.data[0].korean_name : ''}}</a></dt>
        <dt></dt>
        <dt>주문금액</dt>
        <dt>진행상황</dt>
      </dl>
      <dl class="order-info">
        <dd>
          <img :src="propsdata.data ? propsdata.data[0].main_img : ''" />
        </dd>
        <dd>
          <span class="item-title">{{ propsdata.data ? propsdata.data[0].name : '' }}</span>
          <span>{{ propsdata.data ? propsdata.data[0].option_color : '' }}/{{ propsdata.data ? propsdata.data[0].option_size : '' }}</span>
          <span>{{ propsdata.data ? propsdata.data[0].units : '' }} 개</span>
        </dd>
        <dd>
          <strong>{{ propsdata.data ? Number(propsdata.data[0].price).toLocaleString() : '' }} 원</strong>
        </dd>
        <dd>
          <strong>상품준비중</strong>
          <strong>배송중</strong>
        </dd>
      </dl>
    </div>
  </div>
</template>

<script>
import { axios } from '../../plugins/axios'

export default {
  data:()=>({
  }),
  props:['propsdata'],
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
      }
    }
  }
}
</style>