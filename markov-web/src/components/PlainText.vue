<template>
  <div id="PlainText">
    <h1 id="title">Plain Text</h1>
    <form
      id="markov-form"
      @submit.prevent="submit"
      method="post"
    >
      <md-field>
        <md-textarea v-model="input" maxlength="10000"></md-textarea>
      </md-field>

      <OutputSize ref="OutputSize"/>

      <div id="markov-form-buttons">
        <md-button class="md-raised" v-if="results_lenth" v-on:click="clear">Clear</md-button>
        <md-button type="submit" class="md-raised md-primary">Submit</md-button>
      </div>
    </form>

    <Results ref="results" res-type="PlainText"/>

    <md-snackbar :md-position="position" :md-duration="error_duration" :md-active.sync="show_snackbar" md-persistent>
      <span>{{ error }}</span>
      <md-button class="md-primary" @click="show_snackbar = false">Close</md-button>
    </md-snackbar>
  </div>
</template>

<style scoped>
#title {
  text-align: center;
}

#markov-form-buttons {
  text-align: right;
}

#output-table {
  margin-top: 26px;
}

.output-timestamp {
  width: 180px;
}
</style>

<script>
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

import OutputSize from './OutputSize.vue'
import Results from './Results.vue'
import { requestPlainText } from '../requests'

Vue.use(VueMaterial)

export default {
  name: 'PlainText',

  components: {
    OutputSize,
    Results
  },

  data () {
    return {
      input: '',
      results_lenth: 0,

      show_snackbar: false,
      error: '',
      position: 'center',
      error_duration: 2000
    }
  },

  methods: {
    submit: function () {
      if (this.input === '') {
        return
      }

      var outputSize = this.$refs.OutputSize.get_size()

      requestPlainText(this.input, outputSize)
        .then(function (text) {
          this.$refs.results.add(text)
          this.results_lenth = this.$refs.results.count()
        }.bind(this))
        .catch(function () {
          this.show_snackbar = true
          this.error = 'No connection.'
        }.bind(this))
    },

    clear: function () {
      this.input = ''
      this.$refs.results.clear()
      this.results_lenth = this.$refs.results.count()
    }
  }
}
</script>
