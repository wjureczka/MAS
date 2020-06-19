<template>
  <div class="groups">
    <h1 class="groups__title">Twoje grupy</h1>

    <ul class="groups__list">

      <li class="groups__list-element">

      </li>

      <li class="groups__list-element">
        <div class="groups__add-new">
          <span class="mdi mdi-plus"/>
        </div>
      </li>

    </ul>
  </div>
</template>

<script>

import { getGroups } from '@/api'

export default {
  name: 'Groups',
  data: function () {
    return {
      groups: []
    }
  },
  async beforeCreate () {
    await getGroups()
      .then((data) => {
        this.groups = data
        return data
      })
      .catch(
        (error) => {
          console.error(error)
        }
      )
  }
}

</script>

<style lang="scss">
  @import '@/assets/colors';

  .groups {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    margin-top: 50px;

    &__title {
      color: $primary-heading;
      margin-bottom: 50px;
    }

    &__list {
      width: 100%;
      display: flex;
      flex-wrap: wrap;
      margin: -10px;
    }

    &__list-element {
      margin: 10px;
      width: 22%;
      position: relative;
      box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);

      &:before {
        content: "";
        float: left;
        padding-top: 100%;
        font-size: 0;
      }
    }

    &__add-new {
      display: flex;
      justify-content: center;
      align-items: center;
      background: $primary-background;
      height: 100%;

      &:hover {
        cursor: pointer;
      }

      .mdi.mdi-plus {
        color: white;
        font-size: 10vw;
      }
    }
  }

</style>
