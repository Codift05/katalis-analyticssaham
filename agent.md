# Project Overview
Nama App : Katalis
Name: Stock Market Sentiment Radar
Description: A web-based AI application that analyzes the sentiment of financial news and categorizes it into Positive, Negative, or Neutral to assist retail investors.
Architecture: Decoupled Full-Stack (Frontend: Nuxt 3, Backend: FastAPI + SQLite).

# Core Technologies
## Frontend
- Framework: Nuxt 3 (Vue.js Composition API)
- Styling: Tailwind CSS
- Icons: SVG exclusively (e.g., Heroicons). **Strict Rule: NO EMOJIS in the codebase or UI.**
- State Management: Pinia (if global state is necessary)
- Charts: Chart.js or Apache ECharts for rendering clean, thin-lined sentiment graphs.

## Backend & NLP
- Framework: FastAPI (Python)
- Server: Uvicorn
- Database: SQLite (local file database)
- ORM: SQLAlchemy
- Data Validation: Pydantic
- Machine Learning: Scikit-learn (TF-IDF Vectorizer, Support Vector Machine / Naive Bayes)
- NLP Preprocessing: Sastrawi (Indonesian stemming) / NLTK

# Strict Design & UI/UX Guidelines
The user interface must convey a professional, enterprise-grade financial technology aesthetic. 
1. **Minimalist & Professional**: The layout must be clean, utilizing ample whitespace strategically, but maintaining a dense, data-rich feel typical of trading platforms.
2. **Typography**: Do NOT use oversized text. Use `text-sm`, `text-base`, and `text-xs` for data tables and standard UI elements. Headings should be appropriately sized (`text-lg` or `text-xl` max for card headers).
3. **Card Design**: Cards and containers must NOT be overly large or bulky. Use subtle borders (`border-gray-200` or `border-slate-200`), minimal drop shadows (`shadow-sm`), and tight padding (`p-4` or `p-5`).
4. **Icons**: Strictly use inline SVGs or a professional SVG icon library. Make sure icons are appropriately sized (e.g., `w-4 h-4` or `w-5 h-5`) and match the text color contextually. Do not use colorful or playful illustrations.
5. **Color Palette**: Use a professional palette. Slate or Gray for neutral backgrounds, dark blue/slate for primary text. For sentiment: subtle Green for Positive, subtle Red for Negative, and subtle Gray/Blue for Neutral. Avoid overly saturated neon colors.
6. **No Emojis**: Under no circumstances should emojis be used in the UI, button texts, empty states, or error messages.

# Backend Development Rules
1. **SQLite Setup**: Ensure the database connection uses `connect_args={"check_same_thread": False}` to prevent threading issues with FastAPI.
2. **Model Loading**: The NLP model (`.pkl` file) should be loaded into memory once during FastAPI's startup event, not read from disk on every API request.
3. **API Responses**: Always return structured JSON using Pydantic models. Ensure all endpoints handle errors gracefully with standard HTTP status codes.

# Workflow Definition
- The backend will expose endpoints to retrieve news data and submit new text for sentiment classification.
- The frontend will consume these endpoints and display the aggregated sentiment in a minimalist dashboard (a pie/donut chart and a compact data table).

# Final Tech Stack (Full-Stack NLP Lokal)
## 1. Frontend (Antarmuka Pengguna & Visualisasi)
- Framework: Nuxt 3 (Vue.js). Sangat cepat dan modular.
- Styling: Tailwind CSS. Sempurna untuk membuat desain minimalis dan mengatur ukuran tipografi yang terukur (text-sm, text-xs) serta padding kartu yang presisi.
- Icons: Heroicons atau Tabler Icons (berformat SVG). Dapat diubah skala dan warnanya secara langsung melalui kelas Tailwind (w-5 h-5 text-gray-500).
- Charts: ECharts (via vue-echarts) atau Chart.js. Digunakan untuk merender grafik donut/pie sentimen saham dengan garis desain yang tipis dan elegan.

## 2. Backend (API & Database)
- Framework: FastAPI (Python). Cepat, modern, dan menyediakan dokumentasi otomatis (Swagger UI).
- Database: SQLite. Berjalan 100% lokal di dalam proyek, tidak butuh instalasi server.
- ORM: SQLAlchemy. Mengelola interaksi database menggunakan objek Python, sehingga jika nanti perlu migrasi, cukup ubah satu baris kode.
- Validation: Pydantic. Memastikan tipe data teks dan array yang masuk selalu benar.

## 3. Pemrosesan Bahasa Alami (NLP)
- Library Utama: Scikit-Learn. Sangat ringan untuk algoritma Machine Learning klasik (Support Vector Machine atau Naive Bayes).
- Ekstraksi Fitur: TF-IDF Vectorizer (mengubah teks berita menjadi matriks angka).
- Model Persistance: Joblib (untuk menyimpan model NLP yang sudah dilatih ke dalam bentuk file .pkl agar FastAPI bisa langsung menggunakannya tanpa training ulang).