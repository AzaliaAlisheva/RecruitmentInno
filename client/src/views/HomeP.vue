<template>
  <div class="text">
    <h1>We are glad to see you here!</h1>
    <div class="links">
      <RouterLink :to="`/vacancies`">
        <div class="vac">
          <h2> All Vacancies Page</h2>
        </div>
      </RouterLink>
      <RouterLink :to="`/about`">
        <div class="about">
          <h2> About Page</h2>
        </div>
      </RouterLink>
    </div>
  </div>

</template>
<script lang="ts">
import '@/assets/global.css';
import { defineComponent } from 'vue';
import axios from 'axios';
import { RouterLink } from 'vue-router';

interface Vacancy {
  id: number;
  comment: string;
  grade: string;
  mark: number;
  stack: string;
  full_message: string;
  // добавьте другие поля, если необходимо
}
// OPTIONS API
export default defineComponent({
  name: 'HomeView',
  components: {
    RouterLink
  }
});
</script>
<style scoped>
h1 {
  font-family: League Spartan;
  font-size: 53px;
  font-weight: 500;
  color: #ffffff;
  margin: 0;
  text-shadow: 0px 4px 4px rgba(255, 255, 255, 0.25);
}

.background-image1 {
  position: fixed;
  bottom: 24px;
  left: -469px;
  width: 153%;
}

.background-image2 {
  position: fixed;
  bottom: 0;
  left: -115px;
  width: 115%;
}

.logo_p1 {
  font-family: League Spartan;
  font-size: 27px;
  font-weight: 900;
  line-height: 32px;
  color: #FFFFFF;
  margin-left: 91px;
  margin-right: -79px;
  padding-top: 60px;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.logo {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.text {
  background-color: rgba(220, 220, 220, 0.356);
  height: 110px;
  margin-top: 60px;
  background-size: 100%;
  color: #ffffff;
  padding: 250px;
  font-family: League Spartan;
  font-size: 20px;
  color: #1d1d1d;
  text-decoration: none;
  /* box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); */
  gap: 7%;
}

.links {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 120px;
}

.vac {
  font-size: 20px;
  justify-self: start;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  color: #ffffff;
  font-weight: 300;
  text-decoration: none;
}

.about {
  justify-self: start;
  font-size: 20px;
  justify-self: start;
  color: #ffffff;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
</style>