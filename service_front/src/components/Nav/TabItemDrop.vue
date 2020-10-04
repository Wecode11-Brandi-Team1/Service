<template>
  <div class="category-bg">
    <div class="category-wrap" v-if="this.currentId === 3">
      <ul>
        <div class="border" />
        <li>
          <div class="border" />
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import DropDown from "./DropDown.vue";
export default {
  components: { DropDown },
  props: { currentId: 0 },
  data() {
    return {
      categoryList: [],
    };
  },
  created: function () {
    axios
      .get("http://10.58.2.209:5000/category?q=1")
      .then((res) => (this.categoryList = res.data))
      .catch();
  },
};
</script>

<style lang="scss">
.category-bg {
  position: absolute;
  top: 182;
  display: flex;
  justify-content: center;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.96);
  box-shadow: 0 3px 5px 2px rgba(0, 0, 0, 0.3);
  .category-wrap {
    ul {
      display: flex;
      justify-content: space-around;
    }
    li {
      display: flex;
      flex-direction: column;
      padding: 10px 20px 20px 20px;
      overflow: hidden;
    }
    a {
      width: 180px;
      color: #737373;
    }
    .header {
      font-weight: bold;
      line-height: 2.5;
      color: black;
    }
    .border {
      width: 1px;
      background-color: #e1e1e1;
    }
  }
}
</style>
