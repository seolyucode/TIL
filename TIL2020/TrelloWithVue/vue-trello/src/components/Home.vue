<template>
  <div>
    Home
    <div>
        Board List:
        <div v-if="loaindg">로딩 중..</div>
        <div v-else>
          Api result: {{apiRes}}
        </div>
        <ul>
            <li>
                <router-link to="/b/1">Board 1</router-link>
            </li>
            <li>
                <router-link to="/b/2">Board 2</router-link>
            </li>
        </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
      apiRes: ''
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.loading = true

      const req = new XMLHttpRequest()

      req.open('GET', 'https://server-msvml.run.goorm.io/health')

      req.send()

      req.addEventListener('load', () => {
        this.loading = false
        this.apiRes = {
          status: req.status,
          statusText: req.statusText,
          response: JSON.parse(req.response)
        }
      })
    }
  }
}
</script>

<style>

</style>
