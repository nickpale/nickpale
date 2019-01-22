Vue.component('pro-header', {
  props: ['descriptions', 'resume', 'showAbout', 'homeUrl'],
  template: `
    <header>
      <h1>Nick White - Software Engineer</h1>
      <ul>
        <li>
          <a
              href=""
              @click.prevent="showAbout">
            About
          </a>
        </li>
        <li>
          <a :href="resume ? resume.file : ''">Resume</a>
        </li>
        <li>
          <a :href="homeUrl">Nick Pale</a>
        </li>
      </ul>
    </header>
  `
})

Vue.component('pro-blurb', {
  props: ['blurb'],
  template: `
    <section class="blurb" v-if="blurb">
      <h2 class="blurb-title">{{ blurb.title }}</h2>
      <p class="blurb-text">{{ blurb.text }}</p>
    </section>
  `
})

Vue.component('pro-about', {
  props: ['descriptions'],
  template:`
    <article class="about">
      <section v-for="description in descriptions">
        <h3>{{ description.title }}</h3>
        <p>{{ description.text }}</p>
      </section>
    </article>
  `
})

const proVueApp = new Vue({
  delimiters: ['[[', ']]'],
  el: 'main',
  data: {
    blurb: null,
    descriptions: [],
    resume: null,
    view: 'pro-blurb'
  },
  created: async function() {
    const blurbResponse = await fetch('/api/pro/blurb')
    this.blurb = await blurbResponse.json()

    const descriptionsResponse = await fetch('/api/pro/descriptions')
    const descriptions = await descriptionsResponse.json()
    this.descriptions = descriptions
      .sort((a, b) => a.order_rank - b.order_rank)

    const resumeResponse = await fetch('/api/pro/resume')
    this.resume = await resumeResponse.json()
  },
  computed: {
    currentProperties: function() {
      if (this.view === 'pro-blurb') {
        return { blurb: this.blurb }
      } else if (this.view === 'pro-about') {
        return { descriptions: this.descriptions }
      }
    }
  },
  methods: {
    showAbout: function() {
      this.view = this.descriptions[0] ? 'pro-about' : 'pro-blurb'
    }
  }
})
