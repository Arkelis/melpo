<template>
  <div>
    <h1>Artistes</h1>
    <ul id="artist-list">
        <li v-for="artist in artists" :key="artist.id" class="artist-box box" :style="{backgroundImage: `url(${artist.picture_url})`, backgroundSize: 'cover'}">
            <h4 class="artist-box__name"><span>{{ artist.name }}</span></h4>
        </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ArtistList',
  data() {
    return {
      artists: [],
    }
  },
  created() {
    this.$http.get("http://localhost:8000/artists/").then((response) => {
      this.artists = response.data
    })
  },
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
    grid-gap: 20px;
    grid-template-columns: repeat(6, 200px);
    margin: 1em 0;
    justify-items: center;
    justify-content: center;
}

.artist-box {
    width: 200px;
    height: 200px;
    margin: 0 !important;
    padding: 0;
    
    .artist-box__name {
        opacity: 0;
        display: flex;
        justify-content: center;
        align-content: center;
        justify-items: center;
        align-items: center;
        padding: 20px;
        height: 100%;
        width: 100%;
    }

    &:hover .artist-box__name {
        opacity: 1;
        background-color: rgba(117, 190, 218, 0.5); /* 0.5 - semi-transparent */
    }

    .artist-box__name span {
        vertical-align: middle;
    }
}

/* Responsive */
@media screen and (max-width: 1700px) {
    #artist-list {
        grid-template-columns: repeat(5, 200px);
    }
}

@media screen and (max-width: 1400px) {
    #artist-list {
        grid-template-columns: repeat(4, 200px);
    }
}

@media screen and (max-width: 1100px) {
    #artist-list {
        grid-template-columns: repeat(3, 200px);
    }
}

@media screen and (max-width: 800px) {
    #artist-list {
        grid-template-columns: 1fr;
    }

    .artist-box {
        width: 80%;
    }
}

</style>
