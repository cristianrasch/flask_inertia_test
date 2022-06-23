<template>
  <main>
    <Head title="Welcome to my app!" />

    <header>
      <menu>
        <li><Link :href="$route('index')">Home</Link></li>
        <li><Link :href="$route('about')">About</Link></li>
        <li><Link :href="$route('contact')">Contact</Link></li>
      </menu>
    </header>

    <p v-for="(msg, i) in $page.props.flash_success" :key="i" class="success">{{ msg }}</p>
    <p v-for="(msg, i) in $page.props.flash_error" :key="i" class="error">{{ msg }}</p>

    <article>
      <slot />
    </article>
  </main>
</template>

<script>
import { Head, Link } from '@inertiajs/inertia-vue3'

export default {
  name: 'Layout',

  components: {
    Head,
    Link
  }
}
</script>
