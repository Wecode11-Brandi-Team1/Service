<template>
  <div class="category-bg" @mouseleave="resetHover">
    <div
      class="category-wrap"
      v-if="this.$store.state.menutab.currentHover === 3 && isMobile === false"
    >
      <ul>
        <li v-for="item in shopData().item" :key="Object.keys(item)[0]">
          <a
            class="header"
            v-for="(list, index) in item"
            :key="index"
            @click="pageStatus"
          >
            {{ Object.keys(item)[0] }}
            <a class="list" v-for="(content, index) in list" :key="index">
              {{ content }}
            </a>
          </a>
        </li>
      </ul>
    </div>
    <div
      class="category-wrap"
      v-if="this.$store.state.menutab.currentHover === 4"
    >
      <ul>
        <li v-for="item in brandData().item" :key="Object.keys(item)[0]">
          <a class="header" v-for="(list, index) in item" :key="index">
            {{ Object.keys(item)[0] }}
            <a class="list" v-for="(content, index) in list" :key="index">
              {{ content }}
            </a>
          </a>
        </li>
      </ul>
    </div>
    <div
      class="category-wrap"
      v-if="this.$store.state.menutab.currentHover === 5"
    >
      <ul>
        <li v-for="item in beautyData().item" :key="Object.keys(item)[0]">
          <a class="header" v-for="(list, index) in item" :key="index">
            {{ Object.keys(item)[0] }}
            <a class="list" v-for="(content, index) in list" :key="index">
              {{ content }}
            </a>
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isMobile: false,
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
  methods: {
    pageStatus() {
      let mql = window.matchMedia("screen and (max-width: 400px)");
      if (mql.matches) {
          this.isMobile = true
      } else {
          this.isMobile = false
      }
    },
    resetHover() {
      this.$store.state.menutab.currentHover = null;
    },
    shopData() {
      return JSON.parse(localStorage.getItem("categoryShop"));
    },
    brandData() {
      return JSON.parse(localStorage.getItem("categoryBrand"));
    },
    beautyData() {
      return JSON.parse(localStorage.getItem("categoryBeauty"));
    },
    goToProduct() {
      this.$router.push(`/products/${1}`);
      // return this.$router.push({ name: "ProductList", query: { q: 123 } });
    },
  },
};
</script>

<style lang="scss">
.category-bg {
  position: absolute;
  top: 182;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.96);
  box-shadow: 0 3px 5px 2px rgba(0, 0, 0, 0.3);
  z-index: 9999;
  .category-wrap {
    display: flex;
    justify-content: center;
    ul {
      display: flex;
      flex-wrap: wrap;
      width: 1300px;
      padding: 10px;
      li {
        width: 210px;
        padding: 0 40px;
        .header {
          font-size: 17px;
          font-weight: bold;
          line-height: 2.5;
          color: black;
          cursor: pointer;
        }
        .list {
          display: flex;
          flex-direction: column;
          width: 120px;
          font-size: 16px;
          font-weight: normal;
          line-height: 2;
          color: #737373;
          &:hover {
            color: black;
          }
        }
      }
    }
    .cateLine1 {
      position: absolute;
      width: 1px;
      height: 100%;
      background-color: #e1e1e1;
    }
    .cateLine6 {
      position: absolute;
      left: 98%;
      width: 1px;
      height: 100%;
      background-color: #e1e1e1;
    }
  }
}

@media screen and (max-width: 400px){
  .category-bg{
    display: none;
  }
}
</style>
