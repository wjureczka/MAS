<template>
  <div id="app">
    <Header/>
    <div class="viewport">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header'

export default {
  name: 'App',
  components: {
    Header
  }
}
</script>

<style lang="scss">
  @import '@/assets/reset.scss';
  @import '@/assets/fluiditype.scss';

  .viewport {
    max-width: 1024px;
    margin: auto;
  }
</style>
