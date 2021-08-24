<template>
  <div id="Markov">
    <md-tabs md-sync-route>
      <md-tab id="tab-text" md-label="Text" to="/">
        <router-view/>
      </md-tab>
      <md-tab id="tab-redit" md-label="Reddit" to="/reddit" class="md-primary">
        <router-view/>
      </md-tab>
    </md-tabs>
  </div>
</template>

<script>
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(VueMaterial)

export default {
  name: 'Markov',
  components: {
  }
}
</script>
