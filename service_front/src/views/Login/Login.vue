<template>
  <div class="login-wrap">
    <div class="login-title-box">
      <h1>오늘 사면 내일 도착!</h1>
      <h2>무료배송으로 내일 받는 브랜디 LOGIN</h2>
    </div>
    <div class="login-container">
      <input type="text" placeholder="아이디 입력" v-model="account"/>
      <input type="password" placeholder="비밀번호 입력" v-model="password"/>
      <div class="btn-box">
        <button class="login-btn" v-on:click="loginSubmit">로그인</button>
        <button class="join-btn">회원가입</button>
      </div>
      <h3>간편로그인 / 가입</h3>
      <g-signin-button
        :params="googleSignInParams"
        @success="onSignInSuccess">
        <img class="google-img" src="https://web-staging.brandi.co.kr/static/2020.7.3/images/google-logo.png" />
        <span>Google</span> 계정으로 계속하기
      </g-signin-button>
    </div>
  </div>
</template>

<script>
import { axios } from '../../plugins/axios'

export default {
  data:()=>({
    account:'',
    password:'',
    googleSignInParams: {
      client_id: '766168086002-nlrgc0u79p1mjd7etd18trul3lu961nj.apps.googleusercontent.com'
    }
  }),
  methods:{
    loginSubmit(){
      if(!this.account){
        alert('아이디를 입력하세요');
      }else if(this.account && !this.password){
        alert('비밀번호를 입력하세요')
      }else{
        axios.post('/user', {
          account: this.account,
          password: this.password
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          alert('아이디와 비밀번호를 다시 확인해주세요.');
        });
      }
    },
    
    onSignInSuccess (googleUser) {
      const accessToken = googleUser.getAuthResponse(true).access_token;
      console.log(accessToken);

      axios.post('http://10.251.1.125:5000/api/user/google-login', {
        token_type :'Bearer',
        access_token: accessToken
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.login-wrap{
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  text-align: center;

  .login-title-box{
    padding: 40px 0px 20px 0px;

    h1{
      font-size: 34px;
      font-weight: bold;
      font-family: "Spoqa Han Sans";
      color: #FF204B;
      margin: 0;
      margin-top: 20px;
    }

    h2{
      font-size: 32px;
      font-weight: 100;
      font-family: "Spoqa Han Sans";
      margin: 0;
    }
  }

  .login-container{
    width: 100%;
    max-width: 600px;
    margin: 10px auto;
    padding: 16px;

    input{
      width: 100%;
      height: 50px;
      font-size: 14px;
      border: 1px solid #e1e1e1;
      border-radius: 4px;
      margin: 4px 0;
      padding: 10px;

      &:focus{
        outline: none;
      }
    }

    .btn-box{
      padding-bottom: 25px;
      border-bottom: 1px solid #ccc;
      
      button{
        width: 100%;
        height: 50px;
        font-size: 14px;
        font-family: "Spoqa Han Sans";
        line-height: 50px;
        border-radius: 4px;
        padding: 0;
        cursor: pointer;

        &:focus{
          outline: none;
        }
      }

      .login-btn{
        color: #fff;
        border: 1px solid #000;
        background: #000;
        margin: 10px 0px 2px 0px;
      }
  
      .join-btn{
        color: #000;
        border: 1px solid #000;
        background: #fff;
        margin: 10px 0px 2px 0px;
      }
    }

    h3{
      font-size: 15px;
      font-weight: bold;
      font-family: "Spoqa Han Sans";
      color: #1e1e1e;
      padding-top: 20px;
    }

    .g-signin-button {
      width: 100%;
      height: 50px;
      font-size: 14px;
      font-family: "Spoqa Han Sans";
      line-height: 50px;
      color: rgba(0, 0, 0, 0.54);
      border: 1px solid #bdbdbd;
      border-radius: 4px;
      box-shadow: none;
      padding: 0;
      margin-top: 25px;
      cursor: pointer;

      .google-img{
        width: 28px;
        vertical-align: -8px;
        margin-right: 10px;
      }

      span{
        font-weight: bold;
      }

      &:hover{
        color:#fff;
        background: #000;
      }
    }
  }
}
</style>