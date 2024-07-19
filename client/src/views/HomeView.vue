<template>
  <div class="appproc">
    <!-- <img class="background-image1" src="@/img/Vector (1).svg" alt="background">
    <img class="background-image2" src="@/img/Vector (2).svg" alt="background">

    <RouterLink :to="`/`">
      <div class="logo">
      <h2 class="logo_p1">Recruitment</h2>
      <img class="logo_p2" src="@/img/iu_logo_green 1.svg" alt="university logo ">
    </div>
    </RouterLink> -->

    <!-- <p class="title" style="color: white;">Vacancies</p> -->
    <div class="tables">


      <div class="vac">
        <div class="head">
          <RouterLink :to="`/createVac`">
            <div class="plus">
              <img src="@/img/Plus.svg" alt="plus">
            </div>
          </RouterLink>
          <div class="vac_header">
            <p>New Vacancies</p>
          </div>
        </div>
        <VacancyBox v-for="vacancy in latestVacancies" :key="vacancy.id" :vacancy="vacancy" class="column is-4" />
      </div>


      <div class="vacInPr">
        <div class="vacInPr_header">
          <p>Vacancies in processing</p>
        </div>
        <VacancyInPrBox v-for="vacancy in VacanciesInProcessing" :key="vacancy.id" :vacancy="vacancy"
          class="column is-4" />
      </div>
    </div>

  </div>

</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
import VacancyBox from '@/components/VacancyBox.vue'; // Импорт дочернего компонента
import VacancyInPrBox from '@/components/VacancyInPrBox.vue';
import '@/assets/global.css';

interface Vacancy {
  id: number;
  comment: string;
  grade: string;
  mark: number;
  stack: string;
  rate: number;
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
    VacancyInPrBox
  },
  data() {
    return {
      latestVacancies: [] as Vacancy[],// Начальное состояние для экземпляра компонента 
      VacanciesInProcessing: [] as Vacancy[]
    }
  },
  mounted() {
    localStorage.currid = 0;
    this.getLatestVacancies();
    // this.getVacanciesInPr();
    document.title = 'Home | Vacancies';
  },
  methods: {// Здесь лучше не использовать функции со стрелками, у них не будет доступа через this
    async getLatestVacancies() {
      try {
        const response = await axios.get('main/vacancies/');
        // this.latestVacancies = response.data as Vacancy[];
        for (const vac of response.data as Vacancy[]) {
          localStorage.currid = vac.id;
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
    // async getVacanciesInPr(){
    //   try {
    //     const response = await axios.get('main/vacancies/');
    //     this.VacanciesInProcessing = response.data as Vacancy[];
    //   } catch (error) {
    //     console.error(error);
    //   }
    // }
  }
});
</script>

<style scoped>
.head {
  display: flex;
  flex-direction: row-reverse;
  gap: 5%;
}

.vacancies {
  display: flex;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.title {
  padding-top: 0px;

  font-family: League Spartan;
  font-size: 40px;
  font-weight: 500;

  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.tables {
  display: flex;
  flex-direction: row;
  margin: 0px 30px;
  gap: 15px;

  position: relative;
  z-index: 1;
}

.vac {
  padding-top: 31px;
  width: 50%;
  height: 495px;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-y: scroll;
  border-radius: 3px;
  margin-left: 120px;
  /* box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); */
}

.vac_header {
  color: rgb(255, 255, 255);
  font-family: 'League Spartan';
  font-size: 22px;
  font-weight: 400;
  line-height: 30px;
  border-radius: 3px;
  background: rgb(73, 73, 73);
  width: 300px;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 30px;
}

.vacInPr_header {
  color: rgb(255, 255, 255);
  font-family: 'League Spartan';
  font-size: 22px;
  font-weight: 400;
  line-height: 30px;
  /* Должен быть равен высоте для вертикального центрирования текста */
  border-radius: 3px;
  background: rgb(73, 73, 73);
  width: 300px;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 30px;
}

.vacInPr {
  /* box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); */
  width: 50%;
  height: 520px;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-y: scroll;
  border-radius: 3px;
  margin-right: 153px;
  margin-left: 120px;
}


@media(width: 1024px) {

  .title {
    font-size: 28px;
  }

  .vac {
    height: 324px;
    margin-left: 30px;
  }

  .vac_header {
    width: 350px;
    height: 30px;
    font-size: 18px;
  }

  .vacInPr {
    height: 355px;
    margin-left: 60px;
    margin-right: 0;
  }

  .vacInPr_header {
    width: 350px;
  }
}

@media(width: 1280px) {
  .vac {
    margin-left: 30px;
  }

  .vacInPr {
    margin-left: 30px;
    margin-right: 0;
  }

  .vacInPr_header {
    width: 380px;
  }
}


@media(min-width: 2560px) {

  .title {
    font-family: League Spartan;
    font-weight: 500;
    line-height: 37px;
    font-size: 73px;
  }

  .vac {
    height: 870px;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow-y: scroll;
    padding-top: 31px;
    padding-bottom: 31px;
    border-radius: 3px;
  }

  .vac_header {
    width: 980px;
    height: 50px;
    font-size: 40px;
  }

  .vacInPr {
    height: 930px;
    margin-left: 60px;
    margin-right: 0;
  }

  .vacInPr_header {

    width: 800px;
    height: 50px;
    font-size: 40px;
  }
}

@media(width: 3840px) {


  .vac {
    height: 1182px;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow-y: scroll;
    gap: 20px;
    padding-top: 46px;
    padding-bottom: 31px;
    border-radius: 3px;
  }

  .vac_header {
    width: 1405px;
    height: 80px;
    font-size: 60px;
  }

  .vacInPr {
    height: 1250px;
  }

  .vacInPr_header {
    width: 980px;
    height: 80px;
    font-size: 59px;
  }
}
</style>
