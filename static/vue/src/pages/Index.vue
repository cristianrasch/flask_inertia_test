<template>
  <!--Layout-->
    <div class="content">
      <img class="logo" src="https://flask.palletsprojects.com/en/2.0.x/_static/flask-icon.png" alt="Flask logo">
      <img class="logo" src="https://avatars.githubusercontent.com/u/47703742?s=200&v=4" alt="Inertia logo">
      <img class="logo" src="https://vuejs.org/images/logo.png" alt="Vue logo">

      <h1 class="title">Welcome to your Flask-Inertia {{ frameworkName }} app.</h1>

      <p class="info">
        For more information please visit the
        <a href="https://flask-inertia.readthedocs.io/">documentation</a>
      </p>
    </div>
  <!--/Layout-->
</template>

<script>
// import Layout from './Layout'

export default {
  name: 'Index',

  // layout: Layout,

  data() {
    return {
      frameworkName: 'Vue'
    }
  },

  /*components: {
    Layout,
  },*/
};
</script>

<style lang="scss">
.content {
  width: 75%;
  margin: auto;
  text-align: center;
  font-family: Georgia, Cambria;

  & > .logo { max-height: 5em; margin: 0 10pt; }
  & > .info { color: #787878; }
}
</style>
