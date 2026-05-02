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
        slatebg: "#f6f7f9",
        ink: "#0f172a",
        muted: "#475569",
        positive: "#16a34a",
        negative: "#dc2626",
        neutral: "#64748b"
      }
    }
  },
  plugins: []
};
