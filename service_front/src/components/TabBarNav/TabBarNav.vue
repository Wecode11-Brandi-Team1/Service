<template>
  <div class="tab-bar-nav">
    <ul>
      <li>
        <router-link to="/">
        <div class="tab-home tab-box">
          <img :src="isActive[$store.state.isTabBar][0]" v-if="$store.state.isTabBar" />
          <span class="txt">홈</span>
        </div>
        </router-link>
      </li>
      <li>
        <div class="tab-todaydelivery tab-box">
          <img :src="isActive[$store.state.isTabBar][1]" v-if="$store.state.isTabBar" />
          <span class="txt">하루배송</span>
        </div>
      </li>
      <li>
        <div class="tab-cate tab-box">
          <img :src="isActive[$store.state.isTabBar][2]" v-if="$store.state.isTabBar" />
          <span class="txt">카테고리</span>
        </div>
      </li>
      <li>
        <div class="tab-favor tab-box">
          <img :src="isActive[$store.state.isTabBar][3]" v-if="$store.state.isTabBar" />
          <span class="txt">찜</span>
        </div>
      </li>
      <li>
        <router-link to="/mypage">
        <div class="tab-my tab-box">
          <img :src="isActive[$store.state.isTabBar][4]" v-if="$store.state.isTabBar" />
          <span class="txt">마이페이지</span>
        </div>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data:() => ({
    isActive:{
      home: ["https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-home-brandi-s@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-categoryline-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-categoryline-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-heart-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-my-n@2x.png"],
      todaydelivery: ["https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-home-brandi-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-haru-s@2x.png" ,"https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-categoryline-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-heart-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-my-n@2x.png"],
      category: ["https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-home-brandi-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-categoryline-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-categoryline-s@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-heart-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-my-n@2x.png"],
      favor: ["https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-home-brandi-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-categoryline-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-categoryline-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-heart-s@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-my-n@2x.png"],
      mypage: ["https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-home-brandi-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-categoryline-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-categoryline-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-heart-n@2x.png", "https://web-staging.brandi.co.kr/static/20.08.01/images/ic-gnb-aos-my-s@2x.png"],
    }
  })
}
</script>

<style lang="scss" scoped>
.tab-bar-nav{
  width: 100%;
  height: 57px;
  position: fixed;
  bottom: 0;
  left: 0;
  z-index: 999;
  border-top: 1px solid #bcbcbd;
  background: #fff;
  overflow: hidden;

  ul{
    display: flex;
    flex-direction: row;

    li{
      width: 20%;
      text-align: center;
      background: #fff;

      .tab-box{
        width: 100%;
        height: 100%;
        display: block;
        padding: 14px 3px;
        color: #acb3bd;
        font-size: 11px;
        line-height: 15px;

        .txt{
          width: 1px;
          height: 1px;
          overflow: hidden;
          position: absolute;
          top: -999em;
          left: -999em;
        }
      }

      .tab-home{
        img{
          width: 28px;
          height: 28px;
        }
      }

      .tab-todaydelivery{
        img{
          width: 28px;
          height: 28px;
        }
      }

      .tab-cate{
        img{
          width: 28px;
          height: 28px;
        }
      }

      .tab-favor{
        img{
          width: 28px;
          height: 28px;
        }
      }

      .tab-my{
        img{
          width: 28px;
          height: 28px;
        }
      }
    }
  }
}
</style>