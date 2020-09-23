<template>
  <div class="signup-wrap">
    <div class="join-container">
      <img src="https://web-staging.brandi.co.kr/static/3.50.7/images/h_icon_join_1_confirm_web(245)@3x.png" />
      <h3>브랜디 본인 인증</h3>
      <ul>
        <li>14세미만 회원은 가입이 불가합니다.</li>
        <li>법인폰 사용자는 휴대폰 인증이 불가합니다.</li>
      </ul>
      <div class="line"></div>
      <button @click="linkBtn">휴대폰 인증</button>
    </div>
  </div>
</template>

<script>
export default {
  data:() => ({
    pageName:'signUp',
  }),
  methods:{
    linkBtn(){
      this.$router.push({path: '/signup/agree'});
    }
  },
  mounted:function(){
    this.$store.state.signUpTabName = this.pageName;
  }
}
</script>

<style lang="scss" scoped>
.signup-wrap{
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;

  .join-container{
    width: 100%;
    max-width: 600px;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 10px auto;
    padding: 16px;
    padding-top: 40px;

    img{
      width: 201px;
      margin: 35px 0 25px 0;
    }

    h3{
      font-size: 21px;
      font-family: "Spoqa Han Sans";
      color:#1e1e1e;
      margin:21px 0px 14px 0px;
    }

    ul{
      text-align: left;

      li{
        list-style: disc;
      }
    }

    .line{
      width: 100%;
      height: 1px;
      background-color: #dfdfdf;
      margin: 10px 0px 20px 0px;
    }

    button{
      width: 200px;
      height: 60px;
      font-size: 19px;
      line-height: 65px;
      color: #fff;
      background: #000;
      border: 1px solid #000;
      border-radius: 4px;

      &:focus{
        outline: none;
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
    padding-top: 10px;
    margin: 0 auto;

    img{
      width: 180px;
    }

    h3{
      font-size: 18px;
      font-weight: bold;
    }

    ul{
      font-size: 13px;
      padding-left: 30px;
    }

    button{
      width: 278px !important;
      height: 50px !important;
      font-size: 16px !important;
      line-height: 46px !important;
    }
  }
}
</style>