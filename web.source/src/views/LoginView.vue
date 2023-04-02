<script setup lang="ts">
import { ref } from 'vue';
import { Md5 } from 'ts-md5'

let container_height: string = '400px'
let container_width: string = '380px'
let left_offset = ref((window.innerWidth - parseInt(container_width, 10)) / 2 + 'px');
let top_offset = ref((window.innerHeight - parseInt(container_height, 10)) / 2 + 'px');
// 随网页大小变换位置
window.addEventListener('resize', function () {
    left_offset.value = (window.innerWidth - parseInt(container_width, 10)) / 2 + 'px';
    top_offset.value = (window.innerHeight - parseInt(container_height, 10)) / 2 + 'px';
})

let username = ref('')
let pwd = ref('')

function checkStr(str: string): Boolean {
    return true
}

// 登录
const submitFun = (): void => {
    if (checkStr(username.value) && checkStr(pwd.value)) {
        // 通过验证
        fetch('https://api.bls.hair/login', {
            method: 'POST', cache: 'no-cache', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 'username': username.value, 'password': Md5.hashStr(pwd.value).toUpperCase() })
        })
            .then(resp => resp.json())
            .then((data) => {
                if (data.code == '200') {
                    // 登陆成功
                    // TODO 提醒我要做个检测是否有cookie的功能了
                    // TODO 成功的提示和网页跳转
                    // TODO 还没验证这样有没有问题
                    const now = new Date();
                    const expires = new Date(now.getTime() + 7 * 24 * 60 * 60 * 1000);
                    const expiresUTC = expires.toUTCString;
                    document.cookie = `username=${username.value};expires=${expiresUTC};value=${data.value};`;
                }
            })
            .catch((err) => { console.log(err)/*TODO 这里也要调用通知栏*/ })
    } else {
        // TODO 应该加个提示登录失败，调用提示栏
    }
}

</script>

// TODO 制作一下登录界面
<template>
    <div class="login-container"
        :style="{ height: container_height, width: container_width, left: left_offset, top: top_offset }">
        <div class="container-title">登 录</div>
        <div class="login-box">
            <form action="" method="post" id="login-form">
                <label>账号</label>
                <input type="text" name="username" v-model="username">
                <br>
                <label>密码</label>
                <input type="password" name="password" v-model="pwd">
                <br>
            </form>
        </div>
        <div class="login-button">
            <input type="submit" value="登录" :onclick="submitFun">
        </div>
    </div>
</template>

<style scoped lang="less">
.login-container {
    position: absolute;
    display: flex;
    flex-direction: column;
    /* 垂直对齐排列 */
    justify-content: center;
    /* 水平居中 */
    align-items: center;
    /* 垂直居中 */
    margin: 20px;
    padding: 20px;
    background: rgba(255, 255, 255, 0.2);
    /* 这里使用了一个透明白色背景 */
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    /* 添加一个黑色的阴影，模糊度为10像素 */
    backdrop-filter: blur(10px);
    /* 添加模糊效果，模糊度为10像素 */
    border-radius: 20px;

    .container-title {
        font-size: 60px;
        padding-bottom: 30px;
        font-weight: bolder;
    }

    .login-box {
        form {
            line-height: 50px;
            padding: 10px;
        }

        label {
            font-size: 30px;
            font-family: 'SanJiHua';
        }

        input {
            border-radius: 2px;
            height: 25px;
            font-size: 23px;
        }
    }

    input {
        background-color: rgba(240, 248, 255, 0);
    }

    .login-button {
        padding-top: 20px;

        input {
            height: 50px;
            width: 80px;
            border-radius: 5px;
            font-size: 25px;
        }

        input:hover {
            background-color: rgba(99, 253, 53, 0.3);
        }
    }
}
</style>