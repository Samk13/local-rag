/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  
  content: ["./local_rag/app/templates/**/*.{html,htm}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Figtree", "Inter var", sans-serif',],
      }
    },
  },
  plugins: [],
}

