<template>
  <ul class="categories-card">
    <li>
      <img class="product-photo" alt="product photo" v-bind:src="image_path" />
    </li>
    <li class="list-seller">{{ seller_name }}</li>
    <li class="product-name">
      <p>{{ product_name }}</p>
    </li>
    <li>
      <span class="discount-rate" v-if="discount_rate">{{ discount_rate }}%</span>
      <span class="price">{{ Number(sale_price * (1 - discount_rate / 100)).toLocaleString("en") }}</span>
      <span class="origin-price" v-if="discount_rate">{{ Number(sale_price).toLocaleString("en") }}</span>
    </li>
    <li class="sale-amount" v-if="sale_amount">{{ Number(sale_amount).toLocaleString("en") }}개 구매중</li>
  </ul>
</template>

<script>
export default {
  name: "categories-card",
  components: {},
  props: [
    "product_id",
    "image_path",
    "seller_name",
    "product_name",
    "discount_rate",
    "sale_price",
    "sale_amount",
  ],
  data: () => ({}),
  methods: {},
};
</script>

<style lang="scss">
.categories-card {
  width: 248px;
  margin: 0;
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
  }

  .product-name {
    font-size: 16px;
    font-weight: 500;
    p {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      margin: 0;
    }
  }

  .price,
  .discount-rate {
    font-size: 20px;
    font-weight: 600;
  }

  .discount-rate {
    color: #ff1f4b;
  }

  .origin-price {
    font-size: 15px;
    color: #757575;
    text-decoration: line-through;
  }

  .sale-amount {
    font-size: 13px;
    margin-top: 10px;
  }
}
</style>
