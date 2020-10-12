<template>
  <div class="mypage-wrap">
    <div class="page-box">
      <div class="qna-box">
        <h2>상품 Q&A</h2>
          <div class="qna-list">
            <!-- <dl class="qna-no-data">
              <dd>Q&A 내역이 존재하지 않습니다.</dd>
            </dl> -->
            <dl class="list-header">
              <dt>답변상태</dt>
              <dt>내용</dt>
              <dt>작성자</dt>
              <dt>작성일</dt>
            </dl>
            <dl class="qna_question">
              <dd>미답변</dd>
              <dd>테스트테스트콘푸라이크냠냠</dd>
              <dd></dd>
              <dd>2020.09.24</dd>
            </dl>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data:() => ({
    pageName:'qna',
    mobilePageName:'상품 Q&A'
  }),
  mounted: function () {
    this.$store.state.myPageTabName = this.pageName;
    this.$store.state.myPageShow = true;
    this.$store.state.mobilePageName = this.mobilePageName;
  }
}
</script>

<style lang="scss" scoped>
.mypage-wrap{
  .page-box{
    width: 100%;
    padding: 0px 20px;
    margin: 0px auto;

    .qna-box{
      h2{
        font-size: 26px;
        font-weight: 400;
        border-bottom: 1px solid #000;
        padding-bottom: 10px;
        margin: 0;
        margin-top: 50px;
      }

      .qna-list{
        width: 100%;
        display: table;

        .order-no-data{
          display: none !important;
        }

        dl{
          width: 100%;
          display: table-row;
        }

        dd{
          text-align: center;
          font-size: 16px;
          color: #1e1e1e;
          padding: 50px 0 0 0;
          display: table-cell;
          vertical-align: middle;
          border-bottom: 1px solid #e1e1e1;
          padding: 10px;
        }
      
        .list-header{
          width: 100%;
          display: table-row;
          border-bottom: 1px solid #ddd;
          overflow: hidden;

          dt{
            font-size: 16px;
            text-align: center;
            font-weight: bold;
            display: table-cell;
            vertical-align: middle;
            padding: 10px;
            padding-bottom: 10px;
            border-bottom: 1px solid #ccc;

            &:first-child{
              width: 15%;
              text-align: center;
            }
          }
        }

      }
    }
  }
}

@media screen and (min-width: 769px){
  .mypage-wrap {
    max-width: 1300px;
    margin: 0 auto;
  }
}

@media screen and (max-width: 400px){
  .mypage-wrap {
    max-width: 400px;
    margin: 0 auto;
    margin-top: 75px;

    .qna-box{
      h2{
        display: none;
      }

      .qna-list{
        .list-header{
          display: none !important;
        }
        
        .qna_question{
          border-top: 1px solid #000;
          display: flex !important;
          flex-direction: column;
          
          dd{
            width: 100%;
            display: block !important;
            margin-bottom: 0px;

            &:first-child{
              text-align: left;
              font-weight: 700;
              border-bottom: none;
            }

            &:nth-child(2){
              text-align: left;
              font-size: 15px;
              text-overflow: ellipsis;
              white-space: nowrap;
              border-bottom: none;
            }

            &:nth-child(3){
              padding: 0;
              border-bottom: none;
            }

            &:nth-child(4){
              text-align: right;
            }
          }
        }
      }
    }
  }
}
</style>