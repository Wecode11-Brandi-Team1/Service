<template>
  <div class="result-wrap">
    <div class="result-title">
      <h1>주문완료</h1>
    </div>
    <div class="result-box">
      <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ico_order_success.jpg" />
      <h1>주문이 정상적으로 요청되었습니다.</h1>
    </div>
    <div class="btn-wrap">
      <button @click="resultBtn">주문/배송조회로 이동</button>
    </div>
  </div>
</template>

<script>
export default {
  methods:{
    resultBtn(){
      this.$router.push({path: '/mypage'});
    }
  },
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
    margin: 100px 0 100px 0;

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