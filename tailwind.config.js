/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./frontend/templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: ['light',],
  }
}
