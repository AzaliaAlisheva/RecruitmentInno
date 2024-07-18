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
import DeletePopup from '@/components/DeletePopup.vue';

interface Vacancy {
  id: number;
  comment: string;
  grade: string;
  stack: string;
  rate: number;
  full_message: string;
  // добавьте другие поля, если необходимо
}

export default defineComponent({
  name: 'VacancyBox',
  // это способ передачи данных от родительского компонента к дочернему компоненту в Vue.js.
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
  background: rgb(199, 198, 198);
  border: 1px solid rgb(199, 198, 198);
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

.box_vacancy {
  overflow: hidden;
  text-decoration: none;
}

.vac_data {
  color: rgb(0, 0, 0);
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
}

@media(width: 1280px) {
  .box_vacancy {
    width: 450px;
  }
}

@media(width: 1440px) {
  .box_vacancy {
    width: 400px;
  }
}

@media(width: 1920px) {
  .box_vacancy {
    width: 550px;
  }
}

@media(width: 2560px) {
  .box_vacancy {
    width: 750px;

  }

  .vac_data {
    font-size: 32px;
    line-height: 40px;
  }
}

@media(width: 3840px) {
  .box_vacancy {
    width: 900px;

  }

  .vac_data {
    font-size: 38px;
    line-height: 30px
  }
}
</style>
