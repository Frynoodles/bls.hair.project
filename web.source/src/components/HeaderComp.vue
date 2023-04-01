<script setup lang="ts">
import LogoIcon from './icons/LogoIcon.vue';
import BilibiliIcon from './icons/BilibiliIcon.vue';
import GithubIcon from './icons/GithubIcon.vue';
import SteamIcon from './icons/SteamIcon.vue';
import router from '@/router';
import { ref } from 'vue';

// TODO 为点击头像增加更多动画效果或提示
let click_count: number = 0;
let color_level = ['#00FF00', '#33FF00', '#66FF00', '#99FF00', '#CCFF00',
    '#FFFF00', '#FFCC00', '#FF9900', '#FF6600', '#FF3300']
let border_color = ref(color_level[click_count])
const login = function (): void {
    if (click_count < 9) {
        click_count++;
        border_color.value = color_level[click_count]
    } else {
        router.replace({ path: '/login' });
        click_count = 0;
    }
}

</script>
<template>
    <header class="header">
        <nav class="nav">
            <ul class="nav-list">
                <li>
                    <LogoIcon :iHeight="40" />
                </li>
                <li>
                    <RouterLink to="/">首页</RouterLink>
                    <!-- RouterLink会被渲染成a标签 -->
                </li>
                <li>
                    <RouterLink to="/notes">笔记</RouterLink>
                </li>
                <li>
                    <RouterLink to="/favorites">收藏夹</RouterLink>
                </li>
                <li>
                    <RouterLink to="/toolbox">工具箱</RouterLink>
                </li>
                <li>
                    <RouterLink to="/nav">导航</RouterLink>
                </li>
                <li>
                    <RouterLink to="/storage">黑盘</RouterLink>
                </li>
                <li>
                    <RouterLink to="/about">关于</RouterLink>
                </li>
            </ul>
        </nav>
        <nav>
            <ul class="nav-list">
                <li class="media-icon">
                    <a href="https://space.bilibili.com/29325500">
                        <BilibiliIcon />
                    </a>
                </li>
                <li class="media-icon">
                    <a href="https://github.com/Frynoodles">
                        <GithubIcon />
                    </a>
                </li>
                <li class="media-icon">
                    <a href="https://steamcommunity.com/id/hiderua/">
                        <SteamIcon />
                    </a>
                </li>
                <li class="media-icon">
                    <div class="image-container" :onClick="login" :style="{ borderColor: border_color }">
                        <img src="../assets/img/face-boqi.jpg">
                    </div>
                </li>
            </ul>
        </nav>
    </header>
</template>

<style scoped lang="less">
.header {
    height: 50px;
    background-color: #22222200;
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 0 20px;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;

    a {
        color: #000000;
        text-decoration: none;
        font-size: 24px;
        font-weight: bold;
    }


    .nav-list {
        display: flex;
        flex-direction: row;
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .nav-list li {
        margin-right: 20px;
        align-items: center;
        justify-content: center;
        display: flex;
    }

    .nav-list li:last-child {
        margin-right: 0;
    }

    .media-icon {
        padding: 0 10px;

        .image-container {
            width: 40px;
            /* 设置容器的宽度 */
            height: 40px;
            /* 设置容器的高度 */
            border-radius: 50%;
            /* 将容器的圆角半径设置为50% */
            overflow: hidden;
            border: 1px solid;

            /* 隐藏超出容器部分的内容 */
            img {
                display: block;
                border-radius: 50%;
                width: 100%;
                /* 设置图片的宽度为容器的宽度 */
                height: 100%;
                /* 设置图片的高度为容器的高度 */
                object-fit: cover;
                /* 将图片按比例缩放，铺满整个容器 */
            }
        }

        svg {
            height: 30px;
            width: 30px;
        }
    }
}
</style>