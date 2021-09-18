<template>
  <div>
    <Navbar />
    <div class="container">
      <div class="buttons">
        <button class="button is-primary">Primary</button>
        <button class="button is-link">Link</button>
      </div>

      <div class="buttons">
        <button class="button is-info">Info</button>
        <button class="button is-success">Success</button>
        <button class="button is-warning">Warning</button>
        <button class="button is-danger">Danger</button>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";

export default {
  name: "Home",
  components: { Navbar },
};
</script>
