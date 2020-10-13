<template>
  <div class="main">
    <header class="rollingbanner-container">
      <div class="rollingbanner-photo-container">
        <img alt="rolling banner" v-bind:src="rolling_banner_image" />
      </div>
      <div class="slide-button">
        <div class="spot" href="?"></div>
      </div>
    </header>
    <main class="main-list-container">
      <section>
        <div class="subtitle-container">
          <div class="subtitle">
            <p>
              사람들이 많이 찾는 상품
              <span>요즘 뭐가 그렇게 잘나가?</span>
            </p>
            <router-link v-bind:to="`categories/${`1`}/products`">
              더보기
              <img
                alt="arrow"
                src="https://web-staging.brandi.co.kr/static/2020.7.3/images/img_span_arrow.jpg"
              />
            </router-link>
          </div>
        </div>
        <div class="main-list">
          <router-link
            v-bind:to="`products/${list.product_id}`"
            v-bind:key="list.product_id"
            v-for="list in datas.most_sold_products"
          >
            <list-card v-bind="list" />
          </router-link>
        </div>
        <div class="colume-bar"></div>
      </section>
      <section>
        <div class="subtitle-container">
          <div class="subtitle">
            <p>
              오늘의 특가 리스트
              <span>놓치면 안될 단독 특가!</span>
            </p>
            <router-link v-bind:to="`categories/${`1`}/products`">
              더보기
              <img
                alt="arrow"
                src="https://web-staging.brandi.co.kr/static/2020.7.3/images/img_span_arrow.jpg"
              />
            </router-link>
          </div>
        </div>
        <div class="main-list">
          <router-link
            v-bind:to="`products/${list.product_id}`"
            v-bind:key="list.product_id"
            v-for="list in datas.discounted_products"
          >
            <list-card v-bind="list" />
          </router-link>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import axios from "axios";
import config from "../../api/apiConfig";
import listCard from "./MainComponents/ListCard.vue";

export default {
  name: "home-page",
  components: { listCard },
  data: () => ({
    rolling_banner_image: [
      "http://image.brandi.me/home/banner/bannerImage_159982_1593396258.jpg",
    ],
    rolling_banner_url: [],
    datas: {
      discounted_products: [],
      most_sold_products: [],
    },
  }),
  methods: {},
  created: function () {
    axios
      .get(`http://192.168.7.5:5000/`)
      .then((res) => (this.datas.coupon = res.data));
  },
};
</script>

<style lang="scss">
.main {
  display: flex;
  flex-direction: column;
  width: 100vw;
  box-sizing: border-box;
  margin-bottom: 20px;

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

  .rollingbanner-container {
    position: relative;
    margin-bottom: 30px;
    padding-bottom: 24px;

    .rollingbanner-photo-container {
      display: flex;
      justify-content: center;
    }

    img {
      max-width: 100%;
      background-color: black;
    }

    .slide-button {
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

  .main-list-container {
    display: flex;
    flex-direction: column;
    max-width: 1300px;
    width: 100%;
    padding: 0 30px;
    margin: auto;

    .main-list,
    #mainlist-bottom {
      display: flex;
      flex-wrap: wrap;
    }
  }

  .subtitle-container {
    padding-top: 40px;

    .subtitle {
      display: flex;
      justify-content: space-between;
      margin-top: 10px;
      margin-bottom: 15px;
      padding: 0 5px;

      img {
        position: relative;
        top: -3px;
        width: 20px;
      }
    }

    p {
      font-size: 26px;
      font-weight: 700;
      margin: 0;
    }

    span,
    a {
      font-size: 20px;
      margin-left: 10px;
      color: #4d4d4d;
    }

    a {
      position: relative;
      top: 10px;
    }
  }

  .colume-bar {
    border-bottom: 2px solid #cccccc;
    margin-top: 30px;
  }
}
</style>
