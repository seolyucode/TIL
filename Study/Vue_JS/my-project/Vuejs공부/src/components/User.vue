<template>
  <div class="blue lighten-3 pa-3">
    <h1>User 컴포넌트</h1>
    <p>이름: {{ name }}</p>
    <!-- <button @click="changeName()">이름 변경</button> -->
    <v-col cols="12" sm="3">
      <v-btn text icon color="pink" @click="changeName()">
        <v-icon>이름 변경</v-icon>
      </v-btn>
    </v-col>
    <hr>
    <v-layout row wrap>
      <v-flex xs12 sm6>
        <UserDetail :nameOfChild="name"></UserDetail>
      </v-flex>
      <v-flex xs12 sm6>
        <UserEdit></UserEdit>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
  import UserDetail from "./UserDetail.vue"
  import UserEdit from "./UserEdit.vue"

  export default {
    components: {
      UserDetail,
      UserEdit
    },
    data() {
      return {
        name: '뷰 제이에스'
      }
    },
    methods: {
      changeName() {
        this.name = "Hoza"
      }
    }
  }
</script>