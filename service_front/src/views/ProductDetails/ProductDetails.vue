<template>
  <main class="product-details">
    <product-container v-bind="datas" />
    <section class="product-info" id="info">
      <ul class="sub-nav">
        <a href="#info">
          <li v-bind:class="{ 'select-li': !see_QA }">
            <span>상품정보</span>
          </li>
        </a>
        <a href="#QA">
          <li v-bind:class="{ 'select-li': see_QA }">
            <span>Q&A({{ this.QA_list.qna_count }})</span>
          </li>
        </a>
      </ul>
      <article>
        <div class="main-info" v-html="datas.description"></div>
      </article>
      <article id="QA">
        <div class="QA-header">
          <h2>Q&A({{ this.QA_list.qna_count }})</h2>
          <div class="question">
            <div class="my-question" v-on:click="question_fillter">
              <img
                v-if="!see_my_question"
                alt="checkbox"
                src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-btn-checkbox-n-16-pt.svg"
              />
              <img
                v-if="see_my_question"
                alt="checkbox"
                src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-btn-checkbox-s-16-pt.svg"
              />
              <span>내가 쓴 글보기</span>
            </div>
            <div class="wall" />
            <span v-on:click="question_opener">문의하기</span>
          </div>
        </div>
        <ul class="question-input" v-if="send_question">
          <li>
            <div>질문 유형</div>
            <div>
              <div class="select-question-container">
                <input
                  type="button"
                  class="select-question"
                  v-bind:value="select_category"
                  v-on:click="category_selecter"
                />
                <div
                  class="select-question-list-container"
                  v-if="is_category_open"
                >
                  <div class="select-question-list">
                    <input
                      type="button"
                      class="select-question"
                      v-for="list in QA_category"
                      v-bind:key="list"
                      v-bind:value="list"
                      v-on:click="category_selecter"
                    />
                  </div>
                </div>
              </div>
            </div>
          </li>
          <li>
            <div>내용</div>
            <div>
              <textarea
                placeholder="내용을 입력해 주세요."
                v-on:change="input_main_text"
              ></textarea>
            </div>
          </li>
          <li>
            <div>공개여부</div>
            <div>
              <div class="secret-container" v-on:click="is_secret">
                <img
                  v-if="!secret"
                  alt="checkbox"
                  src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-btn-checkbox-n-16-pt.svg"
                />
                <img
                  v-if="secret"
                  alt="checkbox"
                  src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-btn-checkbox-s-16-pt.svg"
                />
                <span>비공개</span>
              </div>
            </div>
          </li>
          <li>
            <button v-on:click="clear_question">취소하기</button>
            <button v-on:click="upload_question">등록하기</button>
          </li>
        </ul>
        <ul class="QA-list">
          <li>
            <div>
              <span>분류</span>
            </div>
            <div>
              <span>처리상태</span>
            </div>
            <div class="QA-contents">
              <span>내용</span>
            </div>
            <div>
              <span>자</span>
            </div>
            <div>
              <span>작성일</span>
            </div>
          </li>
          <li
            v-for="(list, idx) in this.QA_list.questions"
            v-bind:key="list[1]"
          >
            <div>
              <span>{{ list.question_type }}</span>
            </div>
            <div>
              <span class="not-yet">답변대기</span>
            </div>
            <div>
              <span
                v-if="!list.is_secreted || list.user_id === QA_list.user_id"
                >{{ list.question_content }}</span
              >
              <span v-if="list.is_secreted && list.user_id !== QA_list.user_id">
                <img
                  alt="lock"
                  src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-key-s-22-pt.svg"
                />
                비밀글입니다.
              </span>
              <label v-if="QA_list.user_id === list.user_id">
                <input class="none" type="button" v-bind:value="idx" />
                <img
                  alt="delete"
                  v-on:click="delete_question(list.question_id)"
                  s
                  src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-close-gray-18-pt.svg"
                />
              </label>
            </div>
            <div>
              <span>{{ list.writer }}</span>
            </div>
            <div>
              <span>{{ list.created_at }}</span>
            </div>
          </li>
        </ul>
        <div class="page-button-container" v-if="QA_list.qna_count">
          <div class="arrow" @click="To_the_fore">
            <img
              v-if="button_value !== 1"
              alt="quick back"
              src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-more-arrow-right-black-28-pt.svg"
            />
          </div>
          <div class="arrow" @click="button_value_down">
            <img
              v-if="button_value !== 1"
              alt="quick back"
              src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-arrow-right-black-28-pt.svg"
            />
          </div>
          <input
            class="page-button"
            type="button"
            :value="button_value"
            v-on:click="pagenation_button_clicker"
          />
          <input
            class="page-button"
            type="button"
            :value="button_value + 1"
            v-if="page_button_visible(button_value + 1)"
            v-on:click="pagenation_button_clicker"
          />
          <input
            class="page-button"
            type="button"
            :value="button_value + 2"
            v-if="page_button_visible(button_value + 2)"
            v-on:click="pagenation_button_clicker"
          />
          <input
            class="page-button"
            type="button"
            :value="button_value + 3"
            v-if="page_button_visible(button_value + 3)"
            v-on:click="pagenation_button_clicker"
          />
          <input
            class="page-button"
            type="button"
            :value="button_value + 4"
            v-if="page_button_visible(button_value + 4)"
            v-on:click="pagenation_button_clicker"
          />

          <div class="arrow" @click="button_value_up">
            <img
              v-if="post_button_visible()"
              alt="quick front"
              src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-arrow-left-black-28-pt.svg"
            />
          </div>
          <div class="arrow" @click="To_the_last">
            <img
              v-if="post_button_visible()"
              alt="quick front"
              src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-more-arrow-left-black-28-pt.svg"
            />
          </div>
        </div>
      </article>
    </section>
  </main>
</template>

<script>
import axios from "axios";
import config from "../../api/apiConfig";
import productContainer from "./ProductDetailsComponents/ProductContainer.vue";

export default {
  name: "product-details",
  components: { productContainer },
  data: () => ({
    limit: 5,
    offset: 0,
    button_value: 1,
    see_my_question: false,
    send_question: false,
    is_category_open: false,
    my_user_name: "",
    select_category: "질문유형을 선택하세요.",
    main_text: "",
    secret: false,
    see_QA: false,
    QA_category: [
      "질문유형을 선택하세요.",
      "상품 문의",
      "교환/반품",
      "불량/오배송",
      "기타",
      "배송 문의",
      "하루배송",
      "취소/변경",
    ],
    QA_list: {
      qna_count: 0,
      questions: [],
    },
    datas: {
      product_id: 0,
      seller_name: "",
      product_name: "",
      sale_price: 0,
      discount_rate: 0,
      sale_amount: 0,
      option: [],
      image_path: [],
      description: "",
    },
  }),
  computed: {},
  methods: {
    button_value_up: function (e) {
      this.button_value = this.button_value + 5;
    },
    button_value_down: function (e) {
      this.button_value = this.button_value - 5;
    },
    To_the_fore: function () {
      this.button_value = 1;
    },
    To_the_last: function () {
      if (
        Math.floor(this.QA_list.qna_count / 5) ===
        this.QA_list.qna_count / 5
      ) {
        this.button_value = this.QA_list.qna_count / 5 - 4;
      } else {
        this.button_value = Math.floor(this.QA_list.qna_count / 5);
      }
    },
    post_button_visible: function () {
      if (
        Math.floor(this.QA_list.qna_count / 5) === this.QA_list.qna_count / 5 &&
        this.button_value === this.QA_list.qna_count / 5 - 4
      ) {
        return false;
      }
      if (
        Math.floor(this.QA_list.qna_count / 5) !== this.QA_list.qna_count / 5 &&
        this.button_value === Math.floor(this.QA_list.qna_count / 5)
      ) {
        return false;
      }
      return true;
    },
    page_button_visible: function (num) {
      if (
        Math.floor(this.QA_list.qna_count / 5) === this.QA_list.qna_count / 5 &&
        num <= Math.floor(this.QA_list.qna_count / 5)
      ) {
        return true;
      }
      if (
        Math.floor(this.QA_list.qna_count / 5) !== this.QA_list.qna_count / 5 &&
        num <= Math.floor(this.QA_list.qna_count / 5) + 1
      ) {
        return true;
      }
      return false;
    },
    pagenation_button_clicker: function (e) {
      this.offset = (e.target.value - 1) * this.limit;
      axios
        .get(
          `${config.API}/products/1/questions?offset=${this.offset}&limit=${this.limit}`,
          {
            headers: {
              Authorization: localStorage.getItem("token"),
            },
          }
        )
        .then((res) => (this.QA_list = res.data));
    },
    question_fillter: function () {
      this.see_my_question = !this.see_my_question;
      if (!this.see_my_question) {
        axios
          .get(`${config.API}/products/1/questions?limit=10`, {
            headers: {
              Authorization: localStorage.getItem("token"),
            },
          })
          .then((res) => (this.QA_list = res.data));
      } else {
        axios
          .get(`${config.API}/products/1/questions?u=${this.QA_list.user_id}`, {
            headers: {
              Authorization: localStorage.getItem("token"),
            },
          })
          .then((res) => (this.QA_list = res.data));
      }
    },
    is_secret: function () {
      this.secret = !this.secret;
    },
    question_opener: function () {
      this.send_question = !this.send_question;
    },
    category_selecter: function (e) {
      this.select_category = e.target.value;
      this.is_category_open = !this.is_category_open;
    },

    input_main_text: function (e) {
      this.main_text = e.target.value;
    },

    clear_question: function () {
      this.select_category = "질문유형을 선택하세요.";
      this.main_text = "";
      this.secret = false;
      this.send_question = false;
    },
    upload_question: function () {
      if (this.select_category === "질문유형을 선택하세요.") {
        return alert("질문유형을 선택하세요.");
      } else if (!this.main_text) {
        return alert("내용을 입력하세요");
      }
      axios
        .post(
          `${config.API}/products/1/questions`,
          {
            questions: {
              question_type_id: this.QA_category.indexOf(this.select_category),
              question_content: this.main_text,
              is_secreted: this.secret,
            },
          },
          {
            headers: {
              Authorization: localStorage.getItem("token"),
            },
          }
        )
        .then((res) => console.log(res))
        .then(() =>
          axios
            .get(`${config.API}/products/1/questions?limit=10`, {
              headers: {
                Authorization: localStorage.getItem("token"),
              },
            })
            .then((res) => (this.QA_list = res.data))
        )
        .catch((error) => console.log(error));

      alert("등록되었습니다.");
      this.select_category = "질문유형을 선택하세요.";
      this.main_text = "";
      this.secret = false;
      this.send_question = false;
    },
    handleScroll: function (e) {
      let length_QA = document
        .querySelector(".QA-header")
        .getBoundingClientRect().top;
      let length_info = document
        .querySelector(".product-info")
        .getBoundingClientRect().top;
      if (length_QA - window.innerHeight * 0.3 <= 0) {
        return (this.see_QA = true);
      } else {
        return (this.see_QA = false);
      }
    },
    delete_question(num) {
      let question_id = Number(num);
      axios
        .delete(`${config.API}/products/1/questions?q=${question_id}`, {
          headers: {
            Authorization: localStorage.getItem("token"),
          },
        })
        .then((res) => console.log(res))
        .then(() =>
          axios
            .get(`${config.API}/products/1/questions?limit=10`, {
              headers: {
                Authorization: localStorage.getItem("token"),
              },
            })
            .then((res) => (this.QA_list = res.data))
        )
        .catch((error) => console.log(error));
    },
  },
  created: function () {
    axios
      .get(`${config.API}/products/${this.$route.params.id}`)
      .then((res) => (this.datas = res.data));
    axios
      .get(`${config.API}/products/1/questions?limit=5`, {
        headers: {
          Authorization: localStorage.getItem("token"),
        },
      })
      .then((res) => (this.QA_list = res.data));

    window.addEventListener("scroll", this.handleScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
};
</script>

<style lang="scss" scoped>
.product-details {
  max-width: 1230px;
  margin: 0 auto;
  padding: 70px 15px;

  .none {
    display: none;
  }

  button {
    &:focus {
      outline: none;
    }
  }

  .product-info {
    .sub-nav {
      position: sticky;
      top: 0;
      display: flex;
      background-color: white;

      a {
        text-decoration: none;
      }

      a,
      li {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 68px;
        font-size: 20px;
        color: #9a9a9e;
        border-bottom: 4px solid #f2f2f2;
      }

      .select-li {
        border-bottom: 4px solid black;
      }
    }

    .main-info {
      text-align: center;

      img {
        margin: 0 auto;
      }
    }

    .wall {
      height: 20px;
      border-left: 1px solid #e1e1e1;
      margin: 0 10px;
    }

    .page-button-container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 46px;
      margin-top: 72px;

      .arrow {
        width: 29px;
      }

      .page-button {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 46px;
        height: 100%;
        font-size: 17px;
        color: #9a9a9e;
        border: 1px solid #e6e6e6;
        margin: 0 5px;

        .is_select {
          color: black;
        }
      }
    }

    .QA-header {
      display: flex;
      justify-content: space-between;
      border-bottom: 1px solid black;
      margin-top: 140px;
      padding-bottom: 16px;

      h2 {
        font-size: 26px;
        font-weight: 500;
      }

      span {
        align-self: flex-end;
        font-size: 22px;
        text-decoration: underline;
      }

      .question {
        display: flex;
        align-items: center;

        span {
          cursor: pointer;
        }

        .my-question {
          cursor: pointer;

          img {
            position: relative;
            bottom: 2px;
            width: 23px;
          }

          span {
            text-decoration: none;
          }
        }
      }
    }

    .question-input {
      padding: 15px;
      background-color: #f7f7f7;

      li {
        display: flex;
        align-items: center;
        border-bottom: 1px solid #e6e6e6;

        div {
          &:first-child {
            width: 16%;
            font-size: 18px;
          }
          &:last-child {
            width: 84%;

            textarea {
              font-size: 18px;
              width: 100%;
              height: 146px;
              border-radius: 10px;
              padding: 16px;
              margin: 20px 0;
              background-color: white;
            }

            img {
              border-radius: 4px;
              background-color: white;
              margin-right: 1%;
            }
          }
          .select-question-list,
          .select-question-container {
            width: 100%;
          }

          .select-question-list-container {
            position: relative;
            width: 100%;
          }

          .select-question {
            width: 100%;
            height: 50px;
            font-size: 16px;
            text-align: start;
            border: 1px solid #e6e6e6;
            padding: 12px 16px;
            background-color: white;
          }

          .select-question-list {
            position: absolute;

            .select-question {
              border-top: 0;

              &:hover {
                background-color: #017ffe;
              }
            }
          }
        }

        &:first-child {
          height: 90px;
        }

        &:nth-last-child(2) {
          height: 65px;
        }

        &:last-child {
          display: flex;
          justify-content: center;
          align-items: center;
          font-size: 19px;
          font-weight: 500;

          button {
            border-radius: 10px;
            width: 15%;
            height: 60px;
            margin: 50px 0;

            &:first-child {
              color: #1e1e1e;
              border: 1px solid #1e1e1e;
              background-color: white;
              margin-right: 1%;
            }

            &:last-child {
              color: white;
              background-color: #1e1e1e;
            }
          }
        }
      }

      .secret-container {
        display: flex;
        align-items: center;
        cursor: pointer;

        img {
          width: 23px;
        }
      }
    }

    .QA-list {
      li {
        display: flex;
        border-bottom: 1px solid #e1e1e1;

        div {
          display: flex;
          justify-content: center;
          align-items: center;
          height: 67px;
          font-size: 18px;

          &:first-child {
            width: 164px;
          }
          &:nth-child(2) {
            width: 152px;
          }
          &:nth-child(3) {
            justify-content: start;
            width: 560px;
            padding: 0 36px;

            label {
              margin: 0;
            }
          }
          &:nth-child(4),
          &:last-child {
            width: 162px;
          }
        }

        &:first-child {
          font-weight: 600;

          .QA-contents {
            justify-content: center;
          }
        }
      }

      .finish,
      .not-yet {
        font-size: 14px;
        border-radius: 13px;
        padding: 2px 4px;
      }

      .finish {
        color: #1e88e5;
        border: 1px solid #1e88e5;
      }

      .not-yet {
        color: #9a9a9e;
        border: 1px solid #9a9a9e;
      }
    }
  }
}
</style>
