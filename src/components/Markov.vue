<template>
  <div id="Markov">
    <h1>Markov</h1>
    <form
      id="markov-form"
      @submit.prevent="submitMarkov"
      action="localhost:5000"
      method="post"
    >
      <md-field>
        <label>Textarea</label>
        <md-textarea v-model="input" md-counter="80"></md-textarea>
      </md-field>

      <md-button type="submit" class="md-raised">Submit</md-button>
    </form>

    <md-table v-model="output">
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="Output">{{ item.text }}</md-table-cell>
        <md-table-cell md-label="Copy">Copy</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<style scoped>
#Markov {
  width: 75%;
}
</style>

<script>
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import axios from 'axios'

Vue.use(VueMaterial)

let MarkovUrl = 'localhost:5000'

function Request (text, assign) {
  assign('fdsa')
  axios.post(MarkovUrl, {'text': text})
    .then(response => {
      assign(response['text'])
    })
    .catch(e => {
      this.errors.push(e)
    })
}

export default {
  name: 'Markov',

  data () {
    return {
      input: '',
      output: [{'text': 'ai'}, {'text': 'ui'}],
    }
  },

  methods: {
    submitMarkov: function () {
      Request(this.input, output => {
        this.output.push(output)
      })
    }
  }
}
</script>
