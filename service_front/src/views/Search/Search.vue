<template>
  <div class="search">
    <header>
      <button
        id="product"
        v-bind:class="{ 'select-header': this.select_search === 'product' }"
        v-on:click="switching_search"
      >
        상품
      </button>
      <button
        id="store"
        v-bind:class="{ 'select-header': this.select_search === 'store' }"
        v-on:click="switching_search"
      >
        스토어
      </button>
    </header>
    <main>
      <section
        v-bind:class="{
          'product-container': this.select_search === 'product',
          none: this.select_search !== 'product',
        }"
      >
        <article>
          검색결과(<span>{{ this.datas.products.length }}</span
          >건)
        </article>
        <article>
          <div class="checkbox-container" v-on:click="checkbox_clicker">
            <div class="sale-checkbox">
              <img
                v-bind:class="{ checked: is_checked }"
                alt="checkbox"
                src="https://web-staging.brandi.co.kr/static/2020.7.3/images/icon_check_bg.png"
              />
            </div>
            <span>세일</span>
          </div>
          <div class="filter-container">
            <div class="filter-box-fix" v-on:click="filter_closer">
              <span>{{ this.filter }}</span
              ><img
                v-bind:class="{ 'reverse-img': open_filter }"
                alt="arrow"
                src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-arrow-bl-down@3x.png"
              />
            </div>
            <div v-bind:class="{ none: !open_filter }">
              <div class="filter-floating">
                <div class="filter-box" id="추천순" v-on:click="filter_closer">
                  추천순
                </div>
                <div
                  class="filter-box"
                  id="판매량순"
                  v-on:click="filter_closer"
                >
                  판매량순
                </div>
                <div class="filter-box" id="최신순" v-on:click="filter_closer">
                  최신순
                </div>
              </div>
            </div>
          </div>
        </article>
        <article>
          <a v-for="list in datas.products" v-bind:key="list.product_id">
            <ul class="product">
              <li><img alt="store logo" v-bind:src="list.image_url" /></li>
              <li>{{ list.seller_name }}</li>
              <li>
                <p>{{ list.product_name }}</p>
              </li>
              <li>
                <span
                  v-bind:class="{
                    discount: list.discount_rate,
                    none: !list.discount_rate,
                  }"
                  >{{ list.discount_rate }}%</span
                >
                <span class="price">{{
                  list.origin_price * (1 - list.discount_rate / 100)
                }}</span>
                <span
                  v-bind:class="{
                    'origin-price': list.discount_rate,
                    none: !list.discount_rate,
                  }"
                  >{{ list.origin_price }}</span
                >
              </li>
              <li>{{ list.sale_amount }}개 구매중</li>
            </ul>
          </a>
        </article>
      </section>
      <section
        v-bind:class="{
          'store-container': this.select_search === 'store',
          none: this.select_search !== 'store',
        }"
      >
        <article>
          스토어 검색결과(<span>{{ this.datas.stores.length }}</span
          >건)
        </article>
        <article>
          <div
            class="store"
            v-for="list in datas.stores"
            v-bind:key="list.seller_id"
          >
            <img alt="store logo" v-bind:src="list.profile_image" />
            <div>
              <p>{{ list.korean_name }}</p>
              <p>
                <span v-for="hash in list.hash_tag" v-bind:key="hash"
                  >#{{ hash }}</span
                >
              </p>
            </div>
          </div>
        </article>
      </section>
    </main>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "",
  components: {},
  data: () => ({
    is_checked: false,
    select_search: "product",
    filter: "추천순",
    open_filter: false,
    datas: {
      products: [
        {
          discount_rate: 0,
          discounted_price: 32000,
          image_url:
            "https://image.brandi.me/cproduct/2020/06/04/17082238_1591255535_image1_M.jpg",
          origin_price: 32000,
          product_id: 1,
          product_name: "vivi 반팔자켓 린넨자켓 2col_무드글램",
          sale_amount: 0,
          seller_name: "이지연1",
        },
        {
          discount_rate: 0,
          discounted_price: 32000,
          image_url:
            "https://image.brandi.me/cproduct/2020/06/04/17082238_1591255535_image1_M.jpg",
          origin_price: 32000,
          product_id: 2,
          product_name: "vivi 반팔자켓 린넨자켓 2col_무드글램",
          sale_amount: 0,
          seller_name: "이지연1",
        },
        {
          discount_rate: 10,
          discounted_price: 32000,
          image_url:
            "https://image.brandi.me/cproduct/2020/06/04/17082238_1591255535_image1_M.jpg",
          origin_price: 32000,
          product_id: 3,
          product_name: "vivi 반팔자켓 린넨자켓 2col_무드글램",
          sale_amount: 10,
          seller_name: "이지연1",
        },
        {
          discount_rate: 0,
          discounted_price: 32000,
          image_url:
            "https://image.brandi.me/cproduct/2020/06/04/17082238_1591255535_image1_M.jpg",
          origin_price: 32000,
          product_id: 4,
          product_name: "vivi 반팔자켓 린넨자켓 2col_무드글램",
          sale_amount: 0,
          seller_name: "이지연1",
        },
        {
          discount_rate: 20,
          discounted_price: 32000,
          image_url:
            "https://image.brandi.me/cproduct/2020/06/04/17082238_1591255535_image1_M.jpg",
          origin_price: 32000,
          product_id: 5,
          product_name: "vivi 반팔자켓 린넨자켓 2col_무드글램",
          sale_amount: 147,
          seller_name: "이지연1",
        },
        {
          discount_rate: "",
          discounted_price: 32000,
          image_url:
            "https://image.brandi.me/cproduct/2020/06/04/17082238_1591255535_image1_M.jpg",
          origin_price: 32000,
          product_id: 6,
          product_name: "vivi 반팔자켓 린넨자켓 2col_무드글램",
          sale_amount: 147,
          seller_name: "이지연1",
        },
      ],
      stores: [
        {
          korean_name: "이지연1",
          profile_image:
            "https://image.brandi.me/cproduct/2020/01/17/13216968_1579243036_image1_L.jpg",
          seller_id: 1,
        },
      ],
    },
  }),
  methods: {
    checkbox_clicker: function () {
      this.is_checked = !this.is_checked;
      if (this.is_checked) {
        axios
          .get("public/data/mockData/discountjson.json")
          .then((res) => (this.datas = { ...this.datas, ...res.data }));
      } else {
        axios
          .get("public/data/mockData/allproductjson.json")
          .then((res) => (this.datas = { ...this.datas, ...res.data }));
      }
    },
    switching_search: function (e) {
      this.select_search = e.target.id;
    },
    filter_closer: function (e) {
      if (e.target.id) {
        this.filter = e.target.id;
      }
      this.open_filter = !this.open_filter;
    },
  },
  // created: function () {
  //   axios
  //     .get("http://10.251.1.160:5000/search?q=이지연&r=10")
  //     .then((res) => (this.datas = res.data));
  // },
};
</script>

<style lang="scss" scoped>
.search {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100wv;

  .none {
    display: none;
  }

  header {
    display: flex;
    width: 80%;
    height: 62px;
    margin-top: 20px;

    button {
      width: 50%;
      font-size: 15px;
      border-bottom: 1px solid #e1e1e1;

      &:focus {
        outline: none;
      }
    }

    .select-header {
      color: #ff1f4b;
      border-bottom: 3px solid #ff1f4b;
    }
  }

  main {
    width: 90%;
    margin: 0 auto;
    padding: 0 2.3%;

    section {
      padding: 50px 0 0.9%;
    }

    .product-container {
      article {
        &:first-child {
          font-size: 19.5px;
          font-weight: 700;
          margin-bottom: 30px;
          span {
            color: #ff1f4b;
          }
        }
        &:nth-child(2) {
          display: flex;
          justify-content: space-between;
          margin-bottom: 20px;

          .checkbox-container {
            display: flex;
            align-items: center;
            padding-left: 0.6%;
            cursor: pointer;
          }

          .filter-container {
            position: relative;
            display: flex;
            flex-direction: column;
            width: 11.4%;

            .filter-floating {
              position: absolute;
              width: 100%;
            }

            .filter-box,
            .filter-box-fix {
              display: flex;
              justify-content: space-between;
              align-items: center;
              height: 34px;
              font-size: 13px;
              border: 1px solid #e1e1e1;
              padding: 0 6%;

              img {
                width: 13%;
              }

              .reverse-img {
                transform: rotate(180deg);
              }

              &:active {
                color: #ff1f4b;
              }
            }

            .filter-box {
              border-top: 0;
              &:hover {
                color: #ff1f4b;
              }
            }
          }
        }

        &:last-child {
          display: flex;
          flex-wrap: wrap;
          a {
            width: 20%;
            .product {
              display: flex;
              flex-direction: column;
              margin: 0;
              padding: 0 0.6% 30px;

              li {
                display: flex;

                &:first-child {
                  img {
                    width: 100%;
                  }
                }

                &:nth-child(2) {
                  font-size: 15px;
                  margin-top: 8px;
                }

                &:nth-child(3) {
                  p {
                    font-size: 16px;
                    font-weight: 500;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    white-space: nowrap;
                    margin: 0;
                  }
                }
                &:nth-child(4) {
                  display: flex;
                  align-items: flex-end;
                  font-size: 20px;
                  font-weight: 600;

                  span {
                    padding-right: 1%;

                    &:first-child {
                      color: #ff1f4b;
                    }

                    &:last-child {
                      font-size: 15px;
                      font-weight: 400;
                      color: #757575;
                      text-decoration: line-through;
                      padding-bottom: 1%;
                    }
                  }
                }
                &:last-child {
                  font-size: 13px;
                  color: #757575;
                  margin-top: 10px;
                }
              }
            }
          }
        }
      }
      .sale-checkbox {
        max-height: 17px;
        overflow: hidden;
        margin-right: 5px;
        img {
          position: relative;
          max-height: initial;
        }

        .checked {
          top: -17px;
        }
      }
    }

    .store-container {
      height: 100px;
      article {
        &:first-child {
          margin: 12.45px 0;
          span {
            color: #ff1f4b;
          }
        }

        &:last-child {
          display: flex;
          flex-wrap: wrap;

          .store {
            display: flex;
            width: 23%;
            margin: 1%;

            img {
              width: 20%;
              display: block;
              border-radius: 50%;
              margin-right: 6%;
            }
            p {
              margin: 0;

              &:first-child {
                font-size: 15.6px;
              }
              &:last-child {
                font-size: 13px;
                color: #8d8d8d;
                span {
                  margin-right: 5px;
                }
              }
            }
          }
        }
      }
    }
  }
}
</style>
