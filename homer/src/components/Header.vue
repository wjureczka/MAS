<template>
  <header class="header">
    <nav class="nav">
      <ul class="nav__links">
        <li>
          <router-link class="nav__link" to="/search">
            Szukaj
          </router-link>
        </li>

        <li>
          <router-link class="nav__link" to="/agreement">Twoje umowy</router-link>
        </li>

        <li>
          <router-link class="nav__link" to="/rental-objects">Twoje obiekty</router-link>
        </li>

        <li>
          <router-link class="nav__link" to="/groups">Twoje grupy</router-link>
        </li>
      </ul>

      <div class="nav__user user">
        <img class="user__avatar" src="https://api.adorable.io/avatars/285/abott@adorable.pngCopy to Clipboard"/>

        <a class="user__name" href="#">Hej, Ziomek!</a>

        <span class="mdi mdi-chevron-down"/>
      </div>
    </nav>
  </header>
</template>

<style lang="scss">
  @import '@/assets/colors';

  .header {
    width: 100%;
    display: block;
    background: $primary-background;
  }

  .nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;

    &__links {
      display: flex;
      justify-content: center;
      align-items: center;
    }

    &__link {
      margin: 0 10px;
      color: $primary-text;

      &.router-link-active {
        text-decoration: underline;
      }

      &:hover {
        color: $primary-text;
        text-decoration: underline;
      }

      &:first-of-type {
        margin-left: 0;
      }
    }

    &__user {
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .user {
      color: $primary-text;

      &:hover {
        color: $primary-text;
        text-decoration: underline;
        cursor: pointer;
      }

      & > * {
        margin: 0 8px;
      }

      &__avatar {
        max-width: 50px;
        border-radius: 50%;
        border: 2px solid lightblue;
      }

      &__name {
        color: $primary-text;
      }
    }
  }
</style>
