<template>
  <div class="main_block">
    <h2>Vacancy Name</h2>
    <TabList>
      <TabItem title="Vacancy">
        <p>{{ vacancy.full_message }}</p>
        <button id="button_vac" @click="changeProcessingStatus">
          <p class="button_vac_text" id="button_vac_text"></p>
        </button>
      </TabItem>
      <TabItem title="Specialists">
        <SpecialistBox v-for="specialist in specialists" :key="specialist.id" :specialist="specialist"
            :vacancyid="vacancy.id" class="column is-4" />
      </TabItem>
      <TabItem title="Specialists in processing">
        <SpecialistInPrBox v-for="specialist in specialistsInProcessing" :key="specialist.id" :vacancyid="vacancy.id"
            :specialist="specialist" class="column is-4" />
      </TabItem>
      <TabItem title="Recently Deleted">
        <SpecialistDelBox v-for="specialist in recentlyDeleted" :vacancyid="vacancy.id" :key="specialist.id"
            :specialist="specialist" class="column is-4" />
      </TabItem>
      <TabItem title="Comments">
        <ul>
          <li v-for="(line, index) in commentLines" :key="index">{{ line }}</li>
        </ul>
        <form>
          <input class="input" id="input" type="text">
          <button class="button" @click="submitComment">Submit</button>
        </form>
      </TabItem>
    </TabList>
    <!-- <div class="tables">
      <div class="tables_tex">
        <div class="vac">
          <div class="vac_header">
            <p>vacancy</p>
          </div>
          <p>{{ vacancy.full_message }}</p>
        </div>
        <div class="com">
          <div class="com_header">
            <p>comments</p>
          </div>
          <div class="comments__rendering">
            <div v-if="commentLines.length">
              <ul>
                <li v-for="(line, index) in commentLines" :key="index">{{ line }}</li>
              </ul>
            </div>
          </div>
          <div class="new__comment">
            <input class="input" id="input" type="text">
            <button class="button" @click="submitComment">Submit</button>
          </div>
        </div>
      </div>
      <div class="specialists">
        <div class="spec">
          <div class="spec_header">
            <p>specialists</p>
          </div>
          <SpecialistBox v-for="specialist in specialists" :key="specialist.id" :specialist="specialist"
            :vacancyid="vacancy.id" class="column is-4" />
        </div>
        <div class="button_vac" id="button_vac" @click="changeProcessingStatus">
          <p class="button_vac_text" id="button_vac_text"></p>
        </div>
      </div>
      <div class="flagTables">
        <div class="specFlag">
          <div class="specFlag_header">
            <p>specialists in processing</p>
          </div>
          <SpecialistInPrBox v-for="specialist in specialistsInProcessing" :key="specialist.id" :vacancyid="vacancy.id"
            :specialist="specialist" class="column is-4" />
        </div>
        <div class="specFlag">
          <div class="specFlag_header">
            <p>recently deleted</p>
          </div>
          <SpecialistDelBox v-for="specialist in recentlyDeleted" :vacancyid="vacancy.id" :key="specialist.id"
            :specialist="specialist" class="column is-4" />
        </div>
      </div>
    </div> -->
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
        // for (const specId of this.vacancy.specialists) {
        //   const response = await axios.get('main/specialists/' + specId);
        //   const specialist = response.data as Specialist;
        //   const mark = await this.getSpecmark(specId);
        //   if (mark === -1) {
        //     this.specialists.push(specialist);
        //   } else if (mark === 1) {
        //     this.specialistsInProcessing.push(specialist);
        //   } else {
        //     this.recentlyDeleted.push(specialist);
        //   }
        // }
      } catch (error) {
        console.error(error);
      }
    },
    // async getSpecmark(specialist_id: number) {
    //   try {
    //     const response = await axios.get('/get-specmark/', {
    //       params: {
    //         vacancy_id: this.vacancy.id,
    //         specialist_id: specialist_id,
    //       }
    //     });
    //     return response.data as number;
    //   } catch (error) {
    //     console.error('Error retrieving specmark:', error);
    //   }
    // },
    async getVacancy() {
      try {
        const response = await axios.get('main/vacancies/' + this.id);
        this.vacancy = response.data as Vacancy;
      } catch (error) {
        console.error(error);
      }
    },
    async submitComment() {
      const input = document.getElementById('input') as HTMLInputElement;
      const comment = this.vacancy.comment + input.value + '/n';
      await axios.patch(`main/vacancies/${this.vacancy.id}/`, { comment });
      input.value = '';
      this.commentLines.push(input.value);
      location.reload();
    },
    async drawSomeThings() {
      const buttonText = document.getElementById('button_vac_text') as HTMLElement;
      const mark = this.vacancy.mark;
      buttonText.textContent = mark === -1 ? 'Add to vacancy in Process' : 'Remove vacancy from Process';
      this.commentLines = this.vacancy.comment ? this.vacancy.comment.split('/n') : [];
    },
    async changeProcessingStatus() {
      const buttonText = document.getElementById('button_vac_text') as HTMLElement;
      const newMark = this.vacancy.mark === -1 ? 0 : -1;
      const response = await axios.patch(`main/vacancies/${this.vacancy.id}/`, { mark: newMark });
      this.vacancy.mark = newMark;
      buttonText.textContent = newMark === -1 ? 'Add to vacancy in Process' : 'Remove vacancy from Process';
      location.reload();

      return response.data;
    },
    // async viewSpecialistDetail(id: number) {
    //   this.$router.push({ name: 'SpecDescription', params: { id } });
    // },
  },
});
</script>

<style scoped>
/* .input {
  background-color: rgb(219, 215, 215);
  margin-bottom: 30px;
  display: inline-block;
  margin-left: 20px;
} */

#button_vac {
  padding: 0 20px;
  border: 1px solid #E8E7E7;
  margin: 0 auto;
  margin-bottom: 20px;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  background: #E8E7E7;
  /* margin-top: 20px; */
  /* position: relative; */
}

.button_vac_text {
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

ul {
  /* margin-top: 0; */
  min-height: calc(100% - 3rem);
  
}
</style>
