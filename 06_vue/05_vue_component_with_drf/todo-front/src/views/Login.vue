<template>
  <div>
    <LoginForm/>
  </div>
</template>

<script>
  // @ 는 '/src' 의 alias
  // import LoginForm from '../components/LoginForm'
  import LoginForm from '@/components/LoginForm'
  export default {
    name: 'Login',
    components: {
      LoginForm,
    }
  }
</script>

<style>

</style>