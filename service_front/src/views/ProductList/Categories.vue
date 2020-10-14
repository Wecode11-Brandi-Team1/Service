<template>
  <div class="categories">
    <header>
      <article>
        <ul>
          <li>{{top_category}}</li>
          <li>
            <span>></span>카테고리
          </li>
          <li v-if="$route.query.fc_id">
            <span>></span>
            {{ Object.keys(datas.nav_list[$route.query.fc_id])[0] }}
          </li>
          <li v-if="$route.query.sc_id">
            <span>></span>
            {{
            Object.values(datas.nav_list[$route.query.fc_id])[0][
            $route.query.sc_id
            ]
            }}
          </li>
        </ul>
      </article>
    </header>
    <main>
      <section class="sub-nav">
        <article>
          <h2>
            <span>상품 옵션</span>
          </h2>
          <div class="nav-box checkbox" v-on:click="sale_checker">
            <div
              v-bind:class="{
                checked: is_sale_list,
                unchecked: !is_sale_list,
              }"
            >✓</div>세일
          </div>
          <h2>
            <span>CATEGORIES</span>
          </h2>
          <div class="nav-box" id="전체" v-on:click="update_main_category">전체</div>
          <div v-for="list in datas.nav_list" v-bind:key="Object.keys(list)[0]">
            <div class="nav-box" v-bind:id="Object.keys(list)[0]" v-on:click="update_main_category">
              {{ Object.keys(list)[0] }}
              <img
                v-if="select_main_category === Object.keys(list)[0]"
                alt="arrow"
                src="https://web-staging.brandi.co.kr/static/2020.7.3/images/arr_up.png"
              />
              <img
                v-if="select_main_category !== Object.keys(list)[0]"
                alt="arrow"
                src="https://web-staging.brandi.co.kr/static/2020.7.3/images/arr_down.png"
              />
            </div>
            <ul v-if="select_main_category === Object.keys(list)[0]">
              <li
                v-bind:class="{ select: select_sub_category === '전체' }"
                v-on:click="update_sub_category"
              >
                <span>전체</span>
              </li>
              <li
                v-for="(sublist, idx) in Object.values(list)[0]"
                v-bind:key="idx"
                v-bind:id="sublist"
                v-on:click="update_sub_category"
                v-bind:class="{ select: select_sub_category === sublist }"
              >
                <span>{{ sublist }}</span>
              </li>
            </ul>
          </div>
        </article>
      </section>
      <section class="product">
        <article class="product-header">
          <div class="fillter-container">
            <div class="fillter" v-on:click="fillter_opener">
              <span>{{ filltering_criteria }}</span>
              <img
                v-bind:class="{ 'down-arrow': is_fllter_active }"
                alt="arrow"
                src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-arrow-bl-down@3x.png"
              />
            </div>
            <div
              v-for="(list,idx) in fillter_list"
              v-bind:key="idx"
              v-bind:class="{
                fillter: is_fllter_active,
                none: !is_fllter_active,
              }"
              v-bind:id="list"
              v-on:click="fillering_what"
            >{{ list }}</div>
          </div>
        </article>
        <article class="product-list">
          <router-link
            v-bind:to="`/products/${list.product_id}`"
            v-for="(list,idx) in datas.product_list"
            v-bind:key="idx + `product_id`"
          >
            <categories-card v-bind="list" />
          </router-link>
        </article>
      </section>
    </main>
  </div>
</template>

<script>
import axios from "axios";
import { config } from "../../api/apiConfig";
import categoriesCard from "./ProductCard/CategoriesCard.vue";

export default {
  name: "categories",
  components: { categoriesCard },
  data: () => ({
    top_category: "",
    is_sale_list: false,
    is_fllter_active: false,
    filltering_criteria: "인기순",
    select_main_category: "",
    select_sub_category: "",
    fillter_list: ["인기순", "최신순", "가격순"],
    datas: {
      nav_list: [],
      product_list: {},
    },
  }),
  computed: {
    main_category_number: function () {
      for (let i = 0; i < Object.values(this.datas.nav_list).length; i++) {
        if (
          Object.keys(Object.values(this.datas.nav_list)[i])[0] ===
          this.select_main_category
        ) {
          return i;
        }
      }
    },
    sub_category_number: function () {
      return Object.values(
        Object.values(this.datas.nav_list)[this.main_category_number]
      )[0].indexOf(this.select_sub_category);
    },
  },
  methods: {
    query_maker: function () {
      let query_arr = [];
      if (this.is_sale_list) {
        query_arr.push("&is_discounted=1");
      }
      if (this.filltering_criteria === "인기순") {
        query_arr.push("&is_popular=1");
      }
      if (this.filltering_criteria === "최신순") {
        query_arr.push("&is_new=1");
      }
      if (this.filltering_criteria === "가격순") {
        query_arr.push("&is_cheap=1");
      }
      if (this.select_main_category && this.select_sub_category === "전체") {
        query_arr.unshift(`&fc_id=${this.main_category_number}`);
      } else if (
        this.select_sub_category &&
        this.select_sub_category !== "전체"
      ) {
        query_arr.unshift(
          `&fc_id=${this.main_category_number}&sc_id=${this.sub_category_number}`
        );
      }
      query_arr.unshift(`?sp_id=${this.$route.params.id}`);
      this.$router.push(query_arr.join(""));
    },
    update_main_category: function (e) {
      let updatedText = e.target.id;
      if (e.target.id !== this.select_main_category) {
        this.select_main_category = updatedText;
      } else {
        this.select_main_category = "";
      }

      if (this.select_main_category === "전체") {
        this.$router.push(`?sp_id=${this.$route.params.id}`);

        axios
          .get(
            `${config.API}products${this.$route.fullPath.replace(
              this.$route.path,
              ""
            )}`
          )
          .then((res) => (this.datas.product_list = res.data));
      }
    },
    update_sub_category: function (e) {
      let updatedText = e.target.id;
      if (updatedText) {
        this.select_sub_category = updatedText;
      } else {
        this.select_sub_category = "전체";
      }
      this.query_maker();

      axios
        .get(
          `${config.API}products${this.$route.fullPath.replace(
            this.$route.path,
            ""
          )}`
        )
        .then((res) => (this.datas.product_list = res.data));
    },

    fillter_opener: function () {
      this.is_fllter_active = !this.is_fllter_active;
    },
    fillering_what: function (e) {
      this.filltering_criteria = e.target.id;

      this.query_maker();

      axios
        .get(
          `${config.API}products${this.$route.fullPath.replace(
            this.$route.path,
            ""
          )}`
        )
        .then((res) => (this.datas.product_list = res.data));
      this.is_fllter_active = false;
    },
    sale_checker: function () {
      this.is_sale_list = !this.is_sale_list;

      this.query_maker();

      axios
        .get(
          `${config.API}products${this.$route.fullPath.replace(
            this.$route.path,
            ""
          )}`
        )
        .then((res) => (this.datas.product_list = res.data));
    },
  },
  mounted: function () {
    axios
      .get(`${config.API}category?q=${this.$route.params.id}`)
      .then(
        (res) => (
          (this.datas.nav_list = Object.values(res.data)[0]),
          (this.top_category = Object.keys(res.data)[0])
        )
      );

    axios
      .get(
        `${config.API}products${this.$route.fullPath.replace(
          this.$route.path,
          ""
        )}`
      )
      .then((res) => (this.datas.product_list = res.data));
  },
};
</script>

<style lang="scss" scoped>
.categories {
  header {
    height: 70px;
    padding: 20px 0 30px;

    ul {
      display: flex;

      li {
        font-size: 14px;
        color: #b2b2b2;

        &:last-child {
          color: black;
          span {
            color: #b2b2b2;
          }
        }

        span {
          position: relative;
          bottom: 1px;
          padding: 4px;
        }
      }
    }
  }

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

  main,
  header article {
    display: flex;
    max-width: 1300px;
    margin: auto;
    padding: 0 30px;
  }

  main {
    .product {
      display: flex;
      flex-direction: column;
      width: 992px;
      padding: 16px 0 20px;

      .product-header {
        position: relative;
        display: flex;
        justify-content: flex-end;
        height: 45px;

        .fillter-container {
          position: absolute;
        }

        .fillter {
          display: flex;
          justify-content: space-between;
          align-items: center;
          width: 130px;
          height: 35px;
          font-size: 14px;
          border: 1px solid #e7e7e7;
          border-top: 0;
          margin-right: 6.188px;
          padding: 7px 10px;
          cursor: pointer;
          background-color: white;

          &:first-child {
            border-top: 1px solid #e7e7e7;
          }

          img {
            display: block;
            width: 13px;
          }

          .down-arrow {
            transform: rotate(180deg);
          }
        }
      }
    }

    .product-list {
      display: flex;
      flex-wrap: wrap;
    }

    .sub-nav {
      display: flex;
      flex-direction: column;

      article {
        width: 248px;
        margin-top: 20px;
        padding-right: 12.391px;
      }

      ul,
      .nav-box,
      h2 {
        border-bottom: 1px solid #e7e7e7;
        margin-right: 20px;
        margin-bottom: 0;
      }

      ul {
        padding: 6px 0;
      }

      li {
        display: flex;
        align-items: center;
        height: 39px;
        font-size: 14px;
        color: #696969;
        padding-left: 12px;
        cursor: pointer;

        &:hover {
          color: black;
          background-color: #f2f2f2;
        }
      }

      .select {
        color: black;
        background-color: #f2f2f2;
      }

      .nav-box,
      h2 {
        display: flex;
        align-items: center;
        height: 60px;
      }

      h2 {
        span {
          margin: auto 0;
        }
      }

      .nav-box {
        display: flex;
        justify-content: space-between;
        cursor: pointer;

        img {
          width: 12px;
          margin-right: 10px;
        }
      }

      .checkbox {
        justify-content: flex-start;
        font-size: 15px;
        font-weight: 500;
        padding: 20px 0;
      }

      .checked,
      .unchecked {
        position: relative;
        top: 2px;
        width: 17px;
        height: 17px;
        font-weight: 700;
        text-align: center;
        line-height: 17px;
        color: white;
        margin: 0 10px;
      }

      .unchecked {
        background-color: white;
        border: 1px solid #969696;
      }

      .checked {
        background-color: black;
      }

      h2 {
        font-size: 18px;
        font-weight: 600;
        margin-top: 20px;

        &:first-child {
          margin-top: 0;
        }
      }
    }
  }
}
</style>
