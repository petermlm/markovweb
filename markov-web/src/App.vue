<template>
  <div id="app">
    <Header/>
    <Markov/>
    <Footer/>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Markov from './components/Markov.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'app',
  components: {
    Header,
    Markov,
    Footer
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;

  max-width: 1100px;
  margin: 0 auto;
  padding: 0px 16px 16px 16px;
}
</style>
