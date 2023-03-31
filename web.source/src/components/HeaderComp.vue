<script setup lang="ts">
import LogoIcon from './icons/LogoIcon.vue';
import BilibiliIcon from './icons/BilibiliIcon.vue';
import GithubIcon from './icons/GithubIcon.vue';
import SteamIcon from './icons/SteamIcon.vue';

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

        svg {
            height: 30px;
            width: 30px;
        }
    }
}
</style>