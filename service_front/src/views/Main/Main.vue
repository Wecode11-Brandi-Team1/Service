<template>
  <div id="Main">
    <header id="rollingBannerContainer">
      <a href="?">
        <img
          alt="rollingBanner"
          src="http://image.brandi.me/home/banner/bannerImage_159982_1593396258.jpg"
        />
      </a>
      <div id="slideButton">
        <div class="spot" href="?"></div>
      </div>
    </header>
    <main id="mainListContainer">
      <div id="mainPageTittle">
        <span>당신을 위한 추천</span>
      </div>
      <div class="MainList">
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
      </div>
      <div class="mainSubBanner">
        <a href="?">
          <img
            alt="Banner photo"
            src="http://image.brandi.me/home/banner/bannerImage_159429_1593395957.jpg"
          />
        </a>
      </div>
      <div class="MainList">
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
      </div>
      <div class="mainSubBanner">
        <a href="?">
          <img
            alt="Banner photo"
            src="http://image.brandi.me/home/banner/bannerImage_159375_1593395565.jpg"
          />
        </a>
      </div>
      <div id="MainListBottom">
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
        <listCard />
      </div>
      <div class="buttonContainer">
        <button class="more">더보기</button>
      </div>
    </main>
  </div>
</template>

<script>
import listCard from "./MainComponents/ListCard.vue";

export default {
  name: "main",
  components: { listCard },
  data: () => ({}),
  methods: {},
};
</script>

<style lang="scss">
#main {
  display: flex;
  flex-direction: column;
  width: 100vw;
  box-sizing: border-box;

  #rollingBannerContainer {
    position: relative;
    margin-bottom: 30px;
    padding-bottom: 24px;

    img {
      max-width: 100%;
      background-color: black;
    }

    #slideButton {
      position: absolute;
      display: flex;
      justify-content: center;
      align-items: flex-end;
      bottom: 0;
      width: 100%;
      height: 19px;

      .spot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: black;
        cursor: pointer;
      }
    }
  }

  #mainListContainer {
    display: flex;
    flex-direction: column;
    width: 1300px;
    padding: 0 30px;
    margin: auto;

    .MainList,
    #MainListBottom {
      display: flex;
      flex-wrap: wrap;
    }
  }

  #mainPageTittle {
    display: flex;
    justify-content: center;
    margin-bottom: 30px;
    padding-top: 40px;
    span {
      font-size: 26px;
      font-weight: 700;
    }
  }

  .mainSubBanner {
    height: 313.3px;
    margin-top: 50px;
    margin-bottom: 80px;

    img {
      width: 100%;
      height: 313.3;
      padding: 0 6.1875px;
    }
  }

  .buttonContainer {
    display: flex;
    justify-content: center;
    height: 82px;
    padding: 20px 0;

    .more {
      width: 250px;
      border: 1px solid black;
      font-size: 14px;

      &:focus {
        border: inherit;
      }
    }
  }
}
</style>