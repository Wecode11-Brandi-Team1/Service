<template scroll=no>
  <div>
    <div class="nav-wrap" @mouseenter="resetHover">
      <div class="nav-left">
        <img
          @click="$router.push('/')"
          alt="logo"
          src="https://web-staging.brandi.co.kr/static/2020.7.3/images/logo@3x.png"
        />
      </div>
      <div class="nav-center">
        <div class="label">
          <button type="button" @click="move_search" /><input
            type="text"
            v-model="search"
            v-on:keyup.enter="move_search"
          />
        </div>
      </div>
      <div class="nav-right">
        <ul>
          <li>찜</li>
          <li class="border">|</li>
          <li @click="$router.push('order')">장바구니</li>
          <li class="border">|</li>
          <li @click="$router.push('mypage')">마이페이지</li>
          <li class="border">|</li>
          <li v-if="!this.$cookies.get('accesstoken')" @click="$router.push('login')">
            로그인
          </li>
          <li v-else @click="logout">로그아웃</li>
          <li class="border">|</li>
          <li>입점문의</li>
        </ul>
        <img class="cart-mobile" src="http://web-staging.brandi.co.kr/static/20.08.01/images/img_top_cart.png" />
      </div>
    </div>
    <div class="nav-menu">
      <tab-item v-for="item in menu" v-bind="item" :key="item.id" />
    </div>
    <tab-item-drop
      v-if="
        this.$store.state.menutab.currentHover === 3 ||
        this.$store.state.menutab.currentHover === 4 ||
        this.$store.state.menutab.currentHover === 5
      "
    />
  <!-- MobileNav  -->
  <div class="nav-wrap-mobile">
    <div class="gnbTop">
        <h1>
          <router-link to="/">
            <img ait="BRANDI" src="https://web-staging.brandi.co.kr/static/20.08.01/images/logo@3x.png" />
          </router-link>
        </h1>
        <div class="search-box">
          <form>
            <button>검색</button>
            <input type="text" />
          </form>
        </div>
        <div class="cart-icon">
          <img src="https://web-staging.brandi.co.kr/static/20.08.01/images/img_top_cart.png" />
        </div>
      </div>
      <div class="nav-menu-mini">
        <div class="nav-container">
          <ul>
            <tab-item v-for="item in menu" v-bind="item" :key="item.id" />
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {config} from "../../api/apiConfig"
import TabItemDrop from "./TabItemDrop.vue";
import TabItem from "./TabItem.vue";
export default {
  components: { TabItem, TabItemDrop },
  data() {
    return {
      search: "",
      menu: [
        { id: 0, label: "홈" },
        { id: 1, label: "랭킹" },
        { id: 2, label: "하루배송" },
        { id: 3, label: "쇼핑몰 · 마켓" },
        { id: 4, label: "브랜드" },
        { id: 5, label: "뷰티" },
        { id: 6, label: "특가" },
        { id: 7, label: "기획전" },
        { id: 8, label: "스토어" },
      ],
    };
  },
  created() {
    if (this.$router.history.current.name === "Main") {
      this.$store.state.menutab.activeTab = 0;
    } else if (this.$router.history.current.name === "Event") {
      this.$store.state.menutab.activeTab = 7;
    } else {
      this.$store.state.menutab.activeTab = null;
    }
    axios
      .get(`${config.API}category?q=1`)
      .then((res) => (this.$store.state.categoryShop = res.data.쇼핑몰));
    axios
      .get(`${config.API}category?q=4`)
      .then(
        (res) => (this.$store.state.categoryBrand = res.data.디자이너브랜드)
      );
    axios
      .get(`${config.API}category?q=7`)
      .then((res) => (this.$store.state.categoryBeauty = res.data.뷰티));
  },

  beforeUpdate() {
    const categoryShop = { item: this.$store.state.categoryShop };
    const categoryBrand = { item: this.$store.state.categoryBrand };
    const categoryBeauty = { item: this.$store.state.categoryBeauty };
    localStorage.setItem("categoryShop", JSON.stringify(categoryShop));
    localStorage.setItem("categoryBrand", JSON.stringify(categoryBrand));
    localStorage.setItem("categoryBeauty", JSON.stringify(categoryBeauty));
  },
  methods: {
    logout() {
      this.$cookies.remove('accesstoken');
      alert("로그아웃 하였습니다");
      this.$router.push({ path: "/" });
    },
    resetHover() {
      this.$store.state.menutab.currentHover = null;
    },
    move_search() {
      if (this.search.length >= 1) {
        this.$router.push({ name: "Search", query: { q: this.search } });
      } else {
        alert("검색어를 입력해주세요");
      }
    },
  },
};
</script>

<style lang="scss">
.nav-wrap {
  position: relative;
  top: 0;
  display: flex;
  justify-content: space-between;
  max-width: 1300px;
  height: 120px;
  margin: auto;
  padding: 20px 40px;
  color: black;
  background-color: white;
  z-index: 9999;
  .nav-left {
    margin: auto 0;
    img {
      width: 150px;
      cursor: pointer;
    }
  }
  .nav-center {
    margin: auto 0;
    .label {
      display: flex;
      justify-content: flex-start;
      width: 504px;
      height: 40px;
      margin: auto 0;
      padding: 5px;
      border-radius: 20px;
      color: #1e1e1e;
      background-color: #eeeeee;
      button {
        width: 20px;
        height: 20px;
        margin: auto 10px;
        background-image: url("https://web-staging.brandi.co.kr/static/2020.7.3/images/a-action-bar-icon-search-nor.png");
        background-size: 20px;
        outline: none;
      }
      input {
        width: 100%;
        height: 25px;
        margin: auto 0;
        outline: none;
      }
    }
  }
  .nav-right {
    margin: auto 0;
    ul {
      display: flex;
      margin: 0;
      font-size: 15px;
      li {
        cursor: pointer;
      }
      .border {
        margin: 0 5px;
        cursor: default;
      }
    }

    .cart-mobile{
      display: none;
    }
  }
}
.nav-menu {
  display: flex;
  justify-content: center;
  max-width: 100%;
  height: 62px;
  margin: auto 0;
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
  text-align: center;
  font-weight: 900;
}

.nav-wrap-mobile{
  display: none;
}

@media screen and (max-width: 400px){
  .nav-wrap {
    display: none;
  }

  .nav-menu{
    display: none;
  }

  .nav-wrap-mobile{
    width: 100%;
    height: 57px;
    position: relative;
    display: block;
    z-index: 21;

      .gnbTop{
        padding: 13px 10px;
        display: block;
        height: 57px;
        border-bottom: 1px solid #d2d2d2;

        h1{
          width: 25%;
          height: 30px;
          text-align: left;
          float: left;
          margin: 0 3px 0 0;
          padding: 0;

          a{
            width: 100%;
            max-width: 80px;
            height: 30px;
            position: relative;
            display: block;
            line-height: 30px;

            img{
              width: 100%;
              vertical-align: top;
              margin-top: 8px;
            }
          }
        }
      }

      .search-box{
        width: 64%;
        height: 30px;
        float: left;
        border-radius: 15px;
        background-color: #eee;
        background-image: url('https://web-staging.brandi.co.kr/static/20.08.01/images/ico_search_m.gif');
        background-repeat: no-repeat;
        background-position: 10px 7px;
        background-size: 15px;
        padding: 0;
        padding-left: 34px;

        form{
          width: 100%;
          height: 100%;

          button{
            width: 0;
            height: 0;
            border: 0px;
            overflow: hidden;
            text-indent: -999px;
          }

          input{
            width: calc(100% - 58px);
            height: 30px;
            font-size: 15px;
            line-height: 20px;
            background: transparent;
            border: 0px;
            padding: 5px;
          }
          
        }
      }

      .cart-icon{
        width: 30px;
        height: 30px;
        display: block;
        position: absolute;
        top: 50%;
        right: 12px;
        text-align: center;
        transform: translate(0, -50%);

        img{
          width: 30px;
          position: absolute;
          top: 37%;
          left: 50%;
          transform: translate(-50%, -50%);
        }
      }

      .nav-menu-mini{
        width: 100%;
        height: 51px;
        display: block;
        background: #fff;
        overflow: hidden;
        border-bottom: 1px solid #ddd;

        .nav-container{
          width: 360px;
          overflow-x:scroll;
          white-space: nowrap;
          
          ul{
            padding: 13px 15px;

            span{
              font-size: 13px;
              font-weight: bold;
              padding: 0px;
              margin-right: 28px;
            }
          }
        }
      }
    }
  }
</style>
