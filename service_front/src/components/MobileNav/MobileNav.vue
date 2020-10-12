<template>
  <header>
    <div class="nav">
      <div class="back-icon" v-if="isBackIcon" @click="isBack">
        <img alt="이전 페이지로 이동" src="https://web-staging.brandi.co.kr/static/20.08.01/images/img_sub_header_back.jpg" />
      </div>
      <div class="nav-title">
        <img src="https://image.brandi.me/user/empty_profile.jpg" v-if="isTitleImg"/>
        <span>{{ this.$store.state.mobilePageName }}</span>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  data:() => ({
    isBackIcon: true,
    isTitleImg: true,
    mobilePageName:'dlskdld'
  }),
  computed:{
    isMypages(){
      if(this.$store.state.isMypage){
        this.isBackICon = false;
        this.isTitleImg = true;
      }else{
        this.isBackICon = true;
        this.isTitleImg = false;
      }
    }
  },
  mounted: function () {
    this.$store.state.isMypage = true;
  },
  methods:{
    isBack(){
      this.$router.go(-1);
    }
  }
}
</script>

<style lang="scss" scoped>
header{
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 99;
  letter-spacing: -0.05em;

  .nav{
    position: relative;
    height: 56px;
    border-bottom: 1px solid #e1e1e1;
    background: #ffff;

    .back-icon{
      width: 48px;
      height: 48px;
      position: absolute;
      top: 4px;
      left: 4px;

      img{
        width: 100%;
      }
    }

    .nav-title{
      width: 70%;
      height: 56px;
      text-align: center;
      line-height: 56px;
      margin: 0 auto;

      img{
        width: 35px;
        height: 35px;
        border-radius: 50%;
        vertical-align: middle;
        margin-right: 6px;
      }

      span{
        height: 56px;
        display: inline-block;
        font-size: 16.5px;
        font-weight: bold;
        letter-spacing: -0.1em;
      }
    }
  }
}
</style>