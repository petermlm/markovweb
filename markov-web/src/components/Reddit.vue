<template>
  <div id="Reddit">
    <h1 id="title">Reddit</h1>
    <form
      id="markov-form"
      @submit.prevent="submit"
      method="post"
    >
      <md-field id="input">
        <label>Reddit Username</label>
        <md-input v-model="input"></md-input>
      </md-field>

      <div id="markov-form-buttons">
        <md-button class="md-raised" v-if="results_lenth" v-on:click="clear">Clear</md-button>
        <md-button type="submit" class="md-raised md-primary">Submit</md-button>
      </div>
    </form>

    <Results ref="results" res-type="Reddit"/>

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
</style>

<script>
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

import Results from './Results.vue'
import { request_reddit } from '../requests'

Vue.use(VueMaterial)

export default {
  name: 'Reddit',

  components: {
    Results,
  },

  data () {
    return {
      input: '',
      results_lenth: 0,

      show_snackbar: false,
      error: '',
      position: 'center',
      error_duration: 2000,
    }
  },

  methods: {
    submit: function () {
      if(this.input == '') {
        return;
      }

      request_reddit(this.input)
        .then(function (text) {
          this.$refs.results.add(text);
          this.results_lenth = this.$refs.results.count();
        }.bind(this))
        .catch(function () {
          this.show_snackbar = true;
          this.error = 'No connection.';
        }.bind(this));
    },

    clear: function () {
      this.input = '';
      this.$refs.results.clear();
      this.results_lenth = this.$refs.results.count();
    },
  }
}
</script>
