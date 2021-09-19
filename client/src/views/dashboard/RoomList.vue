<template>
  <div>
    <div class="box" v-for="room in rooms" :key="room.id">
      Room - {{ room.title }}
      <p>Schedule on - {{ room.schedule_on }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["classroom_id"],
  data() {
    return {
      rooms: null,
    };
  },
  created() {
    axios
      .get(`${process.env.VUE_APP_API_URL}/api/rooms/list`, {
        params: {
          classroom_id: this.classroom_id,
        },
      })
      .then(({ data }) => (this.rooms = data))
      .catch((e) => console.log(e));
  },
};
</script>

<style>
</style>