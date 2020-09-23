<template>
  <div id="app">
    <div
      v-if="loading"
      style="
        width: 100%;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 10000;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: rgba(0,0,0,0.5);
        transition: all 0.3s;
      "
    >
      <div>
        <img src="https://web-staging.brandi.co.kr/static/2020.7.3/images/ico_loading.png" />
      </div>
    </div>
    <router-view :key="$route.fullPath"></router-view>
  </div>
</template>

<script>
export default {
  name: "app",
  data: () => ({
    loading: true,
  }),
  created() {
    setTimeout(() => {
      this.loading = false;
    }, 2000);
  },
};
</script>
