<template>
  <div>
    <div class="nav-wrap">
      <div class="nav-left">
        <img
          @click="$router.push('main')"
          alt="logo"
          src="https://web-staging.brandi.co.kr/static/2020.7.3/images/logo@3x.png"
        />
      </div>
      <div class="nav-center">
        <label
          ><button @click="pushResult" type="button" /><input
            v-model="search"
            type="text"
        /></label>
      </div>
      <div class="nav-right">
        <ul>
          <li>찜</li>
          <li class="border">|</li>
          <li>장바구니</li>
          <li class="border">|</li>
          <li @click="$router.push('mypage')">마이페이지</li>
          <li class="border">|</li>
          <li @click="$router.push('login')">로그인</li>
          <li class="border">|</li>
          <li>입점문의</li>
        </ul>
      </div>
    </div>
    <div class="nav-menu">
      <tab-item
        v-for="item in list"
        v-bind="item"
        :key="item.id"
        v-model="currentId"
      />
    </div>
    <tab-item-drop
      :currentId="currentId"
      v-if="currentId === 3 || currentId === 4 || currentId === 5"
    />
  </div>
</template>

<script>
import axios from "axios";
import TabItemDrop from "./TabItemDrop.vue";
import TabItem from "./TabItem.vue";
export default {
  components: { TabItem, TabItemDrop },
  data() {
    return {
      search: "",
      currentId: 0,
      list: [
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
  computed: {},
  methods: {
    pushResult() {
      if (this.search.length > 0) {
        // this.$router.push(`search/?q=${this.search}&r"20`);
      } else {
        alert("검색어를 입력해주세요.");
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
    label {
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
        width: 22px;
        height: 22px;
        margin: auto 10;
        background-image: url("https://web-staging.brandi.co.kr/static/2020.7.3/images/a-action-bar-icon-search-nor.png");
        background-size: 22px;
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
</style>
