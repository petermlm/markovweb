<template>
  <div id="app">
    <Markov/>
  </div>
</template>

<script>
import Markov from './components/Markov.vue'

export default {
  name: 'app',
  components: {
    Markov
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
