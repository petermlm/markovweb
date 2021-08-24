import Vue from 'vue'

import Router from 'vue-router'
import PlainText from '@/components/PlainText.vue'
import Reddit from '@/components/Reddit.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'PlainText',
      component: PlainText
    },
    {
      path: '/reddit',
      name: 'Reddit',
      component: Reddit
    }
  ]
})
