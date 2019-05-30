<template>
  <div class="Footer">
    MarkovWeb - &copy; Pedro Melgueira, {{cyear}}
  </div>
</template>

<style>
.Footer {
  color: #5a5a5a;
  font-size: smaller;
  margin-top: 32px;
  text-align: center;
}
</style>

<script>
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(VueMaterial)

export default {
  name: 'Footer',
  data () {
    return {cyear: (new Date()).getFullYear()}
  }
}
</script>
