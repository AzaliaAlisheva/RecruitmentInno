<template>
  <div class="box_specialists">
    <div class="spec_data">
      <div class="spec_flags">
        <img class="ellipse1" :src="ellipse1Src" alt="ellipse" @click="changeOnGreen" width="20px" height="20px">
        <img class="ellipse2" :src="ellipse2Src" alt="ellipse" @click="changeOnRed" width="20px" height="20px">
      </div>
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
import { RouterLink } from 'vue-router';


interface Specialist {
  id: number;
  name: string;
  comment: string;
  mark: number;
  grade: string;
  stack: string;
}

interface Connect {
  "id": number,
  "overlap": null,
  "specmark": number,
  "vacancy": number,
  "specialist": number,
}

export default defineComponent({
  data() {
    return {
      ellipse1Src: require('@/img/greeninit.png'),
      ellipse2Src: require('@/img/redinit.png'),
      connectId: Number,
    };
  },
  async mounted() {
    this.getConnect();
  },
  name: 'SpecialistBox',

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
  components: {
    RouterLink
  },

  methods: {
    async updateSpecmark(newMark: number) {
      const response = await axios.patch('main/connect/' + this.connectId, { specmark: newMark });
      return response.data;
    },
    async changeOnRed() {
      const response = await axios.get('main/connect/' + this.connectId);
      let con = response.data as Connect;
      if (con.specmark == -1) {
        try {
          this.ellipse2Src = require('@/img/redpicked.png');
          this.ellipse1Src = require('@/img/greeninit.png');
          await axios.patch('main/connect/' + this.connectId + '/', { "specmark": 0 });
        }
        catch (error) {
          console.error(error);
        }
      } else {
        this.ellipse2Src = require('@/img/redinit.png');
        await axios.patch('main/connect/' + this.connectId + '/', { "specmark": -1 });
      }
    },

    async changeOnGreen() {
      const response = await axios.get('main/connect/' + this.connectId);
      let con = response.data as Connect;
      if (con.specmark == -1) {
        try {
          this.ellipse1Src = require('@/img/greenpicked.png');
          this.ellipse2Src = require('@/img/redinit.png');
          await axios.patch('main/connect/' + this.connectId + '/', { "specmark": 1 });
        } catch (error) {
          console.error(error);
        }
      } else {
        this.ellipse1Src = require('@/img/greeninit.png');
        await axios.patch('main/connect/' + this.connectId + '/', { "specmark": -1 });

      }
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

<style>
.box_specialists {
  padding: 0px;
  border: 1px solid rgb(199, 198, 198);
  margin-bottom: 20px;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  background: rgb(199, 198, 198);
  display: flex;
  justify-content: center;
  position: relative;
}

.spec_flags {
  position: absolute;
  flex-direction: row;
  left: 20px;
  top: 15px;
  gap: 5px;
}

.spec_data {
  display: flex;
}

.spec_data.text {
  padding-left: 15px;
  padding-right: 15px;
}

.ellipse {
  position: absolute;
  left: 20px;
  top: 18px;
}

.text {
  display: relative;
  flex-direction: column;
  display: flex;
  padding-left: 73px;
  align-items: flex-start;
}
</style>