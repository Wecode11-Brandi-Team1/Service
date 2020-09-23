<template>
  <div class="main">
    <header id="rollingbanner-container">
      <a href="?">
        <img alt="rolling banner" v-bind:src="datas.rolling_banner_image" />
      </a>
      <div id="slide-button">
        <div class="spot" href="?"></div>
      </div>
    </header>
    <main id="main-list-container">
      <div id="main-page-title">
        <span>당신을 위한 추천</span>
      </div>
      <div class="main-list">
        <a
          v-bind:href="`/productdetail/` + list.id"
          v-bind:key="list.id"
          v-for="list in datas.list.slice(0, 20)"
        >
          <list-card v-bind="list" />
        </a>
      </div>
      <div class="main-subbanner">
        <a href="?">
          <img alt="Banner photo" v-bind:src="datas.main_subbanner_image[0]" />
        </a>
      </div>
      <div class="main-list">
        <a
          v-bind:href="`/productdetail/` + list.id"
          v-bind:key="list.id"
          v-for="list in datas.list.slice(20, 40)"
        >
          <list-card v-bind="list" />
        </a>
      </div>
      <div class="main-subbanner">
        <a href="?">
          <img alt="Banner photo" v-bind:src="datas.main_subbanner_image[1]" />
        </a>
      </div>
      <div id="mainlist-bottom">
        <a
          v-bind:href="`/productdetail/` + list.id"
          v-bind:key="list.id"
          v-for="list in paginatedData"
        >
          <list-card v-bind="list" />
        </a>
      </div>
      <div
        v-bind:class="{
          'button-container': datas.list.length !== paginatedData.length + 40,
          none: datas.list.length === paginatedData.length + 40,
        }"
      >
        <button class="more" v-on:click="more_loading">더보기</button>
      </div>
    </main>
  </div>
</template>

<script>
import listCard from "./MainComponents/ListCard.vue";
import axios from "axios";

export default {
  name: "main",
  components: { listCard },
  data: () => ({
    offset: 40,
    limit: 20,
    loading_list: 1,
    datas: {
      list: [
        {
          id: "",
          src: "",
          seller_name: "",
          product_name: "",
          discount: 0,
          origin_price: 0,
          list_count: 0,
          one_day_delivery: false,
        },
      ],
      rolling_banner_image: [],
      rolling_banner_url: [],
      main_subbanner_image: [],
      main_subbanner_url: [],
    },
  }),
  computed: {
    paginatedData() {
      const start = this.offset,
        end = start + this.limit * this.loading_list;
      return this.datas.list.slice(start, end);
    },
  },
  methods: {
    more_loading() {
      this.loading_list += 1;
    },
  },
  created: function () {
    axios
      .get("public/data/mockData/mainProductJson.json")
      .then((res) => (this.datas = res.data));
  },
};
</script>

<style lang="scss">
.main {
  display: flex;
  flex-direction: column;
  width: 100vw;
  box-sizing: border-box;

  .none {
    display: none;
  }

  a {
    color: inherit;

    &:hover {
      color: inherit;
      text-decoration: none;
    }
  }

  #rollingbanner-container {
    position: relative;
    margin-bottom: 30px;
    padding-bottom: 24px;

    img {
      max-width: 100%;
      background-color: black;
    }

    #slide-button {
      position: absolute;
      display: flex;
      justify-content: center;
      align-items: flex-end;
      bottom: 0;
      width: 100%;
      height: 19px;

      .spot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: black;
        cursor: pointer;
      }
    }
  }

  #main-list-container {
    display: flex;
    flex-direction: column;
    width: 1300px;
    padding: 0 30px;
    margin: auto;

    .main-list,
    #mainlist-bottom {
      display: flex;
      flex-wrap: wrap;
    }
  }

  #main-page-title {
    display: flex;
    justify-content: center;
    margin-bottom: 30px;
    padding-top: 40px;
    span {
      font-size: 26px;
      font-weight: 700;
    }
  }

  .main-subbanner {
    height: 313.3px;
    margin-top: 50px;
    margin-bottom: 80px;

    img {
      width: 100%;
      height: 313.3;
      padding: 0 6.1875px;
    }
  }

  .button-container {
    display: flex;
    justify-content: center;
    height: 82px;
    padding: 20px 0;

    .more {
      width: 250px;
      border: 1px solid black;
      font-size: 14px;

      &:focus {
        border: inherit;
      }
    }
  }
}
</style>
