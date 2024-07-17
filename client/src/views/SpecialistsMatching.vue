<template>
  <div class="main_block">
    <h2>Vacancy Name</h2>
    <TabList>
      <TabItem title="Vacancy">
        <p>{{ vacancy.full_message }}</p>
        <button id="button_vac" @click="changeProcessingStatus">
          {{  buttonText }}
        </button>
      </TabItem>
      <TabItem title="Specialists">
        <SpecialistBox v-for="specialist in specialists" :key="specialist.id" :specialist="specialist"
            :vacancyid="vacancy.id"/>
      </TabItem>
      <TabItem title="Specialists in processing">
        <SpecialistInPrBox v-for="specialist in specialistsInProcessing" :key="specialist.id" :vacancyid="vacancy.id"
            :specialist="specialist"/>
      </TabItem>
      <TabItem title="Recently Deleted">
        <SpecialistDelBox v-for="specialist in recentlyDeleted" :vacancyid="vacancy.id" :key="specialist.id"
            :specialist="specialist"/>
      </TabItem>
      <TabItem title="Comments">
        <ul>
          <li v-for="(line, index) in commentLines" :key="index">{{ line }}</li>
        </ul>
        <form>
          <input class="input" id="input" type="text" v-model="inputText">
          <button class="button" @click="submitComment">Submit</button>
        </form>
      </TabItem>
    </TabList>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
import SpecialistBox from '@/components/SpecialistBox.vue';
import SpecialistInPrBox from '@/components/SpecialistInPrBox.vue';
import SpecialistDelBox from '@/components/SpecialistDelBox.vue';
import TabItem from '@/components/TabItem.vue';
import TabList from '@/components/TabList.vue';

interface Specialist {
  id: number;
  name: string;
  comment: string;
  mark: number;
  grade: string;
  stack: string;
}

interface Vacancy {
  id: number;
  comment: string;
  specialists: number[];
  mark: number;
  full_message: string;
}

export default defineComponent({
  name: 'SpecialistsView',
  components: {
    SpecialistBox,
    SpecialistInPrBox,
    SpecialistDelBox,
    TabItem,
    TabList
  },
  props: {
    id: String,
  },
  data() {
    return {
      specialists: [] as Specialist[],
      specialistsInProcessing: [] as Specialist[],
      recentlyDeleted: [] as Specialist[],
      vacancy: {} as Vacancy,
      commentLines: [] as string[],
      buttonText: "",
      inputText: "",
    };
  },
  async mounted() {
    await this.getVacancy();
    await this.getSpecialistsForVacancy();
    await this.drawSomeThings();

  },
  methods: {
    async getSpecialistsForVacancy() {
      try {
        const response = await axios.get('main/connect/');
        for (const con of response.data) {
          const vac = con.vacancy;
          if (vac === this.vacancy.id) {
            const response = await axios.get('main/specialists/' + con.specialist);
            const spec = response.data as Specialist;
            const mark = con.specmark;
            if (mark === -1) {
              this.specialists.push(spec);
            } else if (mark === 1) {
              this.specialistsInProcessing.push(spec);
            } else {
              this.recentlyDeleted.push(spec);
            }
          }
        }
      } catch (error) {
        console.error(error);
      }
    },

    async getVacancy() {
      try {
        const response = await axios.get('main/vacancies/' + this.id);
        this.vacancy = response.data as Vacancy;
      } catch (error) {
        console.error(error);
      }
    },

    async submitComment() {
      if(!this.inputText) return;
      const comment = this.vacancy.comment + this.inputText + '/n';
      await axios.patch(`main/vacancies/${this.vacancy.id}/`, { comment });
      this.inputText = '';
      this.commentLines.push(this.inputText);
    },

    async drawSomeThings() {
      const mark = this.vacancy.mark;
      this.buttonText = mark === -1 ? 'Add to vacancy in Process' : 'Remove vacancy from Process';
      this.commentLines = this.vacancy.comment ? this.vacancy.comment.split('/n') : [];
    },

    async changeProcessingStatus() {
      const newMark = this.vacancy.mark === -1 ? 0 : -1;
      const response = await axios.patch(`main/vacancies/${this.vacancy.id}/`, { mark: newMark });
      this.vacancy.mark = newMark;
      this.buttonText = newMark === -1 ? 'Add to vacancy in Process' : 'Remove vacancy from Process';
      location.reload();
      return response.data;
    },
  },
});
</script>

<style scoped>
#button_vac {
  padding: 20px;
  border: 1px solid #E8E7E7;
  margin-bottom: 20px;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  background: #E8E7E7;

  color: rgb(0, 0, 0);
  font-family: League Spartan;
  font-size: 20px;
  font-weight: 400;
  line-height: 18px;
}


form {
    background: rgba(0, 0, 0, 0.15);
    padding: 0.25rem;
    position: relative;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    height: 3rem;
    box-sizing: border-box;
    backdrop-filter: blur(10px);
}

input {
    border: none;
    padding: 0 1rem;
    flex-grow: 1;
    border-radius: 2rem;
    margin: 0.25rem;
}

input:focus {
    outline: none;
}

form > button {
    background: #333;
    border: none;
    padding: 0 1rem;
    margin: 0.25rem;
    border-radius: 3px;
    outline: none;
    color: #fff;
}

/* p {
  margin-top: 0;
} */

ul {
  margin-top: 0;
  min-height: calc(100% - 3rem);
}

li {
  word-break: break-word;
  padding: 0.5rem 1rem;
}

li:nth-child(odd) {
    background-color: #f8f8f8;
}
</style>
