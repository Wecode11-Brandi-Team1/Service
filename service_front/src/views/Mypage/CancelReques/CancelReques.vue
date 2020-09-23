<template>
  <div class="cancel-wrap">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  mounted: function () {
    this.$store.state.myPageShow = false;
  }
}
</script>

<style lang="scss" scoped>
.cancel-wrap{
  padding: 0px 20px;
}

@media screen and (min-width: 769px){
  .cancel-wrap{
    max-width: 1300px;
    margin: 0 auto;
  }
}
</style>