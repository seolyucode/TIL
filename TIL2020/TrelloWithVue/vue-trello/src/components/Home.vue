<template>
  <div>
    Home
    <div>
        Board List:
        <div v-if="loaindg">로딩 중..</div>
        <div v-else>
          Api result: <pre>{{apiRes}}</pre>
        </div>
        <div v-if="error"><pre>{{error}}</pre></div>
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
import axios from 'axios'

export default {
  data() {
    return {
      loading: false,
      apiRes: '',
      error: ''
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.loading = true

      axios.get('https://server-msvml.run.goorm.io/_health')
        .then(res => {
          this.apiRes = res.data
        })
        .catch(res => {
          this.error = res.response.data
        })
        .finally(() => {
          this.loading = false
        })

      // const req = new XMLHttpRequest()
      // req.open('GET', 'https://server-msvml.run.goorm.io/health')
      // req.send()
      // req.addEventListener('load', () => {
      //   this.loading = false
      //   this.apiRes = {
      //     status: req.status,
      //     statusText: req.statusText,
      //     response: JSON.parse(req.response)
      //   }
      // })
    }
  }
}
</script>

<style>

</style>
