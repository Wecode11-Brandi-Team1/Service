# 위코드 기업협업 브랜디 과제 소개
위코드 부트캠프 11기 브랜디 기업협업 과제로 진행한 [BRANDI](https://www.brandi.co.kr) 웹사이트 클론 입니다.

## 개발 인원 및 기간
### 개발 인원
* 프론트엔드 3명: [류상욱](https://github.com/ryuinkyoto), [이효정](https://github.com/ovovv), [한태규](https://github.com/recurian1058)
* 백엔드 2명: [김기욱](https://github.com/keywookkim), [김태하](https://github.com/taeha7b)

### 개발 기간
* 2020/09/14 ~ 2020/10/15

## 프로젝트 목적
패션 커머스 기업 브랜디 웹사이트를 클론함으로써 모델링과 회원가입, 소셜 로그인, 상품 구매와 같은 핵심 기능을 구현하고,
각자의 개발 역량을 기르고자 한다.

## 적용 기술 및 구현된 기능
### 적용 기술 - 백엔드
* Python, Flaks web framework
* Bcrypt
* JWT
* MySQL
* AWS EC2, RDS

### 구현된 기능 - 백엔드
* Bcrypt를 활용한 비밀번호 암호화
* JWT를 활용한 로그인 토큰 발행
* 회원가입시 정규식을 사용한 회원정보 유효성 검사
* Q&A 작성
* 상품 구매, 취소, 환불

### 적용 기술 - 프론트엔드
* HTML, CSS
* JS
* Vue(Vue router, Vue Webpack, Vuex)
* SASS
* Vuetify

### 구현된 기능 - 프론트엔드
* JWT와 cookies를 이용하여 로그인 기능 구현
* 구글 토큰 발행을 활용하여 소셜로그인 및 회원가입 구현
* v-if를 활용하여 구글소셜회원가입 / 기본회원가입을 한페이지 내에서 구현
* 마이페이지 상품조회에서 데이터베이스에 저장된 상태값에 따라 환불, 취소 기능 구현
* API 통신을 통해 해당 계정이 작성한 Q&A 게시글 불러오기
* API 통신을 통해 해당 계정이 받은 쿠폰 불러오기
* media query를 이용하여 모바일 페이지 반응형 레이아웃 구현
