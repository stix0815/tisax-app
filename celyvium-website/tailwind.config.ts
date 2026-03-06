import type { Config } from "tailwindcss";

export default {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        // Primary (Background / Dark)
        'deep-navy': '#141631',
        'navy': '#232554',
        'steel-blue': '#2A4C71',
        'deep-blue': '#345895',
        
        // Accent (Glow / Orb-Gradient)
        'neon-cyan': '#68D7EF',
        'soft-cyan': '#9DDAF5',
        'azure-blue': '#5DA2DC',
        'electric-indigo': '#6769DB',
        'vivid-purple': '#9E69DE',
        'soft-magenta': '#D695F7',
        'lavender': '#A19BEB',
        
        // Neutral (Text/Smoke)
        'off-white': '#EEF1F5',
        'cool-grey': '#9999A5',
      },
      backgroundImage: {
        'brand-gradient': 'linear-gradient(135deg, #68D7EF 0%, #6769DB 50%, #9E69DE 100%)',
        'glow-gradient': 'radial-gradient(circle at center, #68D7EF 0%, #6769DB 40%, #9E69DE 70%, #D695F7 100%)',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
} satisfies Config;
