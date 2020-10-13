<template>
  <div class="footer-box">
    <div class="division">
      <ul class="info-cs">
        <li class="cs">고객센터 1566-6575</li>
        <li class="cs-sub">영업시간 : AM 10:00 ~ PM 17:00 (주말 및 공휴일 휴무)</li>
        <li class="cs-sub">점심시간 : PM 12:30 ~ PM 13:30</li>
        </ul>
        <ul class="link-sns">
          <li><img alt="" src="https://web-staging.brandi.co.kr/static/20.08.01/images/icon_footer_01.png" width="28px" /><a>자주 묻는 질문</a></li>
          <li><img alt="" src="https://web-staging.brandi.co.kr/static/20.08.01/images/icon_footer_02.png" width="28px" /><a>카톡 플러스 친구</a></li>
          <li><img alt="" src="https://web-staging.brandi.co.kr/static/20.08.01/images/icon_footer_03.png" width="28px" /><a>페이스북</a></li>
          <li><img alt="" src="https://web-staging.brandi.co.kr/static/20.08.01/images/icon_footer_04.png" width="28px" /><a>인스타그램</a></li>
        </ul>
    </div>
    <div class="line-division"></div>
    <div class="division">
      <div class="company">
        <ul class="info">
          <li>회사명 : ㈜브랜디 | 대표이사 : 서정민 | 사업자등록번호 : 220-88-93187 | 통신판매업신고 : 2016-서울강남-00359 | 호스팅사업자 : (주)브랜디</li>
          <li>주소 : (06223) 서울특별시 강남구 테헤란로 32길 26 청송빌딩</li>
          <li>개인정보관리책임자 : 윤석호(privacy@brandi.co.kr)</li>
          <li>브랜디는 통신판매중개자로서 통신판매 당사자가 아니며, 판매자가 등록한 상품정보 및 거래에 브랜디는 책임을 지지 않습니다.</li>
        </ul>
        <ul class="link-company">
          <li>이용약관</li>
          <li class="border">|</li>
          <li class="bold">개인정보처리방침</li>
          <li class="border">|</li>
          <li>사업자정보확인</li>
        </ul>
      </div>
      <ul class="link-sns">
        <li><img alt="" src="https://web-staging.brandi.co.kr/static/20.08.01/images/icon_footer_05.png" width="28px" />셀러어드민</li>
        <li><img alt="" src="https://web-staging.brandi.co.kr/static/20.08.01/images/icon_footer_06.png" width="28px" />입점문의</li>
        <li><img alt="" src="https://web-staging.brandi.co.kr/static/20.08.01/images/escrow.png" width="48px" /></li>
        </ul>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
  .footer-box {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    max-width: 100%;
    height: 363px;
    margin-top: 50px;
    color: white;
    background-color: #1e1e1e;
    .division {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      margin: 0 auto;
      width: 1240px;
      .info-cs {
        .cs {
        font-size: 2.1em;
        font-weight: bold;
        cursor: pointer;
        }
        .cs-sub {
          font-size: 0.9em;
          opacity: 0.56;
        }
      }
      .link-sns {
        display: flex;
        li {
          margin-left: 10px;
        }
        a {
          cursor: pointer;
        }
        img {
          margin-right: 6px;
        }
      }
      .company {
          font-size: 0.9em;
          .info {
            opacity: 0.56;
            line-height: 1.2;
          }
          .link-company {
            display: flex;
            cursor: pointer;
            .border {
              margin: 0 10px 0 10px;
              }
              .bold {
                font-weight: bold;
                }
          }
      }
    }
    .line-division {
      width: 1240px;
      height: 1px;
      margin: 0 auto;
      border-top: 1px solid #333;
    }
  }
</style>
