<template>
  <div class="success-wrap">
    <div class="page-title">
      <h1>회원가입</h1>
    </div>
    <signUpTab v-bind:propsdata="pageName"></signUpTab>
    <div class="join-container">
      <img src="https://image.brandi.me/common/200115_pc_join_finish_3x.png" />
      <h3>브랜디 회원 가입을 축하드립니다!</h3>
      <h4>바로 사용 가능한 1만원 혜택이 지급되었습니다!</h4>
      <h5>지급받으신 혜택은 쿠폰함에서 확인 가능합니다</h5>
      <div class="line"></div>
      <div class="button-wrap">
        <button>쿠폰 확인하기</button>
        <router-link to="/main"><button>바로 쇼핑하기</button></router-link>
      </div>
    </div>
  </div>
</template>

<script>
import signUpTab from '../../components/signUpComponent/signUpTab.vue'; 

export default {
  data:() => ({
    pageName:'complete'
  }),
  props:['propsdata'],
    components: {
    signUpTab
  }
}
</script>

<style lang="scss" scoped>
.success-wrap{
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;

  .page-title{
    margin-bottom: 30px;
    padding: 0 20px;

    h1{
      font-size: 28px;
      text-align: center;
      margin-bottom: 15px;
    }
  }

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
</style>