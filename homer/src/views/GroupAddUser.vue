<template>
  <div class="add-user">
    <h1 class="add-user__title">Dodaj użytkownika</h1>

    <form class="add-user__form form" @submit="(event) => handleOnSubmit(event, id)">

      <h3 class="form__title">
        Podaj email użytkownika
      </h3>

      <input class="form__input" id="email" type="email"/>

      <button class="form__button" type="submit">Dodaj</button>
    </form>
  </div>
</template>
<script>
import { postNewUserToGroup } from '@/api'

const handleOnSubmit = async (event, id) => {
  event.preventDefault()

  const { email } = event.target.elements

  await postNewUserToGroup({ groupId: id, email: email.value })
    .then(() => {
      alert('succ')
    })
    .catch(() => {
      alert('fail')
    })
}

export default {
  name: 'GroupCreated',
  props: ['id'],
  methods: {
    handleOnSubmit
  }
}
</script>

<style lang="scss">
  @import '@/assets/colors';

  .add-user {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    margin-top: 50px;

    &__title {
      color: $primary-heading;
      margin-bottom: 50px;
    }

    &__form {
      background: $primary-background;
      padding: 25px;
      color: white;
      margin: auto;
      text-align: center;
    }

    .form {
      display: flex;
      flex-direction: column;

      &__input {
        margin: 20px 0;
      }

      &__button{
        background: $call-to-action-background;
        border: none;
        color: white;
        width: 40%;
        padding: 15px;
        font-size: 24px;
        margin: auto;
      }
    }
  }

</style>
