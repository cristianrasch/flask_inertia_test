<template>
  <Layout>
    <h1>Your are on the '{{ msg }}' page.</h1>
  </Layout>
</template>

<script>
import Layout from './Layout'

export default {
  name: 'StaticPage',

  props: {
    msg: {
      type: String,
      required: true
    }
  },

  components: {
    Layout,
  },
};
</script>

