<template>
  <div class="orderer-info-wrap">
    <h2 class="orderer-info-title">주문자 정보</h2>
    <div class="orderer-info-table">
      <div class="name-row">
        <span class="name">이름</span>
        <span class="name-input"
          ><input v-model="ordererlist.name" type="text" placeholder="이름"
        /></span>
      </div>
      <div class="phone-row">
        <span class="phone">휴대폰</span>
        <span class="phone-input"
          ><div class="phone-wrap">
            <input
              v-model="ordererlist.phone1"
              type="number"
            />&nbsp;-&nbsp;<input
              v-model="ordererlist.phone2"
              type="number"
            />&nbsp;-&nbsp;<input
              v-model="ordererlist.phone3"
              type="number"
            />&nbsp;&nbsp;<button type="button" class="get-vertify">
              인증번호받기
            </button>
          </div>
          <div class="attention">
            * 주문자의 휴대폰 번호로 본인 인증 후 주문 가능합니다.<br />
            * 비회원 주문 시, 적립금은 지급되지 않습니다.
          </div>
          <div class="vertify-wrap">
            <input
              v-model="ordererlist.vertifynum"
              class="vertify"
              type="number"
              placeholder="인증번호 숫자 6자리"
            />&nbsp;&nbsp;<button class="confirm" type="button">확인</button>
          </div></span
        >
      </div>
      <div class="email-row">
        <span class="email">이메일</span>
        <span class="email-input"
          ><input
            v-model="ordererlist.email1"
            type="email" />&nbsp;@&nbsp;<input
            v-model="ordererlist.email2"
            type="email"
        /></span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["ordererlist"],
};
</script>

<style lang="scss" scoped>
.orderer-info-wrap {
  input {
    padding: 13px;
    color: #8d8d8d;
    background-color: #f5f5f5;
    &::placeholder {
      font-size: 0.9em;
    }
  }
  .orderer-info-title {
    margin-top: 90px;
    padding-bottom: 10px;
    font-size: 1.8em;
    border-bottom: 1px solid black;
  }
  .orderer-info-table {
    border-bottom: 1px solid black;
    span {
      margin: auto 0;
      padding: 15px;
    }
    .name-row,
    .phone-row,
    .email-row {
      display: flex;
      justify-content: end;
      border-bottom: 1px solid #bdbdbd;
      .name {
        width: 221px;
        font-weight: bold;
      }
      .name-input {
        width: 968px;
        input {
          width: 105%;
          height: 42px;
        }
      }
      .phone {
        width: 221px;
        font-weight: bold;
      }
      .phone-input {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        width: 968px;
        height: 190px;
        input {
          width: 80px;
          height: 42px;
          text-align: center;
        }
        button {
          width: 94px;
          height: 42px;
          color: white;
          font-size: 0.8em;
          font-weight: bold;
        }
        .get-vertify {
          background-color: #4c4c4c;
        }
        .confirm {
          background-color: #bdbdbd;
        }
        .attention {
          font-size: 0.85em;
        }
        .vertify {
          width: 238px;
        }
      }
      .email {
        width: 221px;
        font-weight: bold;
      }
      .email-input {
        width: 968px;
        input {
          width: 238px;
          height: 42px;
        }
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
