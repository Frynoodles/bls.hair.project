<script setup lang="ts">
// TODO 之后要根据后端来动态获取背景
let background_img_index = 'background-' + '1'
</script>
<template>
    <div class="background-wallpaper">
    </div>
</template>

<style scoped lang="less">
.background-wallpaper {
    position: absolute;
    top: 0%;
    margin: 0%;
    padding: 0%;
    height: 100%;
    width: 100%;
    z-index: -1;
    background-image: url('../assets/img/background-img/background-1.jpg');
    background-size: auto 100%;
}
</style>