<template>
  <div class="refund-wrap">
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
.refund-wrap{
  padding: 0px 20px;
}

@media screen and (min-width: 769px){
  .refund-wrap{
    max-width: 1300px;
    margin: 0 auto;
  }
}
</style>