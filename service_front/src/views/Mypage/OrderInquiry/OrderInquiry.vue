<template>
  <div class="order-inquiry-wrap">
    <div class="page-box">
      <div class="order-no-data" v-if="viewNoData">
        주문한 상품이 없습니다.
      </div>
      <div v-if="viewData">
        <div v-for="orderItem in productData" v-bind:key="orderItem.id">
          <h2 class="order-title">{{ orderItem.order_date }}<span></span> 
          {{ orderItem.order_number }}<router-link to="/order/detail"><div class="btn-order">주문상세보기<img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-titleic-detailpage-moreaction@3x.png" /></div></router-link></h2>
          <div class="delivery-title">브랜디 배송 상품</div>
          <div class="delivery-icon"><img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-seller-xl@3x.png" />상품</div>
          <orderData v-bind:propsdata="detailItem" v-for="detailItem in orderItem.order_details" v-bind:key="detailItem.id"></orderData>
          <div class="buttons-box">
            <button class="refundBtn" @click="refundBtn">환불요청</button>
            <button class="cancelBtn" @click="cancelBtn">주문취소</button>
          </div>
        </div>
      </div>
    </div>
    <!-- mobile 레이아웃 -->
    <div class="mobile-box">
        <div class="mobile-iconbox">
          <ul>
            <li>
              <div class="text-box">
                <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-my-point-s@3x.png" />
                <br/>
                <span>포인트 <p class="point-color"></p></span>
              </div>
            </li>
            <li>
              <router-link to="/mypage/coupon">
              <div class="text-box">
                <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-mypage-coupon-s@3x.png" />
                <br/>
                <span>쿠폰 <p class="point-color">{{ $store.state.couponNum }}</p></span>
              </div>
              </router-link>
            </li>
            <li>
              <router-link to="/mypage">
              <div class="text-box">
                <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-mypage-orderlist-s@3x.png" />
                <br/>
                <span>주문/배송조회</span>
              </div>
              </router-link>
            </li>
          </ul>
        </div>
        <div class="divide"></div>
        <div class="my-shopping">
          <h3>MY쇼핑</h3>
          <div class="shopping-box">
            <ul>
              <li>
                <div>
                  <a>
                    <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/ic-myshopping-basket@3x.png" />
                    <span>장바구니 <p class="num-color">1</p></span>
                  </a>
                </div>
              </li>
              <li>
                <router-link to="/mypage/qna">
                <div>
                  <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/ic-myshopping-qna@3x.png" />
                  <span>Q&A</span>
                </div>
                </router-link>
              </li>
              <li>
                <div>
                  <a>
                    <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/ic-myshopping-faq@3x.png" />
                    <span>FAQ</span>
                  </a>
                </div>
              </li>
              <li>
                <div>
                  <a>
                    <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/ic-myshopping-basket-copy@3x.png" />
                    <span>로그아웃</span>
                  </a>
                </div>
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
              <span>10:00-17:00 (점심시간 12:30-13:30), 주말 및 공휴일 휴무</span>
            </li>
            <li>
              <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/f-market-icon-store-call@3x.png" />
              <span>1566 - 6575</span>
              <button>전화하기</button>
            </li>
            <li>
              <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/customer-kakao@3x.png" />
              <span>브랜디</span>
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
    viewNoData: false,
    viewData: false,
    productData: [],
    mobilePageName: '',
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
      url: 'http://10.251.1.174/orders',
      method: 'GET',
      headers: { 
        'Authorization': this.$cookies.get('accesstoken')
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

  .mobile-box{
    display: none;
  }
}

@media screen and (min-width: 769px){
  .order-inquiry-wrapp{
    max-width: 1300px;
    margin: 0 auto;

    .mobile-box{
      display: none;
    }
  }
}

@media screen and (max-width: 400px){
  .order-inquiry-wrap{
    margin: 55px 0 180px 0;

    .order-no-data{
      display: none;
    }

    .mobile-box{
      display: block;

      .mobile-iconbox{

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
          text-align: center;    color: #1e1e1e;
          font-size: 14px;
          color: #1e1e1e;

          a{
            color: #1e1e1e;
          }

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
          align-items: center;
          border-top: solid 1px #e1e1e1;
          border-bottom: solid 1px #e1e1e1;
          line-height: 15px;
          color: #1e1e1e;

          a{
            padding: 7px 10px;
            font-size: 13px;
            line-height: 15px;
            color: #1e1e1e;

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
}

[v-cloak] {
display: none;
}
</style>