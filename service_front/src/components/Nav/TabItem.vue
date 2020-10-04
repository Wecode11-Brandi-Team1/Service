<template>
  <span @click="test" @mouseover="$emit('input', id)" :class="[active, 'tab']">
    {{ label }}
  </span>
</template>

<script>
export default {
  data() {
    return {};
  },
  props: {
    id: Number,
    label: String,
    value: Number,
  },
  computed: {
    active() {
      // return this.value === this.id ? "active" : false;
    },
  },
  methods: {
    test() {
      if (this.id === 0) {
        this.value = this.id;
        this.$router.push("main");
        console.log(this.value);
      } else if (this.id === 1) {
        console.log(this.value);
      } else if (this.id === 2) {
        console.log(this.value);
      } else if (this.id === 3) {
        console.log(this.value);
      } else if (this.id === 4) {
        console.log(this.value);
      } else if (this.id === 5) {
        console.log(this.value);
      } else if (this.id === 6) {
        console.log(this.value);
      } else if (this.id === 7) {
        console.log(this.value);
      } else if (this.id === 8) {
        console.log(this.value);
      }
    },
  },
};
</script>

<style lang="scss">
.tab {
  width: 137px;
  padding: 20px;
  outline: none;

  cursor: pointer;
}
.tab:hover {
  color: #ff1f4b;
  &:nth-child(n + 4):nth-child(-n + 6) {
    border-bottom: 2px solid #ff1f4b;
  }
}
.active {
  border-bottom: 2px solid #ff1f4b;
}
</style>
