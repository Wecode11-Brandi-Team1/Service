<template>
  <div class="agree-wrap">
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
        <button v-bind:class="isActiveBtn" v-on:click="agreeSubmit">다음</button>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
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
  computed: {
    isAllChecked:{
      get () {
        return this.agreeList.every(function(item){
          return item.checked;
        });
      },
      set(newValue){
        
      }
    },
    
    isActiveBtn() {
      if(this.agreeList[0].checked && this.agreeList[1].checked){
        return {activeBtn: true}
      }else{
        return {activeBtn: false}
      }
    }
  },
  methods : {
    toggleSelect() {
      let select = this.isAllChecked;
      this.agreeList.forEach(function(item) {
        item.checked = !select;
      });
      this.isAllChecked = !select;
    },
    agreeSubmit(){
      if(this.agreeList[0].checked && this.agreeList[1].checked){
        this.$router.push({path: '/signup/info'})
      }else{
        alert('약관에 동의해주세요.')
      }
    }
  },
  mounted:function(){
    this.$store.state.signUpTabName = this.pageName;
  }
}
</script>


<style lang='scss' scoped>
.agree-wrap{
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  
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
@media screen and (min-width: 769px){
  .join-container {
    max-width: 1300px;
    margin: 0 auto;
  }
}

@media screen and (max-width: 400px){
  .join-container {
    max-width: 400px;
    padding-top: 10px;
    margin: 0 auto;

    .agree-list-wrap{
      .all-check{
        label{
          font-size: 14px;
          font-weight: bold;
        }
      }

      .agree-detail{
        .detail-list{
          ul{
            li{
              align-items: inherit !important;
          
              label{
                font-size: 13.2px;
              }

              input[type=checkbox] + label:before {
                margin-right: 5px !important;
            }
          }
        }
      }
    }

    .button-wrap{
      button{
        width: 278px !important;
        height: 50px !important;
        font-size: 16px !important;
        line-height: 46px !important;
      }
    }
  }
}
}
</style>