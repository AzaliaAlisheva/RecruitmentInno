<template>

  <div class="box_specialists">
    <div class="spec_data">
      <img class="ellipse" :src="ellipse1Src" alt="ellipse" @click="changeOnGreen" width="20px" height="20px">
      <div class="text">
        <p>{{ specialist.name }}</p>
        <p>{{ specialist.grade }}</p>
        <p>{{ specialist.stack }}</p>
        <RouterLink :to="`/specialists/${specialist.id}/`">
          <p>More Info...</p>
        </RouterLink>
      </div>
    </div>
  </div>

</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import axios from 'axios';

interface Specialist {
  id: number;
  name: string;
  comment: string;
  mark: number;
  grade: string;
  stack: string;
}

export default defineComponent({
  data() {
    return {
      ellipse1Src: require('@/img/greenpicked.png'),
      connectId: Number,
    };
  },
  async mounted() {
    this.getConnect();
  },
  name: 'SpecInPrBox',
  // это способ передачи данных от родительского компонента к дочернему компоненту в Vue.js.
  props: {
    specialist: {
      type: Object as PropType<Specialist>,
      required: true
    },
    vacancyid: {
      type: Number,
      required: true,
    },
  },
  methods: {
    async updateSpecmark(newMark: number) {
      const response = await axios.patch('main/connect/' + this.connectId, { specmark: newMark });
      return response.data;
    },
    async changeOnGreen() {
      this.ellipse1Src = require('@/img/greeninit.png');
      // const response = await axios.patch(`main/specialists/` + this.specialist.id + '/', { "mark": -1 });
      const response = await axios.patch('main/connect/' + this.connectId + '/', { "specmark": -1 });
      // return response.data;
      // this.updateSpecmark(-1);
    },
    async getConnect() {
      try {
        const response = await axios.get('main/connect/');
        for (const con of response.data) {
          const vacId = con.vacancy;
          if (vacId === this.vacancyid) {
            const specId = con.specialist;
            if (specId === this.specialist.id) {
              this.connectId = con.id;
            }
          }
        }
      } catch (error) {
        console.error(error);
      }
    },
  }
});
</script>