<template>
  <ul class="list-card">
    <li>
      <img class="product-photo" alt="product photo" v-bind:src="image_path" />
    </li>
    <li class="list-seller">{{ seller_name }}</li>
    <li class="product-name">
      <p>{{ product_name }}</p>
    </li>
    <li>
      <span v-bind:class="{ discount: discount_rate, none: !discount_rate }"
        >{{ discount_rate }}%</span
      >
      <span class="price">{{
        Number(sale_price * (1 - discount_rate / 100)).toLocaleString("en")
      }}</span>
      <span
        v-bind:class="{ 'origin-price': discount_rate, none: !discount_rate }"
      >
        {{ Number(sale_price).toLocaleString("en") }}
      </span>
    </li>
    <li v-bind:class="{ 'list-count': sale_amount, none: !sale_amount }">
      {{ Number(sale_amount).toLocaleString("en") }}개 구매중
    </li>
  </ul>
</template>

<script>
export default {
  name: "list-card",
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
.list-card {
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
