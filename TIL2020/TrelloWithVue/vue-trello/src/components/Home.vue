<template>
  <div>
    Home
    <div>
        Board List:
        <div v-if="loaindg">로딩 중..</div>
        <div v-else>
          <div v-for="b in boards" :key="b.id">
            {{b}}
          </div>
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
import axios from 'axios'

export default {
  data() {
    return {
      loading: false,
      boards: [],
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.loading = true

      axios.get('https://server-msvml.run.goorm.io/boards')
        .then(res => {
          this.boards = res.data
        })
        .catch(res => {
          this.$router.replace('/login')
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
