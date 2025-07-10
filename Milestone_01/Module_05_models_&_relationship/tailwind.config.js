/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // ** things mean nested folder
    "./templates/**/*.html", //template at the project level
    "./**/templates/**/*.html", //template at the app level
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

