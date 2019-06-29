<template>
  <div class="content" id="app">
    <ArtistList class="container"/>
  </div>
</template>

<script>
import ArtistList from './components/ArtistList.vue'

export default {
  name: 'app',
  components: {
    ArtistList
  }
}
</script>

<style>
@import "~bulma/css/bulma.css";

.content h1 {
    margin-top: 2em;
    margin-bottom: 1em;
}
</style>
