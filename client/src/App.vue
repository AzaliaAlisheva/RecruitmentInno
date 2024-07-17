wrapper value around of all code
<template>
  <nav>
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> -->
  </nav>

  <img id="waves_gray" src="@/img/waves_gray.svg" alt="background">
  <img id="waves_white" src="@/img/waves_white.svg" alt="background">

  <RouterLink :to="`/`">
    <div class="logo">
      <h2>Recruitment</h2>
      <img src="@/img/iu_logo_green.svg" alt="university logo">
    </div>
  </RouterLink>
  <router-view />
</template>

<style lang="scss" scoped>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #waves_gray {
    position: fixed;
    bottom: 24px;
    left: -35%;
    width: 150%;
    z-index: -1;
  }

  #waves_white {
    position: fixed;
    bottom: 0;
    left: -15%;
    width: 120%;
    z-index: -1;
  }

  .logo h2 {
    font-family: Lato;
    font-size: 27px;
    font-weight: 900;
    line-height: 32px;
    color: #FFFFFF;
    margin-left: 91px;
    margin-right: -79px;
    padding-top: 70px;
    text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  }

  .logo {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
  }

  
  @media (max-width: 680px) {
    #waves_gray {
      bottom: 10px;
    }
  }
</style>
