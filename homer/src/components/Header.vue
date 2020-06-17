<template>
  <header class="header">
    <nav class="nav">
      <ul class="nav__links">
        <li>
          A
        </li>

        <li>
          B
        </li>

        <li>
          C
        </li>

        <li>
          D
        </li>

        <li>
          E
        </li>
      </ul>

      <div class="nav__user">

      </div>
    </nav>
  </header>
</template>

<style lang="scss">
  .header {
    width: 100%;
    display: block;
    background: green;
  }

  .nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;

    &__links {
    justify-content: center;
    align-items: center;
    }

    &__user {
    justify-content: center;
    align-items: center;
    }
  }
</style>
