<template>
    <h2>Sign Up</h2>
    <form id="register" @submit.prevent="submitData" action="/">
        <input placeholder="email" id="emailInput" required>
        <input placeholder="password" id="passwordInput1" required>
        <input placeholder="password" id="passwordInput2" required>
        <button class="submit">Submit</button>
        <div class="line">
            <a href="/">Already a member?</a>
        </div>
    </form>
</template>

<script lang="ts">

import { defineComponent } from 'vue';
import axios from 'axios';

// interface User {
//     email: string;
// }

const correctPassword = "password";

export default defineComponent({
    name: 'SignUp',
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
                const passwordInput1 = (document.getElementById('passwordInput1') as HTMLInputElement).value;
                const passwordInput2 = (document.getElementById('passwordInput2') as HTMLInputElement).value;
                if (passwordInput1 !== correctPassword || passwordInput2 !== correctPassword) {
                    alert("You are not member of RecruitemntInno :(");
                } else if (passwordInput1 == passwordInput2) {
                    const response = await axios.post('main/users/', { "email": emailInput });
                    // .then(function (response) {
                    //     console.log(response);
                    // })
                    // .catch(function (error) {
                    //     console.log(error);
                    // });
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