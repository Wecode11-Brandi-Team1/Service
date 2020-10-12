<template>
  <div class="success-wrap">
    <div class="join-container">
      <img src="https://image.brandi.me/common/200115_pc_join_finish_3x.png" />
      <h3>브랜디 회원 가입을 축하드립니다!</h3>
      <h4>바로 사용 가능한 1만원 혜택이 지급되었습니다!</h4>
      <h5>지급받으신 혜택은 쿠폰함에서 확인 가능합니다</h5>
      <div class="line"></div>
      <div class="button-wrap">
        <router-link to="/mypage/coupon"><button>쿠폰 확인하기</button></router-link>
        <router-link to="/"><button>바로 쇼핑하기</button></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data:() => ({
    pageName:'complete'
  }),
  mounted(){
    this.$store.state.signUpTabName = this.pageName;
    // history.pushState(null, null, location.href);
    // window.onpopstate = function(event) {
    //   history.go(1);
    //   alert('잘못된 접근입니다.');
    // };
  }
}
</script>

<style lang="scss" scoped>
.success-wrap{
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;

  .join-container{
    width: 100%;
    max-width: 600px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin: 10px auto;
    padding: 16px;
    padding-top: 40px;

    img{
      width: 260px;
      margin: 25px 0 25px 0;
    }

    h3{
      font-size: 21px;
      font-weight: bold;
      color: #1e1e1e;
      padding-top: 0;
      margin-top: 10px;
      margin-bottom: 16px;
    }

    h4{
      font-size: 18px;
      color: #1e1e1e;
      font-weight: bold;
      margin-top: 12px;
    }

    h5{
      font-size: 16px;
      color: #1e1e1e;
      font-weight: 400;
      margin-top: 5px;
    }

    .line{
      width: 100%;
      height: 1px;
      background-color: #dfdfdf;
      margin-top: 20px;
    }

    .button-wrap{
      width: 75%;
      display: flex;
      justify-content: space-evenly;
      margin: 30px auto 2px auto;

      button{
        width: 200px;
        height: 60px;
        font-size: 19px;
        font-weight: 400;
        line-height: 42px;
        color: #fff;
        display: inline-block;
        border: 1px solid #000;
        border-radius: 5px;
        background: #000;
        padding: 10px;
        margin: 15px auto 2px auto;

        &:focus{
          outline: none;
        }
      }
    }
  }
}

@media screen and (min-width: 769px){
  .join-container {
    max-width: 1300px;
    margin: 0 auto;
  }
}

@media screen and (max-width: 400px){
  .join-container {
    max-width: 400px;
    padding-top: 0px !important;
    margin: 0 auto;

    img{
      width: 240px;
      margin: 0;
      margin-bottom: 25px;
    }

    h4{
      font-size: 16px !important;
      margin-top: 0px !important;
    }

    .button-wrap{
      width: 100% !important;
      flex-direction: column;
      margin: 15px auto 2px auto !important;

      button{
        width: 278px !important;
        height: 50px !important;
        font-size: 16px !important;
        line-height: 46px !important;
        padding: 0 !important;
      }
    }

  }
}
</style>