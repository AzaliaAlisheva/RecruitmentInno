<template>
  <img class="background-image1" src="@/img/Vector (1).svg" alt="background">
  <img class="background-image2" src="@/img/Vector (2).svg" alt="background">
    <RouterLink :to="`/`">
      <div class="logo">
      <h2 class="logo_p1">Recruitment</h2>
      <img class="logo_p2" src="@/img/iu_logo_green 1.svg" alt="university logo ">
    </div>
    </RouterLink>
  <div class="about">
    <h1>The about page</h1>
    <p>Our project is designed to help recruiters make their workflow more efficient. We tried to automate the work and made it easy to use. We have added functions for distributing specialists into different subgroups, the ability to add comments, etc. We hope that you will also appreciate the interface and functionality of our product, as we did.</p>
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
h1{
  font-family: League Spartan;
  font-size: 45px;
  font-weight: 500;
  color: #1d1d1d;
  margin: 0;
  text-shadow: 0px 4px 4px rgba(255, 255, 255, 0.25);
}
.background-image1{
  position: fixed;
    bottom: 24px;
    left: -469px;
    width: 153%;
}
.background-image2{
  position: fixed;
  bottom: 0;
  left: -115px;
  width: 115%;
}
.logo_p1{
  font-family: League Spartan;
  font-size: 27px;
  font-weight: 900;
  line-height: 32px;
  color:#FFFFFF;
  margin-left: 91px;
  margin-right: -79px;
  padding-top: 60px;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.logo{
  display: flex;
   flex-direction: row;
   justify-content: flex-start;
}

.about{
    font-size: 26px;
    font-family: League Spartan;
    background-color: rgba(220, 220, 220, 0.356);
    background-size: 100%;
    color: #1d1d1d;
    width: 657px;
    height: 450px;
    padding-left: 34%;
    padding-right: 35%;
    display: flex;
    padding-top: 5%;
    padding-bottom: 5%;
    text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    flex-direction: column;
    align-items: center;
    text-align: justify;
    justify-content: center;
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
}
</style>