<template>
  <div class="address-modal-bg">
    <div class="address-modal-container">
      <div class="header" v-if="addTab === false">
        <span>배송지 변경</span>
        <button @click="$store.state.showModal = false"><img alt="close" src="https://www.brandi.co.kr/static/2020.7.3/images/ic-popup-exit.png" /></button>
        </div>
      <div class="header" v-else><span>배송지 추가</span>
      <button @click="$store.state.showModal = false"><img alt="close" src="https://www.brandi.co.kr/static/2020.7.3/images/ic-popup-exit.png" /></button>
      </div>
      <div class="contents" v-if="addTab === false">
        <div class="list">
          <div v-if="this.$store.state.showAddressInfo.length > 0">
          <ul class="address-card" v-for="item in $store.state.showAddressInfo" :key="Object.keys(item).value">
            <li>
              <div class="name">{{item.name}}</div>
              <div class="address">{{item.address}}</div>
              <div class="detail-address">{{item.detail_address}}</div>
              <div class="phone">{{item.phone_number}}</div>
              <div class="btn-list">
                <div class="left">
                  <button class="delete-btn" @click="deleteAddressData({item})">삭제</button>
                  <button class="modify-btn" @click="modifyTab = true">수정</button>
                </div>
                <div class="right">
                  <button class="choose-btn" @click="pasteAddressData({item})">선택</button>
                </div>
              </div>
            </li>
            </ul>
            </div>
            <div v-else>
              저장된 배송지가 없습니다
            </div>
        </div>
      </div>
      <div class="contents" v-else>
        <span class="address-input-wrap">
          <div class="name-row">
            <span class="name">수령인</span>
            <span class="name-input"
              ><input v-model="addressList.name" type="text" placeholder="이름"
            /></span>
          </div>
          <div class="phone-row">
            <span class="phone">휴대폰</span>
            <span class="phone-input"
              ><div class="phone-wrap">
                <input type="number" v-model="addressList.phone1" /> &nbsp;<input type="number" v-model="addressList.phone2" />&nbsp;<input
                  type="number" v-model="addressList.phone3"
                />&nbsp;
              </div></span
            >
          </div>
          <div class="address-row">
            <span class="address">배송주소</span>
            <span class="address-input">
              <div class="address-wrap-top">
                <input v-model="addressList.address.zonecode" disabled class="postal-code" type="text" />&nbsp;<button
                  class="find-postcode"
                  type="button"
                  @click="switchDaumAddressModal"
                >
                  우편번호 찾기
                </button>
              </div>
              <div class="address-wrap-mid">
                <vue-daum-postcode
                  v-if="this.showDaumAddressModal === true"
                  @complete="addressList.address = $event"
                />
                <button class="close-btn" type="button" />
              </div>
              <div class="address-wrap-bottom">
                <input v-model="addressList.address.address" disabled class="address-city" type="text" />
                <input v-model="addressList.address_detail" class="address-detail" type="text" placeholder="상세 주소를 입력하세요"/>
              </div>
            </span>
          </div>
        </span>
      </div>
      <div class="footer" v-if="addTab === false">
        <button class="add-address-btn" @click="addTab = true">
          배송지 추가
        </button>
      </div>
      <div class="footer" v-else>
        <button class="cancel-btn" @click="addTab = false">취소</button>
        <button class="complete-btn" @click="pushAddressData">완료</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {config} from "../../api/apiConfig"
import VueDaumPostcode from "vue-daum-postcode";

export default {
  data: () => ({
    addTab: false,
    modifyTab: false,
    showDaumAddressModal: false,
    addressList: {
      name: "",
      phone1: "",
      phone2: "",
      phone3: "",
      address: "",
      address_detail: "",
    }
  }),
  created() {
    const accessToken = this.$cookies.get('accesstoken')
      const headers = {
        headers: { Authorization: accessToken },
      };
        axios
        .get(`${config.API}shipping-information`, headers)
        .then((res) => (this.$store.state.showAddressInfo = res.data));
        },
  updated() {
  },
  methods: {
    updateData() {
      const accessToken = this.$cookies.get('accesstoken')
      const headers = {
        headers: { Authorization: accessToken },
      };
        axios
        .get(`${config.API}shipping-information`, headers)
        .then((res) => (this.$store.state.showAddressInfo = res.data));
    },
    switchDaumAddressModal() {
      if (!this.showDaumAddressModal) {
        this.showDaumAddressModal = true;
      } else {
        this.showDaumAddressModal = false;
      }
    },
    pushAddressData() {
      this.addTab = false
      const accessToken = this.$cookies.get('accesstoken')
      const headers = {
        headers: { Authorization: accessToken },
      };
      const list = {
        name: this.addressList.name,
        phone_number:
          this.addressList.phone1 +
          "-" +
          this.addressList.phone2 +
          "-" +
          this.addressList.phone3,
        zip_code: this.addressList.address.zonecode,
        address: this.addressList.address.address,
        detail_address: this.addressList.address_detail,
      };
      axios
        .post(`${config.API}shipping-information`, list, headers)
        .then(reponese => this.updateData())
    },
    pasteAddressData(data) {
      const phoneNum = data.item.phone_number 
        this.$store.state.shipList.name = data.item.name;
        this.$store.state.shipList.address.zonecode = data.item.zip_code;
        this.$store.state.shipList.address.address = data.item.address;
        this.$store.state.shipList.address_detail = data.item.detail_address;
        this.$store.state.shipList.phone1 = phoneNum.slice(0, 3);
        this.$store.state.shipList.phone2 = phoneNum.slice(4, 8);
        this.$store.state.shipList.phone3 = phoneNum.slice(9, 13);
        this.$store.state.showModal = false
        // console.log(`${this.$store.state.shipList.phone1}-${this.$store.state.shipList.phone2}-${this.$store.state.shipList.phone3}`);
    },
    deleteAddressData(data) {
      this.addTab = false
      const accessToken = this.$cookies.get('accesstoken')
      const headers = {
        headers: { Authorization: accessToken },
      };
      axios
        .delete(`${config.API}shipping-information?id=${data.item.id}`, headers)
        .then(reponese => this.updateData())
        
    },
    modifyAddressData() {
      this.addTab = false
      const accessToken = this.$cookies.get('accesstoken')
      const headers = {
        headers: { Authorization: accessToken },
      };
      const list = {
        name: this.addressList.name,
        phone_number:
          this.addressList.phone1 +
          "-" +
          this.addressList.phone2 +
          "-" +
          this.addressList.phone3,
        zip_code: this.addressList.address.zonecode,
        address: this.addressList.address.address,
        detail_address: this.addressList.address_detail,
      };
      axios
        .post(`${config.API}shipping-information`, list, headers)
        .then((response) => {

        });
    },
  },
};
</script>

<style lang="scss" scoped>
.address-modal-bg {
  background-color: rgba(0, 0, 0, 0.7);
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 99999;
  .address-modal-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
    display: flex;
    flex-direction: column;
    padding: 20px 0 20px 0;
    background-color: white;
    .header {
      display: flex;
      justify-content: space-between;
      padding: 0 15px 15px 15px;
      font-size: 1.6em;
      font-weight: bold;
      border-bottom: 1px solid #e1e1e1;
    }
    .contents {
      width: 500px;
      max-height: 702px;
      overflow: scroll;
      .list {
        padding: 20px;
        ul {
          display: flex;
          justify-content: center;
          margin: 5px 0 5px 0;
        }
        li {
          width: 436px;
          height: 267px;
          margin: 0;
          padding: 25px;
          border: 1px solid #bdbdbd;
          border-radius: 4px;
          .name {
            font-size: 1.5em;
            font-weight: bold;
            line-height: 60px;
          }
          .address, .detail-address, .phone {
            font-size: 1em;
          }
          .btn-list {
            display: flex;
            justify-content: space-between;
            margin-top: 25px;
            .delete-btn, .modify-btn {
              width: 73px;
              padding: 8px;
              border: 1px solid #bdbdbd;
              border-radius: 4px;
            }
            .choose-btn {
              width: 73px;
              padding: 8px;
              border: 1px solid #bdbdbd;
              border-radius: 4px;
              color: white;
              background-color: black;
            }
          }
        }
      }
      .address-input-wrap {
        padding: 15px;
        input {
          width: 90%;
          height: 42px;
          padding: 5px;
          border: 1px solid #bdbdbd;
          border-radius: 4px;
          font-size: 0.9em;
          text-indent: 8px;
        }
        span {
          margin: auto 0;
          padding: 5px;
        }
        .name-row,
        .phone-row {
          display: flex;
          justify-content: space-between;
          .name, .phone {
            width: 100px;
            font-weight: bold;
            text-align: center;
          }
          .name-input {
            width: 100%;
            input {
              width: 90%;
              height: 42px;
            }
          }
          .phone-input {
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            width: 100%;
            text-indent: 0;
            input {
              width: 100px;
              height: 42px;
              text-align: center;
            }
          }
        }
        .address-row {
          display: flex;
          justify-content: end;
          .address {
            width: 100px;
            font-weight: bold;
            text-align: center;
          }
          .vue-daum-postcode {
            margin: 6px 20px 0 0;
            border: 1px solid black;
            z-index: 9999;
            .close-btn {
              position: absolute;
              top: 0;
              width: 10px;
              height: 10px;
              background-color: red;
            }
          }
          .address-input {
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            width: 100%;
            input {
              width: 90%;
              height: 42px;
              margin: 4px 0;
            }
            .find-postcode {
              width: 94px;
              height: 42px;
              font-size: 0.8em;
              font-weight: bold;
              border-radius: 4px;
              color: white;
              background-color: black;
            }
          }
        }
        .delivery-row {
          display: flex;
          justify-content: end;
          .delivery {
            width: 221px;
            font-weight: bold;
          }
          .delivery-input {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            width: 968px;
            input,
            select {
              margin: 5px 0;
            }
            .delivery-note {
              width: 105%;
              height: 46px;
              padding: 13px;
              font-size: 0.9em;
              color: #8d8d8d;
              background-image: url("https://web-staging.brandi.co.kr/static/2020.7.3/images/ic-arrow-bl-down@3x.png");
              background-size: 13px;
              background-position: 98% 50%;
              background-color: #f5f5f5;
            }
          }
        }
      }
    }
    .footer {
      margin: auto;
      .add-address-btn {
        width: 436px;
        height: 68px;
        border-radius: 5px;
        color: white;
        background-color: black;
      }
      .cancel-btn {
        width: 213px;
        height: 68px;
        border-radius: 5px;
        color: white;
        background-color: #9e9e9e;
      }
      .complete-btn {
        width: 213px;
        height: 68px;
        border-radius: 5px;
        color: white;
        background-color: black;
      }
    }
  }
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
