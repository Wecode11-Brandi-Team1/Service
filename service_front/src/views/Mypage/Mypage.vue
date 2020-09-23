<template>
  <div class="mypage-wrap">
    <div class="page-title" v-if="$store.state.myPageShow">
      <h1>마이페이지</h1>
    </div>
      <IconBox v-if="$store.state.myPageShow"></IconBox>
      <router-view></router-view>
  </div>
</template>

<script>
import IconBox from '../../components/MypageComponent/IconBox.vue';

export default {
  data:() => ({
    pageName:'orderList',
    productData:[]
  }),
  components:{
    IconBox,
  },
}
</script>

<style lang="scss" scoped>
.mypage-wrap{
  .page-title{
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 40px 0px 20px 0px;
    margin-bottom: 30px;

    h1{
      font-size: 28px;
      text-align: center;
      margin-bottom: 15px;
    }
  }
}

@media screen and (min-width: 769px){
  .mypage-wrap{
    max-width: 1300px;
    margin: 0 auto;
  }
}


@media screen and (max-width: 400px){
  .mypage-wrap{
    .page-title{
      display: none;
    }
  }
}
</style>