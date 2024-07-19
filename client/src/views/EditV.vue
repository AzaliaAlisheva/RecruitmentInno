<template>
    <h2>Edit Vacancy</h2>
    <div class="outer-container">
        <div class="container">
            <slot />
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';

export default defineComponent({
    name: 'CreateNewView',
    data() {
        return {
        };
    },
    methods: {


    },
});
</script>

<style scoped>
.outer-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    /* Full viewport width */
}

.input {
    display: flex;
    flex-direction: column;
    width: 43vw;
    gap: 15px;
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.submitButton {
    padding: 20px;
    border: 1px solid #E8E7E7;
    box-shadow: 0px 4px 4px 0px rgba(241, 226, 226, 0.25);
    background: #E8E7E7;

    color: rgb(0, 0, 0);
    font-family: League Spartan;
    font-size: 20px;
    line-height: 18px;
}

input[type="text"],
input[type="number"],
input[type="date"],
input[type="tel"] {
    height: 35px;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.reg {
    display: flex;
    gap: 2%;
    align-items: center;
}

input[type="checkbox"] {
    width: 20px;
    height: 20px;
}

.error-message {
    color: red;
    font-size: 14px;
}
</style>
