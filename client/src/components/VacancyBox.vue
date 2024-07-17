<template>
  <RouterLink :to="`/vacancies/${vacancy.id}/`">
    <div class="box_vacancy">
      <div class="vac_data">
        <p>{{ vacancy.id }}</p>
        <p>{{ vacancy.full_message }}</p>
        <!-- <p>{{ vacancy.stack }}</p> -->
      </div>
    </div>
  </RouterLink>

</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import { RouterLink } from 'vue-router';

interface Vacancy {
  id: number;
  comment: string;
  grade: string;
  stack: string;
  full_message: string;
  // добавьте другие поля, если необходимо
}

// const axiosInstance = axios.create({
//   baseURL: 'http://10.90.138.241:8000', // Change this to your backend URL
// });

export default defineComponent({
  name: 'VacancyBox',
  // это способ передачи данных от родительского компонента к дочернему компоненту в Vue.js.
  props: {
    vacancy: {
      type: Object as PropType<Vacancy>,
      required: true
    }
  },
  components: {
    RouterLink
  }
});
</script>

<style>
.box_vacancy {
  border: 1px solid #494949;
  background: rgb(73, 73, 73);
  /* border-radius: 7px; */
  box-shadow: inset 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  /* display: flex; */
  /* justify-content: center; */
  margin-bottom: 8px;
  /* height: 150px; */
  overflow: hidden;

  /* display: -webkit-box;
    -webkit-line-clamp: 5;
    -webkit-box-orient: vertical;
    text-overflow: ellipsis;  */
}

.vac_data {
  color: white;
  font-family: Lato;
  font-size: 18px;
  font-weight: 400;
  line-height: 22px;
  flex-direction: row;
  gap: 10px;
  padding: 10px;
}

@media(width: 1024px) {
  .vac_data {
    font-size: 16px;
  }
}

@media(width: 1920px) {
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