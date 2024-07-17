<template>
  <RouterLink :to="`/vacancies/${vacancy.id}/`">
    <div class="box_vacancy">
      <div class="vac_data">
        <p>{{ vacancy.full_message }}</p>
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
  full_message: string;
  // добавьте другие поля, если необходимо
}

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

<style scoped>
.box_vacancy {
  border: 1px solid rgb(199, 198, 198);
  background: rgb(199, 198, 198);
}

.vac_data {
  color: black;
  font-family: Lato;
  font-size: 18px;
  font-weight: 400;
  line-height: 22px;
  text-decoration: none;

}
</style>