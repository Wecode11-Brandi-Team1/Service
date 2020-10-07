<template>
  <span
    @mouseover="isHover"
    @click="isClick"
    :class="[checkHover, checkActive, checkDrop, 'tab']"
  >
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
    label: "",
  },
  computed: {
    checkHover() {
      if (this.id === 3 || this.id === 4 || this.id === 5) {
        return this.$store.state.menutab.currentHover === this.id
          ? "current-hover"
          : false;
      }
    },
    checkActive() {
      return this.$store.state.menutab.activeTab === this.id
        ? "active-tab"
        : false;
    },
    checkDrop() {
      if (
        this.$store.state.menutab.currentHover === 3 ||
        this.$store.state.menutab.currentHover === 4 ||
        this.$store.state.menutab.currentHover === 5
      ) {
        return this.$store.state.menutab.activeTab === this.id ? "test" : false;
      }
    },
  },
  methods: {
    isHover() {
      this.$store.state.menutab.currentHover = this.id;
    },
    isClick() {
      if (this.id === 0) {
        this.$router.push("/");
      } else if (this.id === 7) {
        this.$router.push("/event");
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
.current-hover {
  border-bottom: 2px solid #ff1f4b;
  color: #ff1f4b;
}
.active-tab {
  border-bottom: 2px solid #ff1f4b;
  color: #ff1f4b;
}
.test {
  border-bottom: none;
  color: black;
}
</style>
