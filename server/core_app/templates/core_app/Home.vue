<!-- <template>
    <div class="home">
      <section class="hero is-medium is-dark mb-6">
          <div class="hero-body has-text-centered">
              <p class="title mb-6">
                  Welcome to Djacket
              </p>
              <p class="subtitle">
                  The best jacket store online
              </p>
          </div>
      </section>
  
      <div class="columns is-multiline">
        <div class="column is-12">
            <h2 class="is-size-2 has-text-centered">Latest vacancies</h2>
        </div>
  
        <ProductBox 
          v-for="vacancy in latestVacancies"
          v-bind:key="vacancy.id"
          v-bind:vacancy="vacancy" />
      </div>
    </div>
  </template>
  <script lang="ts">
  
  import axios from 'axios';
  import ProductBox from './components/HelloWorld.vue'; 
  import SpecialistSerializer from 'serializers.py';
  
  export default {
    components: {
      ProductBox
    },
    data() {
      return {
        latestVacancies:[] as Array < SpecialistSerializer >
      };   
    },
    created() {
      this.fetchLatestVacancies();
    },
    methods: {
      async fetchLatestVacancies() {
        try {
          const response = await axios.get('/api/vacancies/');
          this.latestVacancies = response.data;
        } catch (error) {
          console.error('Error fetching vacancies:', error);
        }
      }
    }
  };
  </script> -->