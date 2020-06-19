<template>
  <div class="groups">
    <h1 class="groups__title">Twoje grupy</h1>

    <ul class="groups__list">

      <li class="groups__list-element" v-for="group in groups" :key="group.id">
        <Group v-bind:group="group"/>
      </li>

      <li class="groups__list-element">
        <div class="groups__add-new">
          <router-link to="/groups/new-group-form">
            <span class="mdi mdi-plus"/>
          </router-link>
        </div>
      </li>

    </ul>
  </div>
</template>

<script>

import { getGroups } from '@/api'
import Group from '@/components/Group'

export default {
  name: 'Groups',
  components: { Group },
  data: function () {
    return {
      groups: []
    }
  },
  async beforeCreate () {
    await getGroups()
      .then(({ data }) => {
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
      flex: 1 1 100%;
      margin: 10px;
      max-width: 30%;
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
