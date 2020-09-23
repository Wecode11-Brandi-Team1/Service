<template>
  <div class="mypage-iconbox">
    <div class="iconbox-wrap">
      <ul>
        <li>
          <router-link to="/mypage">
            <a :class="['icon-wrap', isActive[$store.state.myPageTabName][0]]" v-if="$store.state.myPageTabName">
              <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-mypage-orderlist-s@3x.png" />
              <br/>
              <span>주문/배송조회</span>
            </a>
          </router-link>
        </li>
        <li>
          <a :class="['icon-wrap', isActive[$store.state.myPageTabName][1]]" v-if="$store.state.myPageTabName">
            <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-my-point-s@3x.png" />
            <br/>
            <span>포인트 <p class="point-color">{{ number.num1 }}</p></span>
          </a>
        </li>
        <li>
          <router-link to="/mypage/coupon">
            <a :class="['icon-wrap', isActive[$store.state.myPageTabName][2]]" v-if="$store.state.myPageTabName">
              <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-mypage-coupon-s@3x.png" />
              <br/>
              <span>쿠폰 <p class="point-color">{{ number.num2 }}</p></span>
            </a>
          </router-link>
        </li>
        <li>
          <router-link to="/mypage/qna">
            <a :class="['icon-wrap', isActive[$store.state.myPageTabName][3]]" v-if="$store.state.myPageTabName">
              <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-mypage-qna-s@3x.png" />
              <br/>
              <span>Q & A</span>
            </a>
          </router-link>
        </li>
        <li> 
          <a :class="['icon-wrap', isActive[$store.state.myPageTabName][4]]" v-if="$store.state.myPageTabName">
            <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-myshopping-faq-s@3x.png" />
            <br/>
            <span>FAQ</span>
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data:()=>({
    isActive:{
      orderList: ["on", "none", "none", "none", "none"],
      point: ["none", "on", "none", "none", "none"],
      coupon: ["none", "none", "on", "none", "none"],
      qna: ["none", "none", "none", "on", "none"],
      faq: ["none", "none", "none", "none", "on"],
    },
    number:{
      num1:0,
      num2:1,
    }
  }),
}
</script>

<style lang="scss" scoped>
.mypage-iconbox{
  .iconbox-wrap{
    display: block;
    background-color: #fafafa;
    border: 1px solid #000000;
    overflow: hidden;
    padding: 50px 0;

    ul{
      display: flex;
      justify-content: center;
      align-items: center;

      li{
        width: 20%;
        display: block;
        text-align: center;
        border-right: 1px solid #000;

        &:last-child{
          border-right: none;
        }

        .icon-wrap{
          font-size: 15.5px;
          color: #7d7d7d;

          img{
            width: 75px;
            opacity: 0.4;
          }

          span{
            &::after {
            content: "";
            width: 7px;
            height: 7px;
            display: inline-block;
            border: 1px solid #cdcdcd;
            border-left: 0;
            border-top: 0;
            transform: rotate(-45deg);
            vertical-align: 2px;
            margin-left: 3px;
            }

            .point-color{
              font-weight: bold;
              color: #FF204B;
              display: inline;
            }
          }
        }

        .on{
          font-weight: bold;
          color: #000;

          img{
            opacity: 1;
          }

          span{
            &::after {
              border-color: #3c3c3c;
            }
          }
        }

        a{
          &:hover{
            color: #FF204B;
            text-decoration: none;
            cursor: pointer;
          }
        }
      }
    }
  }
}

@media screen and (max-width: 400px){
  .mypage-iconbox{
    .iconbox-wrap{
      display: none;
    }
  }
}
</style>