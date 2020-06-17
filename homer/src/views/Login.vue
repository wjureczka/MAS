<template>

  <div class="login">
    <h1 class="login__title">
      Login into your account
    </h1>

    <form class="login__form form">

      <label for="email">Email</label>
      <input id="email" type="email">

      <label for="password">Password</label>
      <input id="password" type="password">

      <button type="submit">Login</button>
    </form>
  </div>
</template>

<style lang="scss">
  .login {
    width: 100%;

    &__title {

    }

    &__form {
      margin: auto;
      display: flex;
      flex-direction: column;
      max-width: 320px;
    }
  }
</style>
