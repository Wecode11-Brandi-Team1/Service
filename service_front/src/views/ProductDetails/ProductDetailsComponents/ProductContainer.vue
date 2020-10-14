<template>
  <section class="product-container">
    <article class="photo-container">
      <button class="large-photo-container">
        <div class="moving-photo" v-bind:style="moving_photo">
          <img
            class="large-photo"
            alt="product photo"
            v-bind:src="list"
            v-for="list in image_path"
            v-bind:key="list"
          />
        </div>
      </button>

      <div class="small-photo-container">
        <img
          v-for="(list, idx) in image_path"
          v-bind:key="list"
          alt="product photo"
          v-bind:src="list"
          v-bind:id="list"
          v-on:click="move_this_photo(idx)"
        />
      </div>
    </article>
    <article class="details">
      <ul>
        <li>
          <img
            alt="house"
            src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-btn-seller-28-pt.svg"
          />
          <span class="seller-name">{{ seller_name }}</span>
          <img
            alt="arrow"
            src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-arrow-left-black-28-pt.svg"
          />
        </li>
        <li>
          <span class="product-name">{{ product_name }}</span>
        </li>
        <li class="price-container">
          <div class="price">
            <p class="discount-rate" v-if="discount_rate">{{ discount_rate }}%</p>
            <p class="final-price">
              {{
              Number(sale_price * (1 - discount_rate / 100)).toLocaleString(
              "en"
              )
              }}
              <span>원</span>
            </p>
            <p class="sale-price" v-if="discount_rate">
              {{ Number(sale_price).toLocaleString("en") }}
              <span>원</span>
            </p>
          </div>
          <button class="couppon-open" v-on:click="modal_opener">
            쿠폰받기
            <img
              alt="coupon download"
              src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-download-black-12-pt.svg"
            />
          </button>
          <div class="coupon-modal" v-if="open_modal">
            <div class="coupon-container">
              <div class="close-container">
                <img
                  alt="close"
                  v-on:click="modal_opener"
                  src="https://web-staging.brandi.co.kr/static/20.08.01/images/ic-close-gray-28-pt.svg"
                />
              </div>
              <div class="coupon-frame">
                <div class="coupon" v-for="(list, idx) in datas.coupon" v-bind:key="`coupon` + idx">
                  <div class="red-label" />
                  <div class="coupon-info">
                    <div class="coupon-name">
                      <span>{{ list.coupon_name }}</span>
                      <img
                        alt="coupon download"
                        v-on:click="coupon_downloader(list)"
                        src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-download-black-12-pt.svg"
                      />
                    </div>
                    <div class="coupon-price">
                      {{ Number(list.discount_price).toLocaleString("en")
                      }}
                      <span>원</span>
                    </div>
                    <div class="coupon-sub-info">
                      <span>
                        {{ Number(list.minimum_price).toLocaleString("en") }}원
                        이상 구매시
                      </span>
                      <span class="coupon-date">
                        {{ list.download_started_at }}~{{
                        list.download_ended_at
                        }}
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </li>
        <li class="sale_amount">
          <span>{{ Number(sale_amount).toLocaleString("en") }}개 구매중</span>
        </li>
        <li class="option-choice">
          <div class="option-select-container">
            <div class="option-default" id="color-choice" v-on:click="option_opener">
              <span id="color-choice">{{ option_color_child }}</span>
              <img
                alt="arrow"
                src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-drop-down-black-16-pt.svg"
              />
            </div>
            <div class="option-select" v-if="open_option === 'color-choice'">
              <div
                class="option-default-open"
                v-bind:id="option_color_child"
                v-on:click="option_closer_color"
              >
                <span v-bind:id="option_color_child">
                  {{
                  option_color_child
                  }}
                </span>
                <img
                  v-bind:id="option_color_child"
                  alt="arrow"
                  src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-drop-down-black-16-pt.svg"
                />
              </div>
              <div class="option-list-container">
                <div
                  class="option-list"
                  v-bind:id="list"
                  v-on:click="option_closer_color"
                  v-for="list in option_color"
                  v-bind:key="list"
                >
                  <span v-bind:id="list">{{ list }}</span>
                  <img
                    alt="common"
                    v-bind:id="list"
                    src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-seller-xl@3x.png"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="option-select-container">
            <div
              class="option-default"
              v-bind:class="{
                disabled: this.option_color_child === '[색상]을 선택하세요.',
              }"
              id="size-choice"
              v-on:click="option_opener"
            >
              <span id="size-choice">{{ option_size_child }}</span>
              <img
                alt="arrow"
                src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-drop-down-black-16-pt.svg"
              />
            </div>
            <div class="option-select" v-if="open_option === 'size-choice'">
              <div
                class="option-default-open"
                v-bind:id="option_size_child"
                v-on:click="option_closer_size"
              >
                <span v-bind:id="option_size_child">
                  {{
                  option_size_child
                  }}
                </span>
                <img
                  v-bind:id="option_size_child"
                  alt="arrow"
                  src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-drop-down-black-16-pt.svg"
                />
              </div>
              <div class="option-list-container">
                <div
                  class="option-list"
                  v-bind:id="list.size"
                  v-on:mousedown="option_closer_size"
                  v-on:mouseup="size_checker(list)"
                  v-for="list in option_size"
                  v-bind:key="list.size"
                >
                  <span v-bind:id="list.size">{{ list.size }}</span>
                  <img
                    alt="common"
                    v-bind:id="list"
                    src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-seller-xl@3x.png"
                  />
                </div>
              </div>
            </div>
          </div>
        </li>
        <li
          v-bind:class="{
            'choice-result-container': result_option.length !== 0,
            none: result_option.length === 0,
          }"
          v-for="(list, idx) in result_option"
          v-bind:key="idx"
        >
          <div class="choice-result">
            <p>
              <span>{{ list.select_option }}</span>
            </p>
            <img
              alt="close"
              src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-close-gray-16-pt.svg"
              v-bind:id="idx"
              v-on:click="delete_result"
            />
          </div>
          <img
            class="one-day"
            alt="common"
            src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-seller-xl@3x.png"
          />
          <div class="result-price">
            <div class="product-amount">
              <button v-on:click="plus(list)">
                <img
                  alt="add"
                  src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-amount-add-black-16-pt.svg"
                />
              </button>
              <span>{{ list.quantity }}</span>
              <button v-on:click="minus(list)">
                <img
                  alt="minus"
                  src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-amount-delete-black-16-pt.svg"
                />
              </button>
            </div>
            <span>
              {{
              Number(
              sale_price * (1 - discount_rate / 100) * list.quantity
              ).toLocaleString("en")
              }}원
            </span>
          </div>
        </li>
        <li class="all-sum-price">
          <p>총 사용 금액</p>
          <p>
            <span>
              {{
              Number(
              sale_price * (1 - discount_rate / 100) * sum_result
              ).toLocaleString("en")
              }}
            </span>원
          </p>
        </li>
        <li
          class="perchase"
          v-on:mousedown="large_photo_slider"
          v-on:click="mouse_location_cheacker"
        >
          <button v-on:click="save_product_data">주문 하기</button>
          <button v-on:click="move_order">
            <img
              alt="cart"
              src="https://web-staging.brandi.co.kr/static/2020.7.3/images/btn-cart.svg"
            />
          </button>
        </li>
      </ul>
    </article>
  </section>
</template>

<script>
import axios from "axios";
import { config } from "../../../api/apiConfig";

export default {
  name: "product-container",
  components: {},
  props: [
    "product_id",
    "seller_name",
    "product_name",
    "discount_rate",
    "sale_price",
    "sale_amount",
    "image_path",
    "option",
  ],
  data: () => ({
    open_modal: false,
    open_option: "",
    option_color_child: "[색상]을 선택하세요.",
    option_size_child: "[사이즈]를 선택하세요.",
    result_option: [],
    moving_photo: { transform: "" },
    mouse_location: "",
    moving_photo_num: "",
    datas: {
      coupon: [],
    },
  }),
  computed: {
    sum_result: function () {
      let result = 0;
      if (this.result_option.length > 0) {
        for (let i = 0; i < this.result_option.length; i++) {
          result = result + this.result_option[i].quantity;
        }
      }
      return result;
    },
    option_color: function () {
      let color = new Set();
      let colorInArray = [];
      for (let i = 0; i < this.option.length; i++) {
        color.add(this.option[i].color);
      }
      colorInArray = [...color];

      return colorInArray;
    },
    option_size: function () {
      let size = [];
      for (let i = 0; i < this.option.length; i++) {
        if (this.option[i].color === this.option_color_child) {
          size.push({
            size: this.option[i].size,
            stock: this.option[i].stock,
            option_id: this.option[i].option_id,
          });
        }
      }
      return size;
    },
    result_option_arr: function () {
      let optionArr = [];
      for (let i = 0; i < this.result_option.length; i++) {
        optionArr.push(this.result_option[i].select_option);
      }
      return optionArr;
    },
  },
  methods: {
    modal_opener: function () {
      this.open_modal = !this.open_modal;
    },
    option_opener: function (e) {
      if (
        e.target.id === "size-choice" &&
        this.option_color_child === "[색상]을 선택하세요."
      ) {
        this.open_option = "";
      } else {
        this.open_option = e.target.id;
      }
    },
    plus: function (list) {
      if (list.stock > list.quantity) {
        list.quantity += 1;
        list.final_price = list.discount_price * list.quantity;
      }
    },
    minus: function (list) {
      if (list.quantity > 1) {
        list.quantity -= 1;
        list.final_price = list.discount_price * list.quantity;
      }
    },
    option_closer_color: function (e) {
      this.option_color_child = e.target.id;
      this.open_option = "";
    },
    size_checker: function (list) {
      if (
        this.option_color_child !== "[색상]을 선택하세요." &&
        this.option_size_child !== "[사이즈]를 선택하세요." &&
        this.result_option_arr.indexOf(
          this.option_color_child + ` / ` + this.option_size_child
        ) === -1
      ) {
        this.result_option = [
          ...this.result_option,
          {
            quantity: 1,
            stock: list.stock,
            select_option:
              this.option_color_child + ` / ` + this.option_size_child,
            option_id: list.option_id,
            orderer_name: this.product_name,
            final_price: this.sale_price * (1 - this.discount_rate / 100),
            price: this.sale_price,
            discount_price: this.sale_price * (1 - this.discount_rate / 100),
            seller_name: this.seller_name,
            img_url: this.image_path[0],
          },
        ];
      }

      if (
        this.option_color_child !== "[색상]을 선택하세요." &&
        this.option_size_child !== "[사이즈]를 선택하세요."
      ) {
        this.option_color_child = "[색상]을 선택하세요.";
        this.option_size_child = "[사이즈]를 선택하세요.";
      }

      this.open_option = "";
    },
    option_closer_size: function (e) {
      this.option_size_child = e.target.id;
    },
    delete_result: function (e) {
      if (confirm("선택하신 상품을 삭제하시겠습니까?")) {
        this.result_option.splice(e.target.id, 1);
        this.option_color_child = "[색상]을 선택하세요.";
        this.option_size_child = "[사이즈]를 선택하세요.";
      }
    },
    move_order: function () {
      this.$router.push({ path: "/order" });
    },
    move_this_photo: function (num) {
      this.moving_photo_num = -100 * num;
      this.moving_photo.transform =
        `translatex(` + this.moving_photo_num + `%)`;
    },
    mouse_location_cheacker: function (e) {
      let y = e.pageY;
      this.mouse_location = y;
    },
    large_photo_slider: function (e) {
      let click_location = e.pageY;
      let move_location = click_location - this.mouse_location;
      console.log(click_location - this.mouse_location);
    },
    save_product_data: function () {
      // let result = [];
      // if (localStorage.data) {
      //   result.push(JSON.parse(localStorage.getItem("data")));
      //   for (let i in this.result_option) {
      //     result.push(this.result_option[i]);
      //   }
      //   localStorage.setItem("data", JSON.stringify(result));
      // } else {
        localStorage.setItem("data", JSON.stringify(this.result_option));
      // }
      alert("주문하기에 담았습니다.");
    },
    coupon_downloader: function (obj) {
      axios
        .post(
          `${config.API}coupons?c=${obj.coupon_id}`,
          {
            questions: { a: "" },
          },
          {
            headers: {
              Authorization: this.$cookies.get("accesstoken"),
            },
          }
        )
        .then((response) => {
            if(res.status===200){alert("쿠폰이 등록되었습니다.")}
          })
          .catch((error) => {
            alert("이미 등록된 쿠폰입니다.")
        })
    },
  },
  created: function () {
    axios
      .get(`${config.API}coupons`, {
        headers: {
          Authorization: this.$cookies.get("accesstoken"),
        },
      })
      .then((res) => (this.datas.coupon = res.data.coupons));
  },
};
</script>

<style lang="scss" scoped>
.product-container {
  display: flex;
  justify-content: space-between;
  margin-bottom: 170px;

  button {
    &:focus {
      outline: none;
    }
  }

  .none {
    display: none;
  }

  .photo-container {
    width: 560px;
    margin-right: 48px;
    margin-bottom: 15px;

    .large-photo-container {
      position: relative;
      overflow: hidden;
    }

    .moving-photo {
      position: relative;
      display: flex;
      width: 560px;
      transition: transform 0.3s;
    }

    .large-photo {
      width: 560px;
      height: 620px;
      margin-bottom: 20px;
      background-color: black;
    }

    .fade-image,
    .small-photo-container {
      display: flex;
      flex-wrap: nowrap;
      overflow: scroll;
      &::-webkit-scrollbar {
        display: none;
      }

      .fade-image {
        opacity: 0.8;
      }

      img {
        height: 86px;
        width: 82px;
        margin-right: 10.6px;
        background-color: black;
      }
    }
  }
  .disabled {
    color: #c5c5c5;
  }
  .details {
    width: 592px;
    color: #1e1e1e;

    li {
      display: flex;
      margin-bottom: 10px;
    }

    .none {
      display: none;
    }

    ul li:first-child img {
      position: relative;
      bottom: 2px;
    }

    .seller-name {
      font-size: 22px;
      margin: 0 10px;
    }

    .product-name {
      font-size: 28px;
    }

    .price-container {
      align-items: center;
    }

    .sale_amount {
      padding-left: 5px;
    }

    .price {
      display: flex;
      align-items: flex-end;

      p {
        margin: 0;
      }

      .discount-rate {
        font-size: 34px;
        font-weight: 700;
        color: #ff204b;
        margin-right: 5px;
      }

      .final-price {
        font-size: 34px;
        font-weight: 700;
        margin-right: 10px;

        span {
          font-size: 20px;
        }
      }

      .sale-price {
        position: relative;
        font-size: 20px;
        color: #c5c5c5;
        line-height: 37px;
        text-decoration: line-through;
        margin-right: 10px;

        span {
          font-size: 12px;
        }
      }
    }

    .couppon-open {
      height: 32px;
      font-size: 12px;
      border: 1px solid black;
      border-radius: 4px;
      padding: 7px 8px;
      img {
        position: relative;
        bottom: 2px;
        margin-left: 20px;
      }
    }

    .coupon-modal {
      position: fixed;
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 9999999999;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background-color: rgba(0, 0, 0, 0.4);

      .coupon-container {
        width: 35vw;
        max-height: 50vh;
        overflow: scroll;
        background-color: white;
        -ms-overflow-style: none;
        &::-webkit-scrollbar {
          display: none;
        }
      }

      .close-container {
        display: flex;
        justify-content: flex-end;
        padding-top: 5px;
        padding-right: 5px;
      }

      .coupon-frame {
        display: flex;
        flex-direction: column;
        padding: 0 40px 33px 40px;
      }

      .coupon {
        display: flex;
        overflow: hidden;
        border: 1px solid #dddddd;
        border-radius: 5px;
        margin-bottom: 15px;

        &:last-child {
          margin-bottom: 0;
        }
      }

      .red-label {
        width: 0.8%;
        background-color: #ff1f4b;
        margin-right: 20px;
      }

      .coupon-info {
        display: flex;
        flex-direction: column;
        width: 100%;
        padding-right: 20px;
      }

      .coupon-name {
        display: flex;
        justify-content: space-between;

        font-size: 14px;
        font-weight: 700;
        margin-top: 20px;

        img {
          width: 18px;
        }
      }
      .coupon-price {
        font-size: 20px;
        font-weight: 700;

        span {
          font-size: 18px;
        }
      }

      .coupon-sub-info {
        display: flex;
        justify-content: space-between;
        margin-top: 5px;
        margin-bottom: 20px;
        span {
          &:first-child {
            font-size: 14px;
            color: #9e9e9e;
          }
          &:last-child {
            font-size: 11px;
            color: #c5c5c5;
          }
        }
      }
    }

    .option-choice {
      flex-direction: column;
      margin-bottom: 13px;

      .option-select-container {
        position: relative;
        margin: 5px 0;

        .option-default,
        .option-default-open {
          display: flex;
          justify-content: space-between;
          width: 100%;
          display: flex;
          align-items: center;
          height: 50px;
          font-size: 16px;
          padding-left: 16px;
          padding-right: 20px;
        }

        .option-default {
          border: 1px solid #e1e1e1;
          border-radius: 8px;
        }

        .option-default-open {
          border-bottom: 1px solid #e1e1e1;

          img {
            transform: rotate(180deg);
          }
        }

        .option-select {
          position: absolute;
          top: 0;
          z-index: 10000;
          width: 100%;
          border: 1px solid #e1e1e1;
          border-radius: 8px;
          background-color: white;

          .option-list-container {
            max-height: 300px;
            overflow: scroll;
          }

          .option-list {
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 78px;
            font-size: 18px;
            border-top: 1px solid #e1e1e1;
            padding: 16px;

            &:first-child {
              border: 0;
            }

            img {
              width: 57px;
              height: 14px;
            }
          }
        }
      }
    }

    .choice-result-container {
      flex-direction: column;
      border-radius: 8px;
      padding: 20px;
      background-color: #f5f6f6;

      .one-day {
        width: 57px;
        height: 14px;
      }

      .choice-result {
        p {
          font-size: 18px;
          margin: 0;
        }

        img {
          position: relative;
          bottom: 5px;
          width: 18px;
        }
      }

      .choice-result,
      .result-price {
        display: flex;
        justify-content: space-between;
      }

      .result-price {
        margin-top: 16px;
      }

      .product-amount {
        display: flex;
        align-items: center;
        width: 94px;
        height: 32px;
        border: 1px solid #eceef2;
        border-radius: 4px;
        background-color: white;

        button,
        span {
          width: 100%;
          height: 100%;
        }

        span {
          text-align: center;
          line-height: 30px;
          border-right: 1px solid #eceef2;
          border-left: 1px solid #eceef2;
        }
      }
    }

    .all-sum-price {
      justify-content: space-between;
      align-items: center;
      margin-top: 30px;

      p {
        &:first-child {
          font-size: 18px;
        }
        &:last-child {
          font-size: 20px;
          color: #ff204b;

          span {
            font-size: 30px;
            color: #ff204b;
          }
        }
      }
    }
    .perchase {
      justify-content: flex-end;
      height: 57px;
      padding-right: 10px;

      button {
        border-radius: 6px;

        &:first-child {
          width: 214px;
          font-size: 17px;
          font-weight: 500;
          color: white;
        }

        &:first-child {
          background-color: black;
        }

        &:last-child {
          width: 62px;
          border: 1px solid #eceef2;
          margin-left: 10px;
        }
      }
    }
  }
}
</style>
