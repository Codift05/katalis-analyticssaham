import type { Config } from "tailwindcss";

export default <Partial<Config>>{
  content: [
    "./app.vue",
    "./components/**/*.{vue,js,ts}",
    "./pages/**/*.{vue,js,ts}"
  ],
  theme: {
    extend: {
      colors: {
        slatebg: "#202124",
        cardbg: "#303134",
        borderdark: "#3c4043",
        ink: "#e8eaed",
        muted: "#9aa0a6",
        positive: "#81c995",
        negative: "#f28b82",
        neutral: "#9aa0a6"
      }
    }
  },
  plugins: []
};
