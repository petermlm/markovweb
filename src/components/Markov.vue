<template>
  <div id="Markov">
    <h1 id="title">Markov</h1>
    <form
      id="markov-form"
      @submit.prevent="submitMarkov"
      action="localhost:5000"
      method="post"
    >
      <md-field>
        <md-textarea v-model="input" maxlength="5000"></md-textarea>
      </md-field>

      <div id="markov-form-buttons">
        <md-button class="md-raised" v-if="output.length" v-on:click="clearMarkov">Clear</md-button>
        <md-button type="submit" class="md-raised md-primary">Submit</md-button>
      </div>
    </form>

    <md-table id="output-table" v-model="output" v-if="output.length">
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell class="output-timestamp" md-label="Timestamp">{{ item.timestamp }}</md-table-cell>
        <md-table-cell md-label="Generated Text">{{ item.text }}</md-table-cell>
      </md-table-row>
    </md-table>
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
import axios from 'axios'
import moment from 'moment'

Vue.use(VueMaterial)

let MarkovUrl = 'localhost:5000'

export default {
  name: 'Markov',

  data () {
    return {
      input: '',
      output: [],
    }
  },

  mounted () {
    if(localStorage.output) {
      this.loadOutput();
    } else {
      this.output = [];
    }
  },

  methods: {
    submitMarkov: function () {
      if(this.input == '') {
        return;
      }

      this.request();
    },

    clearMarkov: function () {
      this.output = [];
      this.saveOutput();
    },

    request: function () {
      var text = this.input;
      axios.post(MarkovUrl, {'text': text})
        .then(response => {
          this.output.splice(0, 0, response['text']);

          if(this.output.length > 10) {
            this.output.pop();
          }

          this.saveOutput();
        })
        .catch(e => {
          this.errors.push(e)
        })
    },

    formatTimestamp: function (ts) {
      return moment(ts).format('MMMM Do YYYY, h:mm:ss a')
    },

    saveOutput: function () {
      localStorage.output = JSON.stringify(this.output);
    },

    loadOutput: function () {
      this.output = JSON.parse(localStorage.output);
    },
  }
}
</script>
