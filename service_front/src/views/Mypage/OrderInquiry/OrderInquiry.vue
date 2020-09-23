<template>
  <div class="order-inquiry-wrap">
    <div class="page-box">
      <div class="order-no-data" v-if="viewNoData">
        주문한 상품이 없습니다.
      </div>
      <h2 v-if="viewData" class="order-title">{{ productData.data ? productData.data[0].created_at : '' }}<span></span> 
      {{ productData.data ? productData.data[0].order_detail_id : '' }}<router-link to="/order/detail"><div class="btn-order">주문상세보기<img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-titleic-detailpage-moreaction@3x.png" /></div></router-link></h2>
      <orderData v-if="viewData" v-bind:propsdata="productData"></orderData>
      <div class="buttons-box" v-if="viewData">
        <button class="refundBtn" @click="refundBtn">환불요청</button>
        <button class="cancelBtn" @click="cancelBtn">주문취소</button>
      </div>
    </div>

    <div class="mobile-box">
        <div class="mobile-iconbox">
          <ul>
            <li>
              <div class="text-box">
                <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-my-point-s@3x.png" />
                <br/>
                <span>포인트 <p class="point-color">1</p></span>
              </div>
            </li>
            <li>
              <div class="text-box">
                <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-mypage-coupon-s@3x.png" />
                <br/>
                <span>쿠폰 <p class="point-color">1</p></span>
              </div>
            </li>
            <li>
              <div class="text-box">
                <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-mypage-orderlist-s@3x.png" />
                <br/>
                <span>주문/배송조회</span>
              </div>
            </li>
          </ul>
        </div>
        <div class="divide"></div>
        <div class="my-shopping">
          <h3>MY쇼핑</h3>
          <div class="shopping-box">
            <ul>
              <li>
                <a>
                  <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/ic-myshopping-basket@3x.png" />
                  <span>장바구니 <p class="num-color">1</p></span>
                </a>
              </li>
              <li>
                <a>
                  <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/ic-myshopping-qna@3x.png" />
                  <span>Q&A</span>
                </a>
              </li>
              <li>
                <a>
                  <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/ic-myshopping-faq@3x.png" />
                  <span>FAQ</span>
                </a>
              </li>
              <li>
                <a>
                  <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/ic-myshopping-basket-copy@3x.png" />
                  <span>로그아웃</span>
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div class="divide"></div>
        <div class="information">
          <h3>정보</h3>
          <div class="shopping-box">
            <ul>
              <li>
                <a>
                  <span>개인정보처리방침</span>
                </a>
              </li>
              <li>
                <a>
                  <span>이용약관</span>
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div class="divide"></div>
        <div class="service">
          <h3>고객센터</h3>
          <div class="summary">
            하단의 카카오톡 문의 혹은 브랜디 고객센터 전화 버튼을 눌러주시면 빠르고 정확한 답변을 받아보실 수 있습니다.
          </div>
        </div>
        <div class="service-icon">
          <ul>
            <li>
              <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/f-market-icon-store-time@3x.png" />
              <sapn>10:00-17:00 (점심시간 12:30-13:30), 주말 및 공휴일 휴무</sapn>
            </li>
            <li>
              <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/f-market-icon-store-call@3x.png" />
              <sapn>1566 - 6575</sapn>
              <button>전화하기</button>
            </li>
            <li>
              <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/customer-kakao@3x.png" />
              <sapn>브랜디</sapn>
              <button>카톡하기</button>
            </li>
          </ul>
        </div>
      </div>
  </div>
</template>

<script>
import { axios } from '../../../plugins/axios';
import OrderData from '../../../components/MypageComponent/orderData.vue';

export default {
  data:() => ({
    pageName:'orderList',
    viewNoData:false,
    viewData:false,
    productData:[]
  }),
  props:['propsdata'],
  components:{
    OrderData
  },
  methods:{
    refundBtn(){
      if (confirm('선택하신 주문을 환불하시겠습니까?')) {
        this.$router.push({path: '/mypage/refund'});
      }
    },
    cancelBtn(){
      if (confirm('선택하신 주문을 취소하시겠습니까?')) {
        this.$router.push({path: '/mypage/cancel'});
      }
    },
  },
  mounted: function () {
    this.$store.state.myPageTabName = this.pageName;
    this.$store.state.myPageShow = true;
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
      this.viewData = true;
      this.viewNoData = false;
    })
    .catch((error) => {
      console.log(error);
      this.viewData = false;
      this.viewNoData = true;
    })
  }
}
</script>

<style lang="scss" scoped>
.order-inquiry-wrap{
  .page-box{
    width: 100%;
    padding: 0px 20px;
    margin: 0px auto;

    .order-no-data{
      font-size: 16px;
      text-align: center;
      color: #1e1e1e;
      padding: 50px 0 0 0;
    }
  }

  .order-title{
    font-size: 26px;
    font-weight: bold;
    color: #1e1e1e;
    border-bottom: 3px solid #000;
    padding-bottom: 16px;
    margin-top: 100px;

    span{
      border-right: solid 2px #000;
      margin: 0 10px;
      padding-top: 19px;
      font-size: 0;
      line-height: 0;
    }

    .btn-order{
      font-size: 24px;
      color: #1e1e1e;
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

  .buttons-box{
    width: 100%;
    text-align: right;
    border-top: 1px solid #e1e1e1;
    border-bottom: 1px solid  #000;
    padding: 21px 0px;

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

@media screen and (min-width: 769px){
  .mypage-wrap{
    max-width: 1300px;
    margin: 0 auto;

    .mobile-box{
      display: none;
    }
  }
}

@media screen and (max-width: 400px){
  .mypage-wrap{
    .order-no-data{
      display: none;
    }

    .mobile-iconbox{
      display: block;

      ul{
        width: 100%;
        height: 94px;
        display: flex;
        border-top: 1px solid #e1e1e1;
        border-bottom: 1px solid #e1e1e1;
        background-color: #fff;
        margin: 0;

        li{
          width: 33.3%;
          display: flex;
          align-items: center;
          justify-content: center;
          text-align: center;
          font-size: 14px;

          &:nth-child(2){
            border-left: 1px solid #e1e1e1;
            border-right: 1px solid #e1e1e1;
          }

          .text-box{
            height: 61px;

            img{
              width: 40px;
              height: 40px;
            }

            span{
              font-weight: 700;

              .point-color{
                font-weight: bold;
                color: #FF204B;
                display: inline;
              }
            }
          }
        }
      }
    }

    .divide{
      width: 100%;
      height: 5px;
      border: none;
      background: #f5f5f5;
      border-bottom: 1px solid #ececec;
    }

    .my-shopping{
      h3{
        font-size: 14px;
        font-weight: bold;
        margin: 0;
        padding: 16px 12px;
      }

      ul{
        margin: 0;

        li{
          height: 52px;
          display: flex;
          border-top: solid 1px #e1e1e1;
          border-bottom: solid 1px #e1e1e1;
          line-height: 15px;

          a{
            padding: 7px 10px;
            font-size: 13px;
            line-height: 15px;

            img{
              width: 40px;
              height: 40px;
              margin-top: -2px;
              vertical-align: middle;
            }

            .num-color{
              color: #FF204B;
              display: inline-block;
            }
          }

          &:nth-child(2){
              border-top: none;
          }

          &:nth-child(3){
              border-top: none;
          }

          &:nth-child(4){
              border-top: none;
          }
        }
      }
    }

    .information{
      h3{
        font-size: 14px;
        font-weight: bold;
        margin: 0;
        padding: 16px 12px;
      }

      ul{
        margin: 0;

        li{
          height: 52px;
          display: flex;
          align-items: center;
          border-top: solid 1px #e1e1e1;
          border-bottom: solid 1px #e1e1e1;
          line-height: 15px;

          a{
            padding: 7px 10px;
            font-size: 13px;
            line-height: 15px;
          }

          &:nth-child(2){
            border-top: none;
          }
        }
      }
    }

    .service{
      border-bottom: 1px solid #e1e1e1;

      h3{
        font-size: 14px;
        font-weight: bold;
        margin: 0;
        padding: 16px 12px;
      }

      .summary{
        padding: 0 20px 16.5px 12px;
        font-size: 11px;
        color: #4a4a4a;
      }
    }

    .service-icon{
      height: 40px;
      line-height: 40px;
      font-size: 11px;
      padding: 0 12px;
      margin-top: 12px;

      img{
        width: 16px;
        height: 16px;
        vertical-align: middle;
        margin-right: 8px;
      }

      button{
        height: 28px;
        font-size: 11px;
        color: #4a4a4a;
        line-height: 26px;
        float: right;
        border: 1px solid #000;
        border-radius: 8px;
        background-color: #fff;
        padding: 0 11px;
        margin: 6px 0;
      }
    }
  }
}

[v-cloak] {
display: none;
}
</style>