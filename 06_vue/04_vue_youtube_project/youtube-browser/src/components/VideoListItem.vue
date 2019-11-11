<template>
  <div>
    <li @click="onVideoSelect" class="list-group-item">
      <img :src="thumbnailUrl" alt="image" />
      <div class="media-body" v-html="video.snippet.title"></div>
    </li>
  </div>
</template>

<script>
export default {
  name: "VideoListItem",
  props: {
    video: {
      type: Object,
      required: true
    }
  },
  methods: {
    onVideoSelect() {
      this.$emit("videoSelect", this.video); // $emit('videoSelect', ) videoSelect 올릴 이벤트 이름
    }
  },
  computed: {
    // 미리 캐싱
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url;
    }
  }
};
</script>

<style scoped>
li {
  display: flex;
  cursor: pointer;
}

li:hover {
  background-color: antiquewhite;
}
</style>