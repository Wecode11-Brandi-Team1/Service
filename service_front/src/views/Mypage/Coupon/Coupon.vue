<template>
  <div class="mypage-wrap">
    <div class="page-box">
      <div class="coupon-box">
        <div class="register">
          <h2>쿠폰 등록하기</h2>
          <div class="register-table">
            <dl>
              <dt>등록</dt>
              <dd>쿠폰코드 등록은 앱에서만 가능합니다.</dd>
            </dl>
          </div>
        </div>
        <div>
        <div class="coupon">
          <h2>발급받은 쿠폰 <strong>{{ couponData.the_number_of_coupons }}</strong><span><span class="coupon-star">* </span>유효기간이 30일 지난 쿠폰은 목록에서 삭제됩니다.</span></h2>
          <div class="coupon-list">
            <dl class="list-header">
              <dt>쿠폰명</dt>
              <dt>사용혜택</dt>
              <dt>사용조건</dt>
              <dt>유효기간</dt>
            </dl>
            <dl v-for="(data,index) in couponData.coupons" v-bind:key="data.id">
              <dd>{{ couponData.coupons[index].coupon_name }}</dd>
              <dd>{{ Number(couponData.coupons[index].discount_price).toLocaleString() }}원 할인</dd>
              <dd>[전체 쿠폰] {{ Number(couponData.coupons[index].minimum_price).toLocaleString() }} 이상 구매시</dd>
              <dd>{{ couponData.coupons[index].valid_ended_at }} ~ {{ couponData.coupons[index].valid_started_at }}</dd>
            </dl>
          </div>
          <div class="coupon-no-data" v-if="isCoupon">
            쿠폰이 존재하지 않습니다.
          </div>
        </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { axios } from '../../../plugins/axios'
import {config} from "../../../api/apiConfig"

export default {
  data:() => ({
    pageName:'coupon',
    couponData:[],
    isCoupon: true,
    mobilePageName:'쿠폰함'
  }),
  mounted: function () {
    this.$store.state.myPageTabName = this.pageName;
    this.$store.state.myPageShow = true;
    this.$store.state.mobilePageName = this.mobilePageName;

    axios({
      url: `${config.API}user/coupons`,
      method: 'GET',
      headers: { 
        'Authorization': this.$cookies.get("accesstoken")
        
      }
    })
    .then((response) => {
      console.log(response.data);
      this.couponData = response.data;
      this.$store.state.couponNum = response.data.the_number_of_coupons;

      if(response.data === "쿠폰이 존재하지 않습니다."){
        this.isCoupon = true;
      }else{
        this.isCoupon = false;
      }
    })
    .catch((error) => {
      this.isCoupon = true;
    })
  }
}
</script>

<style lang="scss" scoped>
.mypage-wrap{
  color: #1e1e1e;
  margin: 0px 0 70px 0 !important;

  .page-box{
    width: 100%;
    padding: 0px 20px;
    margin: 0px auto;

    .coupon-box{
      color: #1e1e1e;
      padding: 50px 0 0 0;

      .register{
        h2{
          font-size: 26px;
          font-weight: 400;
          border-bottom: 1px solid #000;
          padding-bottom: 10px;
          margin: 0;
        }

        .register-table{
          border-bottom: 1px solid #aaa;

          dl{
            text-align: left;
            line-height: 25px;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            overflow: hidden;
            padding: 20px;
            margin: 0;

            dt{
              margin-right: 25px;
            }

            dd{
              font-weight: 500;
              margin-bottom: 0;
            }
          }
        }
      }

      .coupon{
        margin-top: 50px;

        h2{
          font-size: 26px;
          font-weight: 400;
          border-bottom: 1px solid #000;
          padding-bottom: 10px;
          margin: 0;

          span{
            font-size: 14px;
            padding-left: 5px;
          }
        }

        .coupon-list{
          width: 100%;
          display: table;

          .list-header{
            width: 100%;
            display: table-row;

            dt{
              font-size: 16px;
              text-align: center;
              font-weight: bold;
              display: table-cell;
              vertical-align: middle;
              padding: 10px;
              padding-bottom: 10px;
              border-bottom: 1px solid #ccc;
            }
          }

          dl{
            width: 100%;
            display: table-row;

            dd{
              font-size: 16px;
              text-align: center;
              display: table-cell;
              vertical-align: middle;
              border-bottom: 1px solid #ccc;
              padding: 20px;

              &:nth-child(2){
                color: #FF204B;
              }
            }
          }
        }
      }

      .coupon-no-data{
        text-align: center;
        padding: 50px;
        border-bottom: 1px solid #000;
      }
    }
  }
}

@media screen and (min-width: 769px){
  .mypage-wrap {
    max-width: 1300px;
    margin: 0 auto;
  }
}

@media screen and (max-width: 400px){
  .mypage-wrap {
    max-width: 400px;
    margin: 0 auto;
    margin-top: 55px;

    .page-box{
      .coupon-box{
        .register{
          h2{
            font-size: 18.5px;
          }

          .register-table{
            dt{
              font-size: 12px;
              margin-right: 15px;
            }

            dd{
              max-width: 400px;
              font-size: 12px;
            }
          }
        }

        .coupon{
          h2{
            font-size: 18.5px;

            span{
              display: block;
              font-size: 12px;
              padding-left: 0;
              margin-top: 10px;
            }

            .coupon-star{
              display: none;
            }
          }

          .coupon-list{
            .list-header{
              display: none;
            }

            dl{
              dd{
                display: flex;
                flex-direction: column;
                text-align: left;
                margin: 0px;

                &:nth-child(1){
                  font-size: 17.5px;
                  border: none;
                  padding: 20px 20px 0 20px;
                }

                &:nth-child(2){
                  font-size: 23px;
                  font-weight: 500;
                  padding: 0px 20px;
                  border: none;
                  margin-bottom: 8px;
                }

                &:nth-child(3){
                  font-size: 13px;
                  padding: 0px 20px;
                  border: none;
                }

                &:nth-child(4){
                  font-size: 13px;
                  padding: 0px 20px 20px 20px;
                }
              }
            }
          }
        }
      }
    }
  }
}

[v-cloak] {
  display: none;
}
</style>