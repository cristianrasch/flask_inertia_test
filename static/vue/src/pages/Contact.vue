<template>
  <Layout>
    <form @submit.prevent="submitForm">
      <fieldset>
        <legend>{{ msg }}</legend>

        <p>
          <label for="name">Name:</label>&nbsp;
          <input name="name" id="name" v-model="form.name" />
          <span v-if="form.errors.name">&nbsp;{{ form.errors.name }}</span>
        </p>

        <p>
          <label for="email">Email:</label>&nbsp;
          <input type="email" name="email" id="email" v-model="form.email" />
          <span v-if="form.errors.email">&nbsp;{{ form.errors.email }}</span>
        </p>

        <p>
          <label for="subject">Subject:</label>&nbsp;
          <input name="subject" id="subject" v-model="form.subject" />
          <span v-if="form.errors.subject">&nbsp;{{ form.errors.subject }}</span>
        </p>

        <p>
          <label for="message">Message:</label>&nbsp;
          <textarea name="message" id="message" v-model="form.message"></textarea>
        </p>

        <p>
          <label for="image">Image:</label>&nbsp;
          <input type="file" name="image" id="image" accept="image/*" ref="image" @change="captureImage" />
          <span v-if="form.errors.image">&nbsp;{{ form.errors.image }}</span>
        </p>

        <p v-if="form.image && form.progress">
          <label for="progress">Image upload progress:</label>&nbsp;
          <progress v-if="form.progress" :value="form.progress.percentage" max="100">
            {{ form.progress.percentage }}%
          </progress>
        </p>

        <p>
          <button type="submit" :disabled="form.processing">Send</button>
        </p>
      </fieldset>
    </form>
  </Layout>
</template>

<script>
import Layout from './Layout'

export default {
  name: 'Contact',

  props: {
    errors: {
      type: Object
    },
    msg: {
      type: String,
      required: true
    }
  },

  data() {
    return {
      form: this.$inertia.form({
        name: '',
        email: '',
        subject: '',
        message: '',
        image: null,
      })
    }
  },

  methods: {
    captureImage(event) {
      this.form.image = event.target.files ? event.target.files[0] : null
    },

    submitForm() {
      this.form.post(this.$route('contact'), {
        onSuccess: () => {
          this.form.reset()
          this.$refs.image.value = null
        }
      })
    }
  },

  components: {
    Layout,
  },
};
</script>

