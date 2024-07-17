<template>
  <h2>Vacancies</h2>
  <TabList>
    <TabItem title="New Vacancies">
      <VacancyBox v-show="true" v-for="vacancy in latestVacancies" :key="vacancy.id" :vacancy="vacancy"/>
    </TabItem>
    <TabItem title="Vacancies in processing">
      <VacancyInPrBox v-for="vacancy in VacanciesInProcessing" :key="vacancy.id" :vacancy="vacancy"/>
    </TabItem>
  </TabList>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
import VacancyBox from '@/components/VacancyBox.vue'; // Импорт дочернего компонента
import VacancyInPrBox from '@/components/VacancyInPrBox.vue';
import TabItem from '@/components/TabItem.vue';
import TabList from '@/components/TabList.vue';
import '@/assets/global.css';

interface Vacancy {
  id: number;
  comment: string;
  grade: string;
  mark: number;
  stack: string;
  full_message: string;
  // добавьте другие поля, если необходимо
}
const axiosInstance = axios.create({
  baseURL: 'http://10.90.138.241:8000', // Change this to your backend URL
});

// OPTIONS API
export default defineComponent({
  name: 'HomeView',
  components: {
    VacancyBox,
    VacancyInPrBox,
    TabItem,
    TabList,
  },
  data() {
    return {
      latestVacancies: [] as Vacancy[],// Начальное состояние для экземпляра компонента 
      VacanciesInProcessing: [] as Vacancy[]
    }
  },

  mounted() {
    this.getLatestVacancies();
    // this.getVacanciesInPr();
    document.title = 'Home | Vacancies';
  },

  methods: {// Здесь лучше не использовать функции со стрелками, у них не будет доступа через this
    async getLatestVacancies() {
      try {
        const response = await axios.get('main/vacancies/');
        for (const vac of response.data as Vacancy[]) {
          if (vac.mark == -1) {
            this.latestVacancies.push(vac as Vacancy);
          } else {
            this.VacanciesInProcessing.push(vac as Vacancy);
          }
        }
      } catch (error) {
        console.error(error);
      }
    },
  },
});
</script>
