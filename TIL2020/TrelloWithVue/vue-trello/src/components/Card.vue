<template>
  <div>
      Card
      <div v-if="loading">로딩 카드</div>
      <div v-else>
        <div>cid: {{cid}}</div>
      </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            cid: 0,
            loading: false
        }
    },
    watch: {
        '$route': {
            handler: 'fetchData',
            immediate: true
        }
    },
    methods: {
        fetchData() {
            this.loading = true
            setTimeout(() => {
                this.cid = this.$route.params.cid
                this.loading = false
            }, 500)
        }
    }
}
</script>

<style>

</style>