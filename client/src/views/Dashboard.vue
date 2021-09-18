<template>
  <div>
    <div class="columns">
      <div class="column is-one-quarter">
        <Sidebar />
      </div>
      <div class="column">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "../components/Sidebar.vue";

export default {
  components: { Sidebar },
};
</script>

<style>
</style>