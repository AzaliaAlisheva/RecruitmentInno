<template>
    <h2>Sign Up</h2>
    <form id="register" @submit.prevent="submitData" action="/">
        <input placeholder="email" class="authentication_input" required v-model="emailInput">
        <input placeholder="password" class="authentication_input" required v-model="passwordInput">
        <input placeholder="password" class="authentication_input" required v-model="passwordValidation">
        <button class="submit">Submit</button>
        <div class="line">
            <a href="/">Already a member?</a>
        </div>
    </form>
</template>

<script lang="ts">

import { defineComponent } from 'vue';
import axios from 'axios';

const correctPassword = "password";

export default defineComponent({
    name: 'SignUp',
    data() {
        return {
            emailInput: "",
            passwordInput: "",
            passwordValidation: ""
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
               if (this.passwordInput !== correctPassword || this.passwordValidation !== correctPassword) {
                    alert("You are not member of RecruitemntInno :(");
                } else if (this.passwordInput == this.passwordValidation) {
                    await axios.post('main/users/', { "email": this.emailInput });
                    return true;
                }
            } catch (error) {
                console.log(error);
            }
            return false;
        }
    }
})
</script>