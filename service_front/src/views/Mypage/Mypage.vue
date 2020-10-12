<template>
  <div class="mypage-wrap">
    <div class="moblieNav">
      <MobileNav></MobileNav>
    </div>
    <div class="page-title" v-if="$store.state.myPageShow">
      <h1>마이페이지</h1>
    </div>
      <IconBox v-if="$store.state.myPageShow"></IconBox>
      <router-view></router-view>
      <div class="tabBarNav">
        <TabBarNav></TabBarNav>
    </div>
  </div>
</template>

<script>
import IconBox from '../../components/MypageComponent/IconBox.vue';
import MobileNav from '../../components/MobileNav/MobileNav.vue';
import TabBarNav from '../../components/TabBarNav/TabBarNav.vue';

export default {
  data:() => ({
    pageName:'mypage',
    productData:[]
  }),
  components:{
    IconBox,
    MobileNav,
    TabBarNav
  },
  mounted: function () {
    this.$store.state.mobilePageName = this.pageName;
    this.$store.state.isTabBar = this.pageName;
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

    .moblieNav{
      display: none;
    }

    .tabBarNav{
      display: none;
    }
  }
}


@media screen and (max-width: 400px){
  .mypage-wrap{
    .page-title{
      display: none;
    }

    .moblieNav{
      display: block;
    }

    .tabBarNav{
      display: block;
    }
  }
}
</style>