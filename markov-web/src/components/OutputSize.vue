<template>
  <div id="OutputSize">
    <md-field>
      <label>Output Size</label>
      <md-input v-model="output_size" type="number" min="3" max="500"></md-input>
    </md-field>
  </div>
</template>

<script>
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(VueMaterial)

export default {
  name: 'OutputSize',

  data () {
    return {
      output_size: 100
    }
  },

  methods: {
    get_size: function () {
      return Number(this.output_size);
    }
  }
}
</script>
