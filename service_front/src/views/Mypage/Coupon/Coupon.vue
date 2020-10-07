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
        <div class="coupon">
          <h2>발급받은 쿠폰 <strong>1</strong><span><span class="coupon-Star">* </span>유효기간이 30일 지난 쿠폰은 목록에서 삭제됩니다.</span></h2>
          <div class="coupon-list">
            <dl class="list-header">
              <dt>쿠폰명</dt>
              <dt>사용혜택</dt>
              <dt>사용조건</dt>
              <dt>유효기간</dt>
            </dl>
            <dl>
              <dd>회원가입 축하쿠폰</dd>
              <dd>2,000원 할인</dd>
              <dd>[쇼핑몰 쿠폰] 15,000원 이상 구매시</dd>
              <dd>2020.01.16 ~ 2020.10.20</dd>
            </dl>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data:() => ({
    pageName:'coupon'
  }),
  mounted: function () {
    this.$store.state.myPageTabName = this.pageName;
    this.$store.state.myPageShow = true;
  }
}
</script>

<style lang="scss" scoped>
.mypage-wrap{
  color: #1e1e1e;

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

    .page-box{
      .coupon-box{
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
        }
      }
    }
  }
}
</style>