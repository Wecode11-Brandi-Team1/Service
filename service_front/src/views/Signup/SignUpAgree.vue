<template>
  <div class="agree-wrap">
    <div class="page-title">
      <h1>회원가입</h1>
    </div>
    <signUpTab v-bind:propsdata="pageName"></signUpTab>
    <div class="join-container">
      <h1>가입 약관 동의</h1>
      <div class="agree-list-wrap">
        <div class="all-check">
          <input type="checkbox" id="agree-all" @click="toggleSelect" :checked="isAllChecked">
          <label for="agree-all">모두동의</label>
        </div>
        <div class="agree-detail">
          <div class="detail-list">
            <ul>
              <li v-for="item in agreeList" v-bind:key="item.id">
                <div>
                  <input type="checkbox" v-model="item.checked" v-bind:id="item.id">
                  <label v-bind:for="item.id">{{ item.name }} <span>{{ item.importance }}</span></label>
                </div>
                <a>내용보기</a>
              </li>
            </ul>
        </div>
      </div>
      <div class="button-wrap">
        <button v-bind:class="isActivBtn" v-on:click="agreeSubmit">다음</button>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import signUpTab from '../../components/signUpComponent/signUpTab.vue'; 

export default {
  components: {
    signUpTab
  },
  data:()=>({
    pageName:'agree',
    agreeList: [ 
      { id: 1, name: '브랜디 약관 동의', importance: '(필수)', checked: false}, 
      { id: 2, name: '개인정보수집 및 이용에 대한 안내', importance: '(필수)', checked: false}, 
      { id: 3, name: '이벤트/마케팅 수신 동의', importance: '(선택)', checked: false}, 
      { id: 4, name: '야간 혜택 알림 수신 동의', importance: '(선택)', checked: false}, 
    ],
    selected: [],
    selectAll: false,
    activeBtn: false,
  }),
  props:['propsdata'],
  computed: {
    isAllChecked: function() {
      return this.agreeList.every(function(item){
        return item.checked;
      });
    },
    
    isActivBtn: function () {
      if(this.agreeList[0].checked && this.agreeList[1].checked){
        return {activeBtn: true}
      }else{
        return {activeBtn: false}
      }
    }
  },
  methods : {
    toggleSelect: function() {
      let select = this.isAllChecked;
      this.agreeList.forEach(function(item) {
        item.checked = !select;
      });
      this.isAllChecked = !select;
    },

    agreeSubmit: function(){
      if(this.agreeList[0].checked && this.agreeList[1].checked){
        this.$router.push({path: '/signup/info'})
      }else{
        alert('약관에 동의해주세요.')
      }
    }
  }
}

</script>


<style lang='scss' scoped>
.agree-wrap{
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;

  .page-title{
    margin-bottom: 30px;
    padding: 0 20px;

    h1{
      font-size: 28px;
      text-align: center;
      margin-bottom: 15px;
    }
  }

  .join-container{
    width: 100%;
    max-width: 600px;
    text-align: left;
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin: 10px auto;
    padding: 16px;

    h1{
      font-size: 16px;
      font-weight: bold;
      margin: 24px 0;
    }

    .agree-list-wrap{
      border-top: 1px solid #e1e1e1;
      border-bottom: 1px solid #e1e1e1;
      padding: 30px 0;

      .all-check{
        label{
          font-size: 16px;
          margin-bottom: 16px;
          cursor: pointer;
        }

        input[type=checkbox] + label:before {
          content: '';
          width: 20px;
          height: 20px;
          position: relative;
          top: -2px;
          display: inline-block;
          background: url("https://web-staging.brandi.co.kr/static/3.50.7/images/f-market-icon-checkbox-m-n.png") round;
          vertical-align: middle;
          margin-right: 15px;
          cursor: pointer;
        }

        input[type=checkbox]:checked + label:before {
	        content: '';
          background: url("https://web-staging.brandi.co.kr/static/3.50.7/images/f-market-icon-checkbox-m-s.png") round;
        }

        input[type=checkbox] {
	        display: none;
        }
      }

      .agree-detail{
        border: 1px solid #e1e1e1;
        padding: 24px 18px;

        .detail-list{
          display: flex;
          justify-content: space-between;
          align-items: center;

          ul{
            width: 100%;
            margin-bottom: 0;
            
            li{
              display: flex;
              justify-content: space-between;
              align-items: center;

              label{
                margin-bottom: 12px;
                cursor: pointer;
              
                span{
                  color: #FF204B;
                }
              }

              input[type=checkbox] + label:before {
                content: '';
                width: 20px;
                height: 20px;
                position: relative;
                top: -2px;
                display: inline-block;
                background: url("https://web-staging.brandi.co.kr/static/3.50.7/images/f-market-icon-checkbox-m-n.png") round;
                vertical-align: middle;
                margin-right: 15px;
                cursor: pointer;
              }

              input[type=checkbox]:checked + label:before {
	              content: '';
                background: url("https://web-staging.brandi.co.kr/static/3.50.7/images/f-market-icon-checkbox-m-s.png") round;
              }

              input[type=checkbox] {
	              display: none;
              }

              a{
                font-size: 13px;
                color: #616161;
                cursor: pointer;

                &:hover{
                  text-decoration: none;
                }
              }
             }
          }
        }
      }

    .button-wrap{
      display: flex;
      justify-content: center;
      margin: 30px auto 2px auto;

      button{
        width: 200px;
        height: 60px;
        font-size: 19px;
        line-height: 63px;
        color: #fff;
        background: #9e9e9e;
        border: 1px solid #9e9e9e;
        border-radius: 4px;

        &:focus{
          outline: none;
        }
      }

      .activeBtn{
        background: #000;
        border: 1px solid #000;
      }
    }
  }
}
}
</style>