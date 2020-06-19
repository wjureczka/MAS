<template>
  <div class="group">
    <h3 class="group__name">
      {{ group.name }}
    </h3>

    <ul>

      <li>
        Metraz: {{ group.preferred_size }}
      </li>

      <li>
        Liczba pokoi: {{ group.preferred_room_quantity }}
      </li>

      <li>
        Budżet: {{ group.preferred_budget }}
      </li>

      <li>
        Lokalizacja: {{ group.preferred_locations }}
      </li>
    </ul>

    <span class="separator"/>

    <h6>Członkowie</h6>
    <ul class="avatars">
      <li v-for="user in group.users" :key="user.id">
        <img class="avatars__item" src="https://api.adorable.io/avatars/30/abott@adorable.png" />
      </li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'Group',
  props: [
    'group'
  ]
}
</script>

<style lang="scss">
  @import '@/assets/colors';

  .group {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 10px;
    padding-top: 20px;
    background: $primary-background;
    color: white;

    &__name {
      margin-bottom: 20px;
    }

    .avatars {
      display: flex;
      justify-content: flex-start;
      flex-wrap: wrap;
      margin: 0 -10px;

      &__item {
        margin: 0 5px;
        border-radius: 50%;
        border: 2px solid white;
      }
    }
    .separator {
      margin: 10px 0;
      height: 2px;
      width: 100%;
      background: white;
    }
  }

</style>
