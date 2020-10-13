<template>
  <div class="result-wrap">
    <div class="result-title">
      <h1>주문취소완료</h1>
    </div>
    <div class="result-box">
      <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ico_order_success.jpg" />
      <h1>주문취소가 정상적으로 요청되었습니다.</h1>
    </div>
    <div class="totalpay-wrap">
      <dl class="order-totalpay">
        <dd>주문취소일</dd>
        <dd class="order-rigth">{{ toDayValue }}</dd>
        <dd>주문취소사유</dd>
        <dd class="order-rigth">{{ selectedType }}</dd>
        <dd class="order-totalpay-title">총 주문취소금액</dd>
        <dd class="order-totalpay-title red order-rigth">{{ Number(this.$store.state.cancelTotal).toLocaleString() }}원</dd>
      </dl>
    </div>
    <div class="precautions">
      <strong>주의사항</strong>
      <br/>
      <span>
        네이버페이 환불안내<br/>
        간편 신용카드/체크카드 : 취소 완료 후 3~5영업일 이후 환불(승인/매입 구분 불가)<br/>
        간편 계좌이체 : 취소 완료 즉시 환불(단, 은행 정기점검시간등에는 환불 실패)<br/>
        포인트 : 취소 완료 즉시 환불
      </span>
    </div>
    <div class="btn-wrap">
      <button @click="resultBtn">주문/배송조회로 이동</button>
    </div>
  </div>
</template>

<script>
export default {
  data:() => ({

  }),
  methods:{
    resultBtn(){
      this.$router.push({path: '/mypage'});
    }
  },
  computed:{
    toDayValue(){
      let today = new Date();   
      let year = today.getFullYear();
      let month = today.getMonth() + 1;
      let date = today.getDate();

      return year + '-' + month + '-' + date
    },
    selectedType(){
      if(this.$store.state.cancelSelected == 1){
        return '구매자 취소';
      }else if(this.$store.state.cancelSelected == 2){
        return '구매자 변심';
      }else if(this.$store.state.cancelSelected == 3){
        return '상품 품절';
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.result-wrap{
  padding: 0px 20px;

  .result-title{
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 40px 0px 10px 0px;

    h1{
      font-size: 28px;
      text-align: center;
      color: #1e1e1e;
      margin-bottom: 15px;
    }
  }

  .result-box{
    text-align: center;

    h1{
      text-align: center;
      font-size: 32px;
      font-weight: 400;
      color: #1e1e1e;
      padding: 20px 0;
    }
  }

  .totalpay-wrap{
    margin-top: 50px;

    .order-totalpay{
      font-size: 15px;
      overflow: hidden;
      border-top: 1px solid #000;
      border-bottom: 1px solid #000;
      padding: 20px 0;
      margin-bottom: 50px;
      
      dd{
        width: 50%;
        text-align: left;
        float: left;
        padding: 10px 20px;
      }

      .order-totalpay-title{
        font-size: 26px;
        font-weight: bold;
      }

      .red{
        color: #FF204B;
      }

      .order-rigth{
        text-align: right;
      }
    }
  }

  .precautions{
    line-height: 200%;
    border: 1px solid #ccc;
    padding: 30px;
    margin-bottom: 30px;

    strong{
      font-size: 16.5px;
      color: #1e1e1e;
    }

    span{
      font-size: 13px;
      color: #1e1e1e;
    }
  }

  .btn-wrap{
    display: flex;
    justify-content: center;
    align-items: center;

    button{
      width: 170px;
      height: 50px;
      font-size: 17px;
      text-align: center;
      line-height: 46px;
      color: #ffffff;
      display: block;
      background: #000;
      border: 1px solid #000;
      border-radius: 4px;
      padding: 0;

      &:focus{
        outline: none;
      }
    }
  }
}

@media screen and (min-width: 769px){
  .result-wrap {
    max-width: 1300px;
    margin: 0 auto;
  }
}
</style>