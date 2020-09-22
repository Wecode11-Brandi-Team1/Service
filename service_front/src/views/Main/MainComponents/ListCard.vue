<template>
  <div id="ListCard">
    <a href="?">
      <ul>
        <li>
          <img
            alt="product photo"
            src="http://image.brandi.me/cproduct/2020/08/27/17865870_1598496166_image1_M.jpg"
          />
        </li>
        <li class="listSeller">
          냥냥 마켓
          <img alt="One day delivery" src="src/assets/oneday.png" />
        </li>
        <li class="productName">안경냥이</li>
        <li>
          <span class="discount">9%</span>
          <span class="price">90</span>
          <span class="originPrice">100</span>
        </li>
        <li class="listCount">5억개 구매중</li>
      </ul>
    </a>
  </div>
</template>

<script>
export default {
  name: "listCard",
  components: {},
  data: () => ({}),
  methods: {},
};
</script>

<style lang="scss">
#ListCard {
  width: 248px;
  padding: 0 6.188px 30px;

  img {
    width: 100%;
  }

  a {
    color: inherit;
    text-decoration: none;
  }

  .listSeller {
    display: flex;
    justify-content: space-between;
    font-size: 15.6px;
    color: #4a4a4a;
    margin-top: 8px;

    img {
      width: 50px;
    }
  }

  .productName {
    font-size: 16px;
    font-weight: 500;
  }

  .price,
  .discount {
    font-size: 20px;
    font-weight: 600;
  }

  .discount {
    color: #ff1f4b;
  }

  .originPrice {
    font-size: 15px;
    color: #757575;
    text-decoration: line-through;
  }

  .listCount {
    font-size: 13px;
    margin-top: 10px;
  }
}
</style>