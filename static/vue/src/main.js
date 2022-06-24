import { createApp, h, App } from 'vue';
import { createInertiaApp } from '@inertiajs/inertia-vue3';

import { InertiaProgress } from '@inertiajs/progress';

InertiaProgress.init();

import './css/app.css';

import Layout from './pages/Layout';

// create a plugin to use window.reverseUrl in our Components
const routePlugin = {
  install: (app, _options) => {
    app.config.globalProperties.$route = window.reverseUrl;
  },
};

createInertiaApp({
  resolve: (name) => {
    const page = require(`./pages/${name}`).default;
    page.layout ??= Layout;
    return page;
  },
  // resolve: async (name) => {
  //   const page = await import(`./pages/${name}`);
  //   page.default.layout ??= Layout;
  //   // page.default.layout = page.default.layout || Layout
  //   return page.default;
  // },
  setup({ el, app, props, plugin }) {
    const vueApp = createApp({ render: () => h(app, props) });
    vueApp.use(plugin);
    vueApp.use(routePlugin);
    vueApp.mount(el);
  },
});
