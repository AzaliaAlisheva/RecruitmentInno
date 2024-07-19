<template>
  <div class="vacancy">
    <RouterLink :to="`/vacancies/${vacancy.id}/`">
      <div class="box_vacancy">
        <div class="vac_data">
          <p>{{ vacancy.stack }}</p>
          <p>{{ vacancy.grade }}</p>
          <p>{{ vacancy.rate }}</p>
        </div>
      </div>
    </RouterLink>
    <div class="actions">
      <img class="" :src="trash" alt="deletion" @click="triggerPopup">
      <img class="editButton" :src="editbutton" alt="edit" @click="triggerEdit">
    </div>
    <DeletePopup v-if="popupTriggers.buttonTrigger">
      <button class="deleteButton" @click="deleteVacancy">
        Delete
      </button>
      <button class="goBackButton" @click="triggerPopup">Go Back</button>
    </DeletePopup>
    <div v-if="popupTriggers.editTrigger">
      <form class="input">
        <input type="text" placeholder="Grade" v-model="vac.grade" required>
        <input type="text" placeholder="Stack" v-model="vac.stack" required>
        <input type="text" placeholder="Instruments" v-model="vac.instruments" required>
        <input type="number" placeholder="Years of Experience" v-model="vac.experience" min="0" step="1" required>
        <input type="number" placeholder="Rate (e.g., per hour)" v-model="vac.rate" min="0" step="any" required>
        <input type="text" placeholder="Location" v-model="vac.location" required>
        <input type="text" placeholder="Citizenship" v-model="vac.citizenship" required>
        <input type="tel" placeholder="Contact Number" v-model="vac.contact" required>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
        <button class="submitButton" @click="editVacancy">Submit</button>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, ref } from 'vue';
import { RouterLink } from 'vue-router';
import axios from 'axios';
import DeletePopup from '@/components/DeletePopup.vue'
import EditV from '@/component/EditV.vue';

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
  mark: number;
}

// const axiosInstance = axios.create({
//   baseURL: 'http://10.90.138.241:8000', // Change this to your backend URL
// });

export default defineComponent({
  name: 'VacancyBox',
  data() {
    const popupTriggers = ref({
      buttonTrigger: false,
      editTrigger: false,
    })
    return {
      trash: require('@/img/trash.svg'),
      editbutton: require('@/img/edit.svg'),
      popupTriggers,
      errorMessage: '',
      vac: {
        id: this.vacancy.id,
        date: this.vacancy.date,
        grade: this.vacancy.grade,
        stack: this.vacancy.stack,
        instruments: this.vacancy.instruments,
        experience: this.vacancy.experience,
        type: this.vacancy.type,
        is_regular_staff: this.vacancy.is_regular_staff,
        is_urgent: this.vacancy.is_urgent,
        rate: this.vacancy.rate,
        location: this.vacancy.location,
        citizenship: this.vacancy.citizenship,
        contact: this.vacancy.contact,
      } as Vacancy,
    }
  },
  // это способ передачи данных от родительского компонента к дочернему компоненту в Vue.js.
  props: {
    vacancy: {
      type: Object as PropType<Vacancy>,
      required: true
    }
  },
  components: {
    RouterLink,
    DeletePopup,
  },
  methods: {
    validateForm() {
      if (this.vacancy.grade && this.vacancy.stack && this.vacancy.instruments && this.vacancy.experience && this.vacancy.rate &&
        this.vacancy.location && this.vacancy.citizenship && this.vacancy.contact) {
        this.editVacancy();
      } else {
        this.errorMessage = 'Please fill in all fields';
      }
    },
    async editVacancy() {
      try {
        const response = await axios.put('main/vacancies/' + this.vacancy.id, {
          "chat_id": this.vac.id,
          "date": this.vac.date,
          "grade": this.vac.grade,
          "stack": this.vac.stack,
          "instruments": this.vac.instruments,
          "experience": this.vac.experience,
          "is_regular_staff": this.vac.is_regular_staff,
          "is_urgent": this.vac.is_urgent,
          "type": this.vac.type,
          "rate": this.vac.rate,
          "location": this.vac.location,
          "citizenship": this.vac.citizenship,
          "contact": this.vac.contact,
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
    triggerEdit() {
      this.popupTriggers.editTrigger = !this.popupTriggers.editTrigger;
    },
    triggerPopup() {
      this.popupTriggers.buttonTrigger = !this.popupTriggers.buttonTrigger;
    },
    async deleteVacancy() {
      this.trash = require('@/img/trash.svg');
      await axios.delete('main/vacancies/' + this.vacancy.id);
      this.triggerPopup();
    },

  }

});
</script>

<style scoped>
.input {
  display: flex;
  flex-direction: column;
  /* width: 43vw; */
  /* gap: 15px; */
  background-color: #ffffff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.submitButton {
  /* padding: 20px; */
  border: 1px solid #E8E7E7;
  box-shadow: 0px 4px 4px 0px rgba(241, 226, 226, 0.25);
  background: #E8E7E7;

  color: rgb(0, 0, 0);
  font-family: League Spartan;
  /* font-size: 20px; */
  line-height: 18px;
}

input[type="text"],
input[type="number"],
input[type="date"],
input[type="tel"] {
  /* height: 35px; */
  /* padding: 10px; */
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.reg {
  display: flex;
  gap: 2%;
  align-items: center;
}

/* input[type="checkbox"] {
  /* width: 20px; */
/* height: 20px; */
/* } */
.actions {
  padding: 5%;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.deleteButton {
  padding: 20px;
  border: 1px solid #E8E7E7;
  box-shadow: 0px 4px 4px 0px rgba(241, 226, 226, 0.25);
  background: #E8E7E7;
  color: rgb(0, 0, 0);
  font-family: League Spartan;
  font-size: 20px;
  line-height: 18px;
}

.goBackButton {
  padding: 20px;
  border: 1px solid #E8E7E7;
  box-shadow: 0px 4px 4px 0px rgba(241, 226, 226, 0.25);
  background: #E8E7E7;
  color: rgb(0, 0, 0);
  font-family: League Spartan;
  font-size: 20px;
  line-height: 18px;
}

.vacancy {
  background: rgb(73, 73, 73);
  border: 1px solid #494949;
  margin-left: 5%;
  margin-left: 5%;
  box-shadow: inset 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  width: 90%;
  display: flex;
  flex-direction: row;
  margin-bottom: 1%;
  display: flex;
  justify-content: space-between;
  border-radius: 3px;
}

/* 
.box_vacancy {
} */

.vac_data {
  color: white;
  font-family: Lato;
  font-size: 18px;
  font-weight: 400;
  line-height: 22px;
  flex-direction: row;
  gap: 10px;
  padding: 10px;
  text-decoration: none;
  text-align: start;
}

@media(width: 1024px) {
  .box_vacancy {
    width: 300px;
  }

  .vac_data {
    font-size: 16px;
  }
}

@media(width: 1280px) {
  .box_vacancy {
    width: 450px;
  }

  .vac_data {
    font-size: 16px;
  }
}

@media(width: 1440px) {
  .box_vacancy {
    width: 480px;
  }

  .vac_data {
    font-size: 16px;
  }
}

@media(width: 1920px) {
  .box_vacancy {
    width: 580px;
  }

  .vac_data {
    font-size: 25px;
  }
}

@media(width: 2560px) {
  .box_vacancy {
    width: 1000px;
    height: auto;
  }

  .vac_data {
    font-size: 32px;
    line-height: 40px
  }
}

@media(width: 3840px) {
  .box_vacancy {
    width: 1450px;
    height: auto;
  }

  .vac_data {
    font-size: 35px;
    line-height: 40px
  }
}
</style>
