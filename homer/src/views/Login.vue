<template>

  <div class="login">
    <h1 class="login__title">
      Login into your account
    </h1>

    <form class="login__form form" @submit="handleOnSubmit">

      <label for="email">Email</label>
      <input id="email" type="email">

      <label for="password">Password</label>
      <input id="password" type="password">

      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import { login } from '@/api'
import router from '@/router'

const handleOnSubmit = async (event) => {
  event.preventDefault()

  const form = event.target.elements

  await login({ email: form.email.value, password: form.password.value })
    .then(() => {
      alert('Success')
      router.push('/groups')
    })
    .catch(() => {
      alert('Fail')
    })
}

export default {
  name: 'Login',
  methods: {
    handleOnSubmit
  }
}
</script>

<style lang="scss">
  .login {
    width: 100%;

    &__title {
      margin: 50px 0;
    }

    &__form {
      margin: auto;
      display: flex;
      flex-direction: column;
      max-width: 320px;

      input {
        margin: 10px 0;
        margin-bottom: 30px;
      }
    }
  }
</style>
