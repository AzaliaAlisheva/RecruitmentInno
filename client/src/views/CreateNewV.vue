<template>
    <h2>Create New Vacancy</h2>
    <div class="outer-container">
        <div class="container">
            <div class="input">
                <input type="text" placeholder="Grade" v-model="vacancy.grade" required>
                <input type="text" placeholder="Stack" v-model="vacancy.stack" required>
                <input type="text" placeholder="Instruments" v-model="vacancy.instruments" required>
                <input type="number" placeholder="Years of Experience" v-model="vacancy.experience" min="0" step="1"
                    required>
                <input type="number" placeholder="Rate (e.g., per hour)" v-model="vacancy.rate" min="0" step="any"
                    required>
                <input type="text" placeholder="Location" v-model="vacancy.location" required>
                <input type="text" placeholder="Citizenship" v-model="vacancy.citizenship" required>
                <input type="tel" placeholder="Contact Number" v-model="vacancy.contact" required>
                <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
                <button class="submitButton" @click="validateForm">Submit</button>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import axios from 'axios';
import { defineComponent } from 'vue';

interface Vacancy {
    id: number;
    date: Date;
    grade: string;
    stack: string;
    instruments: string;
    experience: number;
    is_regular_staff: string;
    is_urgent: boolean;
    type: boolean;
    rate: number;
    location: string;
    citizenship: string;
    contact: string;
}

export default defineComponent({
    name: 'CreateNewView',
    data() {
        return {
            vacancy: {
                id: localStorage.currid++,
                date: new Date(),
                grade: '',
                stack: '',
                instruments: '',
                experience: 0,
                type: false,
                is_regular_staff: "false",
                is_urgent: false,
                rate: 0,
                location: '',
                citizenship: '',
                contact: '',
            } as Vacancy,
            errorMessage: '',
        };
    },
    methods: {
        validateForm() {
            if (this.vacancy.grade && this.vacancy.stack && this.vacancy.instruments && this.vacancy.experience && this.vacancy.rate &&
                this.vacancy.location && this.vacancy.citizenship && this.vacancy.contact) {
                this.createVacancy();
            } else {
                this.errorMessage = 'Please fill in all fields';
            }
        },
        async createVacancy() {
            try {
                const response = await axios.post('main/vacancies/', {
                    "chat_id": this.vacancy.id,
                    "date": this.vacancy.date,
                    "grade": this.vacancy.grade,
                    "stack": this.vacancy.stack,
                    "instruments": this.vacancy.instruments,
                    "experience": this.vacancy.experience,
                    "is_regular_staff": this.vacancy.is_regular_staff,
                    "is_urgent": this.vacancy.is_urgent,
                    "type": this.vacancy.type,
                    "rate": this.vacancy.rate,
                    "location": this.vacancy.location,
                    "citizenship": this.vacancy.citizenship,
                    "contact": this.vacancy.contact,
                });
                console.log('Vacancy created successfully:', response.data);
                alert('Vacancy created successfully');
            } catch (error) {
                if (axios.isAxiosError(error) && error.response) {
                    console.error('Error creating vacancy:', error.response.data, this.vacancy);
                } else {
                    console.error('Unknown error:', error);
                }
            }
        },
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
