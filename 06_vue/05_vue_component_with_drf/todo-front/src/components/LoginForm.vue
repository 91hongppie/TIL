<template>
  <div class='login-div'>
    <div v-if="loading" class="spinner-border text-danger" role="status">
      <span class="sr-only">Loading...</span>
    </div>
    <form v-else class="login-form" @submit.prevent="login">
      <div v-if="errors.length" class="error-list alert alert-danger">
        <h4>다음의 오류를 해결해주세요</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">
          {{ error }}
        </div>
      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input 
        type="text" 
        class="form-control" 
        id="id" 
        placeholder="아이디를 입력해주세요."
        v-model="credentials.username"
        >
      </div>
      <div class="form-group">
        <label for="password">PASSWORD</label>
        <input 
        type="password" 
        class="form-control" 
        id="password" 
        placeholder="비밀번호를 입력해주세요."
        v-model="credentials.password"
        >
      </div>
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script>
  import axios from 'axios'
  import router from '../router'

  export default {
    name: 'LoginForm',
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        },
        // loading: false,
        errors: [],
      }
    },
    computed: {
      loading: function() {
        return this.$store.state.loading
      }
    },
    methods: {
      login() {
        if (this.checkForm()) {
          // 1. django jwt 를 생성하는 주소로 요청을 보냄
          // 이때 post 요청으로 보내야하며 사용자가 입력한 로그인 정보(credentials)를 같이 넘겨야 함
          // this.loading = true
          this.$store.dispatch('startLoading')
          axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
          .then(res => {
            // this.$session.start()
            // this.$session.set('jwt', res.data.token)
            // import router from '../router' 하고 사용한다. '/' 는 index.js 에서 home path
            this.$store.dispatch('endLoading')
            this.$store.dispatch('login', res.data.token)
            router.push('/')
            // 2. 로그인 이후에 loading 의 상태를 다시 false 로 변경
            // 그래야 spinner 가 계속 돌지 않고 로그인 form 을 받아 볼 수 있음
            // this.loading = false
          })
          .catch(err => {
            // 3. 로그인 실패 시 loading 의 상태를 다시 false 로 변경
            // this.loading = false
            this.$store.dispatch('endLoading')
            console.log(err)
          })
        } else {
          console.log('로그인 검증 실패')
        }
      },
      checkForm() {
        this.errors = []
        if (!this.credentials.username) {
            this.errors.push("아이디를 입력해주세요.")
        }
        if (this.credentials.password.length < 8) {
          this.errors.push("비밀번호를 8자 이상 입력해주세요")
        }
        if (this.errors.length === 0) {
          return true
        }
      },
    }
  }
</script>

<style>

</style>