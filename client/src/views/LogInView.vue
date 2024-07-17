<template>
    <h2>Log In</h2>
    <form id="register" @submit.prevent="submitData" action="/">
        <input placeholder="email" id="emailInput" required>
        <input placeholder="password" id="passwordInput" required>

        <div class="line">
            <label class="left">
                <input type="checkbox" id="remember_me" value="remember" />
                Remember me
            </label>
            <a href="" id="forgot_password" class="right">Forgot password?</a>
        </div>

        <button class="submit">Submit</button>
        <div class="line">
            <label class="left">Don't you have account?</label>
            <a href="/signup" class="right">Register</a>
        </div>
    </form>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';

interface User {
    email: string;
}

const correctPassword = "password";

export default defineComponent({
    name: 'LogIn',
    data() {
        return {}
    },
    mounted() {
        localStorage.removeItem('isAuthenticated');
        document.title = 'Login';
    },
    methods: {
        async submitData(e: Event) {
            e.preventDefault();

            try {
                const emailInput = (document.getElementById('emailInput') as HTMLInputElement).value;
                const passwordInput = (document.getElementById('passwordInput') as HTMLInputElement).value;
                const response = await axios.get('main/users/');

                if (passwordInput !== correctPassword) {
                    alert("Wrong password");
                } else {
                    for (const user of response.data as User[]) {
                        if (user.email === emailInput) {
                            (e.target as HTMLFormElement).submit();
                            localStorage.setItem('isAuthenticated', 'true');
                            return true;
                        }
                    }
                    alert("Email not found");
                }
            } catch (error) {
                console.log(error);
            }

            return false; // Return false if validation fails
        }
    }
})
</script>

<style>
    input {
        margin: 0 auto;
        padding: 15px;
        width: 220px;
        border-radius: 18px;
        background-color: #67A14B;
        display: flow;
        border-width: 0;
        margin-bottom: 10px;
        box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
        position: relative;
        z-index: 1;
    }

    ::placeholder {
        color: white;
    }

    .submit {
        padding: 15px;
        width: 250px;
        border-radius: 18px;
        background-color: #04041A;
        color: white;
        border-width: 0;
        box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
        position: relative;
        z-index: 1;
        display: flow;
        margin: 0 auto;
    }

    form {
        color: white;
        display: inline-block;
    }

    #remember_me {
        width: auto;
        margin: 0;
        margin-right: 5px;
        display: inline-block;
        vertical-align: middle;
    }

    label {
        font-size: smaller;
        margin-right: 20px;
    }

    a {
        color: white;
        font-size: smaller;
    }


    .line {
        height: 15px;
        margin: 10px;
        position: relative;
        z-index: 1;
    }

    .right {
        float: right;
    }

    .left {
        float: left;
    }
</style>
