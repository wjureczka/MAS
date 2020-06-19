<template>
  <div class="group-created">
    <h1 class="group-created__title">Sukces!</h1>

    <div class="group-created__modal modal">

      <h3 class="modal__title">
        Sukces!
      </h3>

      <p class="modal__copy">
        Czy chcesz dodać użytkownika do grupy?
      </p>

      <div class="modal__actions">
        <router-link class="modal__button" :to="`/groups/${id}/add-user`">Tak</router-link>
        <router-link class="modal__button" :to="'/groups'">Nie</router-link>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'GroupCreated',
  props: ['id']
}
</script>

<style lang="scss">
  @import '@/assets/colors';

  .group-created {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    margin-top: 50px;

    &__title {
      color: $primary-heading;
      margin-bottom: 50px;
    }

    &__modal {
      background: $primary-background;
      padding: 25px;
      color: white;
      margin: auto;
      text-align: center;
    }

    .modal {
      &__copy {
        margin: 25px 0;
      }

      &__actions {
        display: flex;
        justify-content: space-between;
      }

      &__button{
        background: $call-to-action-background;
        border: none;
        color: white;
        width: 40%;
        padding: 15px;
        font-size: 24px;
      }
    }
  }

</style>
