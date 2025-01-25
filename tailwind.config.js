/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html', // Include app-level templates
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#07529b', // Default shade
        },
        secondary: {
          DEFAULT: '#f5be1c', // Default shade
        },
        body: {
          DEFAULT: '#515151',
        },
      },
      fontFamily: {
        title: ['Darker Grotesque', 'sans-serif'], // Title font
        subheading: ['Darker Grotesque', 'sans-serif'], // Subheading font
        body: ['Work Sans', 'sans-serif'], // Body font
      },
    },
  },
};