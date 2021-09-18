<template>
  <aside class="menu">
    <ul class="menu-list">
      <li class="my-5">
        <router-link
          class="mx-5"
          :to="{ name: 'Overview', params: { classroom_id: classroomId } }"
          >Overview</router-link
        >
      </li>
      <li class="my-5"><a class="mx-5">Rooms</a></li>
      <li class="my-5">
        <router-link
          class="mx-5"
          :to="{ name: 'Other', params: { classroom_id: classroomId } }"
          >Orders</router-link
        >
      </li>
    </ul>
  </aside>
</template>

<script>
export default {
  props: ["classroomId"],
  created() {},
};
</script>

<style>
</style>