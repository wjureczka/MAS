<template>
  <div class="new-group">
    <h1 class="new-group__title">Dodaj nową grupę</h1>

    <form class="new-group__form" @submit="handleOnSubmit">

      <h4 class="new-group__form-title">Wprowadź dane</h4>

      <label for="preferred_budget">Preferowany budżet</label>
      <input class="new-group__form-input" id="preferred_budget" type="number" value="0"/>

      <label for="preferred_size">Preferowany metraż</label>
      <input class="new-group__form-input" id="preferred_size" type="number" value="0"/>

      <label for="preferred_room_quantity">Preferowana liczba pokoi</label>
      <input class="new-group__form-input" id="preferred_room_quantity" type="number" value="0"/>

      <label for="preferred_locations">Preferowana lokalizacja</label>
      <input class="new-group__form-input" id="preferred_locations"/>

      <label for="group_name">Nazwa grupy</label>
      <input class="new-group__form-input" id="group_name"/>

      <button class="new-group__form-submit" type="submit">Utwórz</button>
    </form>

  </div>
</template>

<script>
import { postNewGroup } from '@/api'
import router from '@/router'

const handleOnSubmit = async (event) => {
  event.preventDefault()

  const form = event.target

  const {
    // eslint-disable-next-line camelcase
    group_name,
    // eslint-disable-next-line camelcase
    preferred_locations,
    // eslint-disable-next-line camelcase
    preferred_room_quantity,
    // eslint-disable-next-line camelcase
    preferred_size,
    // eslint-disable-next-line camelcase
    preferred_budget
  } = form.elements

  await postNewGroup({
    group_name: group_name.value,
    preferred_locations: preferred_locations.value,
    preferred_room_quantity: preferred_room_quantity.value,
    preferred_size: preferred_size.value,
    preferred_budget: preferred_budget.value
  })
    .then(({ data }) => {
      router.push(`/groups/${data.group_id}/group-created`)
      return data
    })
    .catch(() => {
      alert('Fail')
    })
}

export default {
  name: 'NewGroupForm',
  methods: {
    handleOnSubmit
  }
}

</script>

<style lang="scss">
  @import '@/assets/colors';

  .new-group {
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
      margin: auto;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      background: $primary-background;
      color: white;
      padding: 20px 40px;
    }

    &__form-title {
      margin-bottom: 25px;
    }

    &__form-input {
      margin-bottom: 20px;
    }

    &__form-submit {
      background: $call-to-action-background;
      border: none;
      color: white;
      width: 100%;
      padding: 15px;
      font-size: 24px;
    }
  }

</style>
