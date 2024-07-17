<template>
    <h2>Log In</h2>
    <form id="login" class="authentication_form" @submit.prevent="submitData" action="/">
            <input placeholder="email" class="authentication_input" required v-model="emailInput">
            <input placeholder="password" class="authentication_input" required v-model="passwordInput">

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
        return {
            emailInput: "",
            passwordInput: ""
        }
    },
    mounted() {
        localStorage.removeItem('isAuthenticated');
        document.title = 'Login';
    },
    methods: {
        async submitData(e: Event) {
            e.preventDefault();
            try {
               const response = await axios.get('main/users/');

                if (this.passwordInput !== correctPassword) {
                    alert("Wrong password");
                } else {
                    for (const user of response.data as User[]) {
                        if (user.email === this.emailInput) {
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
            return false;
        }
    }
})
</script>

<style>
    .authentication_input {
        margin: 0 auto;
        padding: 15px 0;
        text-indent: 15px;
        width: 100%;
        border-radius: 18px;
        background-color: #67A14B;
        /* display: flow; */
        border-width: 0;
        box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
        position: relative;
        z-index: 1;
    }

    ::placeholder {
        color: white;
    }

    .submit {
        padding: 15px;
        width: 100%;
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

    .authentication_form {
        color: white;
        display: flex;
        width: 270px;
        margin: 0 auto;
        flex-direction: column;
        justify-content: center;
        align-items: stretch;
        gap: 10px;
    }

    input[type=checkbox] {
        width: auto;
        margin: 0;
        margin-right: 3px;
        display: inline-block;
        vertical-align: middle;
    }

    label {
        /* font-size: smaller; */
        margin-right: 20px;
    }

    a {
        color: white;
        /* font-size: smaller; */
    }


    .line {
        /* height: 15px; */
        margin: 0 10px;
        position: relative;
        z-index: 1;
    }

    .right {
        float: right;
    }

    .left {
        float: left;
    }

    @media only screen and (min-width: 1920px) {
        .authentication_input {
            font-size: 30px;
            border-radius: 40px;
            padding: 30px 0;
            text-indent: 30px;
            box-shadow: 0px 8px 8px rgba(0, 0, 0, 0.25);
        }

        .submit {
            font-size: 30px;
            padding: 30px;
            border-radius: 40px;
            box-shadow: 0px 8px 8px rgba(0, 0, 0, 0.25);
        }

        .authentication_form {
            font-size: 30px;
            width: 550px;
            gap: 20px;
        }

        .line {
            margin: 0 30px;
        }

        input[type=checkbox] {
            transform: scale(2);
            margin-right: 20px;
        }
    }

    @media only screen and (min-width: 3700px) {
        .authentication_input {
            font-size: 50px;
            border-radius: 60px;
            padding: 50px 0;
            text-indent: 50px;
            box-shadow: 0px 20px 20px rgba(0, 0, 0, 0.25);
        }

        .submit {
            font-size: 50px;
            padding: 50px;
            border-radius: 60px;
            box-shadow: 0px 20px 20px rgba(0, 0, 0, 0.25);
        }

        .authentication_form{
            width: 1050px;
            gap: 40px;
            font-size: 60px;
        }

        .line {
            margin: 0 50px;
        }

        input[type=checkbox] {
            transform: scale(4);
            margin-right: 30px;
        }
    }
</style>
