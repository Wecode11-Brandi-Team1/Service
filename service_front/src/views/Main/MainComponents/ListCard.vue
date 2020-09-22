<template>
  <ul class="list-card">
    <li>
      <img class="product-photo" alt="product photo" v-bind:src="src" />
    </li>
    <li class="list-seller">
      {{seller_name}}
      <img
        v-bind:class="{'none':one_day_delivery}"
        alt="One day delivery"
        src="src/assets/oneday.png"
      />
    </li>
    <li class="product-name">{{product_name}}</li>
    <li>
      <span v-bind:class="{'discount':discount,'none':!discount}">{{discount}}%</span>
      <span class="price">{{origin_price*(1-discount/100)}}</span>
      <span v-bind:class="{'origin-price':discount,'none':!discount}">{{origin_price}}</span>
    </li>
    <li v-bind:class="{'list-count':list_count, 'none':!list_count}">{{list_count}}개 구매중</li>
  </ul>
</template>

<script>
export default {
  name: "list-card",
  components: {},
  props: [
    "id",
    "src",
    "seller_name",
    "product_name",
    "discount",
    "origin_price",
    "list_count",
    "one_day_delivery",
  ],
  data: () => ({}),
  methods: {},
};
</script>

<style lang="scss">
.list-card {
  width: 248px;
  padding: 0 6.188px 30px;

  .none {
    display: none;
  }

  .product-photo {
    width: 100%;
    height: 254px;
  }

  .list-seller {
    display: flex;
    justify-content: space-between;
    font-size: 15.6px;
    color: #4a4a4a;
    margin-top: 8px;

    img {
      width: 50px;
    }
  }

  .product-name {
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

  .origin-price {
    font-size: 15px;
    color: #757575;
    text-decoration: line-through;
  }

  .list-count {
    font-size: 13px;
    margin-top: 10px;
  }
}
</style>