<template>
  <div id="Markov">
    <md-tabs>
      <md-tab id="tab-text" md-label="Text">
        <PlainText/>
      </md-tab>
      <md-tab id="tab-redit" md-label="Reddit">
        <Reddit/>
      </md-tab>
    </md-tabs>
  </div>
</template>

<script>
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

import PlainText from './PlainText.vue'
import Reddit from './Reddit.vue'

Vue.use(VueMaterial)

export default {
  name: 'Markov',
  components: {
    PlainText,
    Reddit,
  }
}
</script>
