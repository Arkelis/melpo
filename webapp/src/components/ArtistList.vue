<template>
  <div>
    <h1>Artistes</h1>
    <ul id="artist-list">
        <li v-for="artist in artists" :key="artist.id" class="artist-box box">
            <h4 class="artist-box__name">{{ artist.name }}</h4>
        </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ArtistList',
  data() {
    return {
      artists: []
    }
  },
  created() {
    this.$http.get("http://localhost:8000/artistes/").then((response) => {
      this.artists = response.data
    })
  }
}
</script>

<style scoped lang="scss">
.artist-box__name {
    text-align: center;
    text-transform: uppercase;
    padding: 0;
    margin: 0;
    transition: opacity 0.4s;
}

#artist-list {
    display: grid;
    grid-gap: 1.5em;
    grid-template-columns: repeat(6, 1fr);
    margin: 1em 0;
    justify-items: center;
}

.artist-box {
    display: flex;
    justify-content: center;
    align-content: center;
    justify-items: center;
    align-items: center;
    width: 200px;
    height: 200px;
    margin: 0 !important;
    padding: 20px;
    
    .artist-box__name {
        opacity: 0;
    }

    &:hover .artist-box__name {
        opacity: 1;
    }
}

/* Responsive */
@media screen and (max-width: calc((200px + 1.5em) * 5)) {
    #artist-list {
        grid-template-columns: repeat(5, 1fr);
    }
}

</style>
