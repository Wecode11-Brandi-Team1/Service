<template>
  <div class="info-wrap">
    <div class="join-container">
      <input type="text" placeholder="아이디 입력" v-model="account" />
      <input class="bottom-input" type="text" placeholder="이메일 입력" v-model="email" v-if="!$store.state.isGoogle"/>
      <span>이메일 정보는 비밀번호 찾기시 사용됩니다.</span>
      <input type="password" placeholder="비밀번호 입력" v-model="password" v-if="!$store.state.isGoogle"/>
      <input class="bottom-input" type="password" placeholder="비밀번호 확인" v-model="passwordCheck" v-if="!$store.state.isGoogle"/>
      <div class="line"></div>
      <h1>추천인 코드</h1>
      <input type="text" placeholder="추천인 코드 (선택사항)" v-model="recommen"/>
      <span>추천인 코드를 입력하시면 1000포인트가 지급됩니다.</span>
      <div class="line"></div>
      <div class="button-wrap">
        <button v-on:click="infoSubmit">다음</button>
      </div>
    </div>
  </div>
</template>

<script>
import { axios } from '../../../plugins/axios';

export default {
  data:() => ({
    pageName:'info',
    account:'',
    email:'',
    password:'',
    passwordCheck:'',
    recommen:''
  }),
  mounted:function(){
    this.$store.state.signUpTabName = this.pageName;
  },
  methods:{
    
    infoSubmit: function(){
      if(!this.account){
        alert('아이디를 입력해주세요.');
      }else if(this.account.length < 4 && !this.account.length > 20){
        alert('4~20자의 영문 소문자, 숫자만 입력 가능합니다.');
      }else if(!this.email && !this.$store.state.isGoogle){
        alert('이메일를 입력하세요.');
      }else if(!this.email.includes('@') && !this.$store.state.isGoogle){
        alert('이메일이 유효하지 않습니다.');
      }else if(!this.password && !this.$store.state.isGoogle){
        alert('비밀번호를 입력하세요.')
      }else if(this.password.length < 8 && !this.$store.state.isGoogle){
        alert('비밀번호는 최소 8자 이상 입력해 주세요.')
      }else if(!this.passwordCheck && !this.$store.state.isGoogle){
        alert('비밀번호를 확인해주세요.')
      }else if(this.password !== this.passwordCheck && !this.$store.state.isGoogle){
        alert('비밀번호가 일치하지 않습니다.')
      }else if(this.password.length >= 20 && !this.$store.state.isGoogle){
        alert('비밀번호는 8~20자 영문 대소문자, 숫자, 특수문자를 사용해 주세요.')
      }else if(!this.$store.state.isGoogle){
        axios.post('http://10.251.1.174:5000/sign-up', {
          account: this.account,
          email: this.email,
          password: this.password,
        })
        .then((response) => {
          if (response.data.message === "SUCCESS"){
            this.$router.push({path: '/signup/success'});
          }else{
            alert('입력된 정보값을 확인하세요.');
          }
        })
        .catch((error) => {
          if(error.response && error.response.data.message){
            let errorText = error.response.data.message
            alert(errorText);
          }
        });
      }else if(this.$store.state.isGoogle){
        const headers = {
          headers: { 'Authorization': this.$store.state.googleToken}
        }
        axios.post('http://10.251.1.174:5000/social-signup', {
          account: this.account
        }, headers)
        .then((response) => {
          if (response.data.message === "SUCCESS") {
            this.$store.state.isGoogle = true;
            this.$router.push({path: '/signup/success'});
          }else{
            alert('입력된 정보값을 확인하세요.');
          }
        })
        .catch((error) => {
          console.log(error);
        })
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.info-wrap{
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
    margin: 10px auto;
    padding: 16px;
    padding-top: 40px;

    input{
      width: 100%;
      height: 40px;
      font-size: 14px;
      border: 1px solid #e1e1e1;
      border-radius: 5px 5px 0px 0px;
      margin: 0px;
      padding: 10px;
    }

    .bottom-input{
      border-top: none;
    }

    span{
      font-size: 13px;
      color: #4c4c4c;
      padding: 10px 0px;
    }

    .line{
      width: 100%;
      height: 1px;
      background-color: #dfdfdf;
      margin-top: 20px;
    }

    h1{
      font-size: 15.5px;
      font-weight: bold;
      margin: 5px 0;
      padding: 20px 0px 7px 0px;
    }

    .button-wrap{
      display: flex;
      justify-content: center;
      margin: 30px auto 2px auto;

      button{
        width: 200px;
        height: 60px;
        font-size: 19px;
        line-height: 63px;
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
  }

  .button-wrap{
    button{
      width: 278px !important;
      height: 50px !important;
      font-size: 16px !important;
      line-height: 46px !important;
    }
  }
}
</style>