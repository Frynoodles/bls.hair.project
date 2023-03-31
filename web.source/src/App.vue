<script setup lang="ts">
import HeaderComp from './components/HeaderComp.vue';
</script>

<template>
  <HeaderComp />
  <RouterView />
</template>

<style scoped lang="less">
body {
  background-color: black;
}
</style>