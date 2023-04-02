<script setup lang="ts">
import HeaderComp from './components/HeaderComp.vue';
import BackgroundComp from './components/BackgroundComp.vue';
</script>

<template>
  <div class="top-container">
    <HeaderComp />
    <RouterView />
    <BackgroundComp />
  </div>
</template>

<style scoped lang="less">

.top-container {
  width: 100%;
  height: 100%;
}
</style>