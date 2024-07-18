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
    <div class="deletion">
      <img class="" :src="trash" alt="deletion" @click="triggerPopup">
    </div>
    <DeletePopup v-if="popupTriggers.buttonTrigger">
      <button @click="deleteVacancy">
        Delete
      </button>
      <button @click="triggerPopup">Go Back</button>
    </DeletePopup>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, ref } from 'vue';
import { RouterLink } from 'vue-router';
import axios from 'axios';
import DeletePopup from '@/components/DeletePopup.vue'


interface Vacancy {
  id: number;
  comment: string;
  grade: string;
  stack: string;
  rate: number;
  full_message: string;
  // добавьте другие поля, если необходимо
}

// const axiosInstance = axios.create({
//   baseURL: 'http://10.90.138.241:8000', // Change this to your backend URL
// });

export default defineComponent({
  name: 'VacancyBox',
  data() {
    const popupTriggers = ref({
      buttonTrigger: false,
      timedTrigger: false,
    })
    return {
      trash: require('@/img/trash.svg'),
      popupTriggers
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
.deletion {
  padding: 5%;
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
