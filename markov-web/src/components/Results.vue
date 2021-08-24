<template>
  <div id="Results">
    <md-table id="output-table" v-model="output" v-if="output.length">
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell class="output-timestamp" md-label="Timestamp">{{ item.timestamp }}</md-table-cell>
        <md-table-cell md-label="Generated Text">{{ item.text }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<style scoped>
</style>

<script>
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import moment from 'moment'
import store from 'store'

Vue.use(VueMaterial)

export default {
  name: 'Results',

  props: ['res-type'],

  data () {
    return {
      output: [],

      error: '',
      error_duration: 2000
    }
  },

  mounted () {
    if (store.get(this.storeKey())) {
      this.loadOutput()
    } else {
      this.output = []
    }
  },

  methods: {
    add: function (resText) {
      var ele = {
        'text': resText,
        'timestamp': this.formatTimestamp()
      }

      this.output.splice(0, 0, ele)

      if (this.output.length > 10) {
        this.output.pop()
      }

      this.saveOutput()
    },

    clear: function () {
      this.output = []
      this.saveOutput()
    },

    formatTimestamp: function () {
      return moment().format('MMMM Do YYYY, h:mm:ss a')
    },

    saveOutput: function () {
      store.set(this.storeKey(), JSON.stringify(this.output))
    },

    loadOutput: function () {
      this.output = JSON.parse(store.get(this.storeKey()))
    },

    storeKey: function () {
      return 'results-' + this.resType
    },

    count: function () {
      return this.output.length
    }
  }
}
</script>
