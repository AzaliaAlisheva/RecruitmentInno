<template>
  <div>
    <div class="box_spec">
      <div class="text">
        <h2>Specialist Description</h2>
        <p> Name: {{ specialist.name }}</p>
        <p> Grade: {{ specialist.grade }}</p>
        <p> Stack: {{ specialist.stack }}</p>
        <!-- <p> instruments: {{ specialist.instruments }}</p> -->
        <p> Experience: {{ specialist.experience }}</p>
        <p> Location: {{ specialist.location }}</p>
        <p> Regularity: {{ specialist.is_regular_staff }}</p>
        <p> Working mode: {{ specialist.full_of_part_time }}</p>
        <p> Rate: {{ specialist.rate }}</p>
        <p> Contacts: {{ specialist.contact }}</p>
        <p> Date: {{ specialist.date }}</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
// import { useRoute, RouterLink } from 'vue-router';

interface Specialist {
  id: number;
  name: string;
  comment: string;
  mark: number;
  grade: string;
  stack: string;
  instruments: string;
  experience: string;
  location: string;
  is_regular_staff: string;
  full_of_part_time: string;
  rate: string;
  contact: string;
  date: Date;
}

// interface Vacancy {
//   id: number;
//   comment: string;
//   grade: string;
//   stack: string;
//   full_message: string;
//   // добавьте другие поля, если необходимо
// }

export default defineComponent({
  name: 'SpecDescription',
  components: {
  },
  data() {
    return {
      specialist: {} as Specialist,
    };
  },
  async mounted() {
    await this.getSpecDesc();
  },
  props: {
    specialistId: {
      type: String,
      required: true,
    },
    // specialist: {
    //   type: Object as PropType<Specialist>,
    //   required: true
    // },
    vacancyid: {
      type: Number,
      required: true,
    },
    id: String,

  },
  methods: {
    async getSpecDesc() {
      try {
        const response = await axios.get(`main/specialists/` + this.id);
        this.specialist = response.data as Specialist;
      } catch (error) {
        console.error(error);
      }
    },
  },
});
</script>

<style scoped>
.box_spec {
  border: 1px solid #494949;
  margin-bottom: 8px;
  background: rgb(190, 190, 190);
  border-radius: 7px;
  box-shadow: inset 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  width: 1285px;
  height: auto;
  margin-left: auto;
  margin-right: auto;
  margin-top: 30px;
  margin-bottom: 30px;
  display: flex;
  justify-content: center;
  padding-left: 25px;
}

.text {
  color: black;
  font-family: 'League Spartan';
  font-size: 22px;
  font-weight: 400;
  line-height: 22px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  line-height: 50px;
}

@media (width: 1024px) {
  .box_spec {
    width: 650px;
    height: 884;
  }

  .text {
    font-size: 18px;
  }
}

@media (width: 1280px) {
  .box_spec {
    width: 850px;
  }
}

@media (width: 1440px) {
  .box_spec {
    width: 980px;
  }
}

@media (width: 2560px) {
  .box_spec {
    width: 1000px;
  }

  .text {
    font-size: 32px;
  }
}

@media (width: 3840px) {
  .box_spec {
    width: 1450px;
    height: auto;
  }

  .text {
    font-size: 46px;
  }
}
</style>
