<template>
  <div :class="{ loader: true, fadeout: !isLoading }">
    <img src ="https://web-staging.brandi.co.kr/static/2020.7.3/images/ico_loading.png" />
    </div>
</template>

<script>
export default { 
  name: "LoadingScreen", 
  props: ["isLoading"] 
};
</script>

<style>
.loader {
  background-color: #1e1e1e;
  bottom: 0;
  color: white;
  display: block;
  font-size: 32px;
  left: 0;
  overflow: hidden;
  padding-top: 10vh;
  position: fixed;
  right: 0;
  text-align: center;
  top: 0;
}

.fadeout {
  animation: fadeout 2s forwards;
}

@keyframes fadeout {
  to {
    opacity: 0;
    visibility: hidden;
  }
}
</style>
