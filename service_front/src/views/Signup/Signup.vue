<template>
<div>
  <div class="signup-wrap">
    <div class="page-title">
      <h1>회원가입</h1>
    </div>
    <signUpTab></signUpTab>
    <router-view></router-view>
  </div>
</div>
</template>

<script>
import signUpTab from '../../components/signUpComponent/signUpTab.vue'; 

export default {
  components: {
    signUpTab
  },
}
</script>

<style lang="scss" scoped>
.signup-wrap{
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  margin: 50px 0;

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
  .page-title{
    display: none;
  }

  .join-container {
    max-width: 400px;
    margin: 0 auto;
  }
}
</style>