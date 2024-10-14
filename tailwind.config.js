/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./frontend/templates/**/*.html"],
  theme: {
    container: {
      center: true,
    },
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: ['light',],
  }
}
