<script setup lang="ts">
document.title = 'BLS | 你寻找的页面走失了（乐'
</script>
<template>
    <div class="container">
        <h1>404</h1>
        <p>Sorry, the page you requested could not be found.</p>
        <button onclick="history.go(-1)">Go Back</button>
        <div style="height: 200px;"></div>
    </div>
</template>

<style scoped lang="less">
body {
    background-color: #f1f1f1;
    font-family: "FiraCode","Courier New", Courier, monospace;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 50px;
    text-align: center;
}

h1 {
    font-size: 72px;
    font-weight: 700;
    color: #0099ff;
    margin-bottom: 20px;
}

p {
    font-size: 24px;
    color: #444;
    margin-bottom: 20px;
}

button {
    display: inline-block;
    padding: 10px 20px;
    background-color: #0099ff;
    color: #fff;
    border-radius: 5px;
    font-size: 18px;
    text-align: center;
    text-decoration: none;
    transition: background-color 0.2s ease;
    margin-top: 20px;
}

button:hover {
    background-color: #0077cc;
}
</style>