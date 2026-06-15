# Laporan Proyek: Katalis - Stock Market Sentiment Radar

## BAB 1 Pendahuluan

### 1.1 Latar Belakang
Di era informasi digital, pergerakan pasar saham tidak hanya dipengaruhi oleh laporan keuangan perusahaan, tetapi juga oleh sentimen berita dan persepsi publik. Investor seringkali kesulitan untuk memantau dan menganalisis volume berita harian untuk menentukan sentimen pasar secara keseluruhan. Oleh karena itu, dibutuhkan sebuah platform analitik prediktif yang dapat mengagregasi berita dan mengklasifikasikannya menjadi sentimen positif, negatif, atau netral secara visual dan interaktif.

### 1.2 Rumusan Masalah
1. Bagaimana merancang antarmuka (dashboard) yang interaktif untuk memonitor sentimen pasar saham?
2. Bagaimana memproses data klasifikasi berita dan menyajikannya dalam bentuk visualisasi analitik seperti rasio ketakutan dan keserakahan (Fear & Greed Index) pasar?

### 1.3 Tujuan
1. Membangun aplikasi web "Katalis" sebagai radar sentimen pasar saham yang fungsional.
2. Mengimplementasikan visualisasi data interaktif (Donut Chart, Stacked Bar Chart, dan Gauge Chart) untuk memudahkan investor membaca arah pasar.
3. Menyediakan arsitektur sistem berbasis *Client-Server* yang memisahkan sisi presentasi (*frontend*) dan proses logika bisnis (*backend*).

### 1.4 Manfaat
Bagi investor, aplikasi ini bermanfaat sebagai alat bantu pendukung keputusan (*Decision Support System*) untuk memantau kondisi psikologis pasar (bullish/bearish) dengan cepat. Bagi pengembang, proyek ini mendemonstrasikan integrasi *modern web stack*.

---

## BAB 2 Teori Pendukung

### 2.1 Analisis Sentimen (Sentiment Analysis)
Analisis sentimen adalah cabang dari *Natural Language Processing* (NLP) yang bertujuan untuk mengekstrak opini atau emosi dari sebuah teks. Dalam konteks pasar saham, sentimen dibagi menjadi Positif (mendorong harga naik/Bullish), Negatif (memicu ketakutan dan aksi jual/Bearish), dan Netral (informasi faktual/Sideways).

### 2.2 Vue 3 dan Nuxt 3
Nuxt 3 adalah *framework* Vue.js yang digunakan untuk membangun aplikasi web modern yang cepat dan optimal. Vue 3 memanfaatkan fitur *Composition API* yang memudahkan pengelolaan *state* dan pembagian logika pada tiap komponen UI (*User Interface*).

### 2.3 FastAPI (Python)
FastAPI adalah *framework* web modern dan berkinerja tinggi untuk membangun API (Application Programming Interface) dengan Python berdasarkan standar petunjuk tipe (type hints). Framework ini sangat efisien dalam memproses *request* data analitik dan terintegrasi dengan baik pada antarmuka *backend*.

### 2.4 Apache ECharts
ECharts adalah pustaka visualisasi data *open-source* yang sangat kuat. Dalam proyek ini, library integrasi `vue-echarts` digunakan untuk menghubungkan konfigurasi grafik ECharts agar dapat di-*render* secara responsif ke dalam komponen Vue.

---

## BAB 3 Desain Sistem

### 3.1 Arsitektur Sistem
Sistem ini menggunakan arsitektur aplikasi web modern:
- **Client (Frontend)**: Menggunakan Nuxt 3. Bertugas menangani antarmuka pengguna, sistem *routing*, visualisasi grafik (ECharts), dan berinteraksi menangkap *input* dari pengguna.
- **Server (Backend)**: Menggunakan FastAPI. Menangani pengaturan rute data (*REST API endpoints*), memproses interaksi baca-tulis, dan melayani data dalam format JSON.
- **Database**: Menggunakan SQLite dengan *Object Relational Mapping* (SQLAlchemy). Digunakan untuk menyimpan riwayat berita dan hasil klasifikasi sentimen secara persisten.

> [PLACEHOLDER GAMBAR: Masukkan Gambar Arsitektur Sistem (Alur Client - REST API - Backend - Database) di sini]

### 3.2 Rancangan Proses / Prinsip Kerja Sistem (Use Case)
Prinsip kerja sistem dirancang agar berjalan mulus sebagai *Single Page Application*:
1. **Sistem Frontend** dimuat oleh *browser* pengguna dan langsung melakukan permintaan data (*fetch API*) ke *backend*.
2. **Backend** merespons dengan mengirimkan kumpulan data riwayat berita beserta status sentimennya.
3. **Sistem Frontend** secara terpusat menghitung persentase sentimen dan mendistribusikannya ke 3 jenis grafik berbeda (Donut, Bias Media, dan Speedometer).
4. **User** dapat menambah masukan berita baru. Backend menyimpannya ke *database* lalu memberikan respons sukses, yang kemudian memicu sistem Frontend untuk me-*refresh* dan menghitung ulang seluruh grafik secara seketika.

> [PLACEHOLDER GAMBAR: Masukkan Gambar Use Case Diagram di sini]

### 3.3 Pemodelan Data (Desain DB / ERD)
Sistem ini berfokus pada struktur pemrosesan analitik, sehingga entitas utama yang dimodelkan adalah tabel `news`:
- `id` (Integer, Primary Key, Auto-increment)
- `source` (String): Asal portal media penyedia berita (Misal: Tech Times, Jakarta Wire)
- `title` (String): Berisi kalimat utuh (judul) berita
- `sentiment` (String): Hasil kesimpulan algoritma (Positive, Negative, Neutral)
- `created_at` (DateTime): Waktu atau *timestamp* (pencatatan waktu tayang)

> [PLACEHOLDER GAMBAR: Masukkan Gambar Entity Relationship Diagram (ERD) di sini]

### 3.4 Rancangan User Interface (UI)
UI didesain menggunakan palet warna "Dark Mode Financial Dashboard" untuk meminimalisir ketegangan mata, dikombinasikan dengan kode warna psikologis:
- Hijau (`#81c995`) yang melambangkan pertumbuhan/keuntungan (Positif).
- Merah Pudar (`#f28b82`) yang melambangkan peringatan/krisis (Negatif).
- Abu-abu (`#8892b0`) untuk konteks wawasan faktual (Netral).

> [PLACEHOLDER GAMBAR: Masukkan Gambar Mockup / Sketsa Awal Rancangan UI Dashboard di sini]

---

## BAB 4 Implementasi Sistem

### 4.1 Hasil Implementasi Rancangan (Antarmuka Pengguna)
Aplikasi berhasil direalisasikan ke bentuk perangkat lunak dengan fitur visualisasi berikut:
1. **Sentiment Overview (Donut Chart)**: Menunjukkan rasio pasar secara umum dari seluruh sampel berita.
2. **Sentiment by Source (Stacked Bar Chart)**: Memetakan sebaran distribusi dan mengukur tingkat bias opini dari media portal yang berbeda.
3. **Market Mood Index (Gauge Chart)**: Mengalkulasi selisih polaritas (Positif dikurangi Negatif) lalu merubahnya menjadi persentase 0 hingga 100 yang menentukan level pasar (*Extreme Fear*, *Neutral*, atau *Greed*).
4. **Research Dictionary**: Area khusus yang menjelaskan definisi terminologi pergerakan harga bagi pengguna baru.

> [PLACEHOLDER GAMBAR: Masukkan Screenshot Halaman Dashboard Utuh (Katalis) di sini]

### 4.2 Potongan Kode Sumber (Source Code)

#### Implementasi Backend (Endpoint Data)
Kode berikut adalah fungsi utama (endpoint) dari FastAPI untuk menyajikan data berita ke *Frontend*.
```python
# backend/app/main.py
@app.get("/news", response_model=List[schemas.NewsRead])
def read_news(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    news = db.query(models.News).order_by(models.News.created_at.desc()).offset(skip).limit(limit).all()
    return news
```

#### Implementasi Frontend (Algoritma Market Mood)
Potongan skrip berbasis *Vue Composition API* yang secara komputasional menerjemahkan perbandingan jumlah sentimen menjadi skor speedometer.
```typescript
// frontend/components/SentimentGauge.vue
const option = computed(() => {
  const items = rows.value || [];
  let pos = 0, neg = 0;
  
  // Agregasi Data
  for (const item of items) {
    if (item.sentiment === 'Positive') pos++;
    else if (item.sentiment === 'Negative') neg++;
  }
  
  // Konversi polaritas pasar menjadi skor rentang 0-100
  const total = items.length || 1;
  let score = Math.round(((pos - neg) / total) * 50 + 50);

  // Parameter Visualisasi
  return {
    series: [{
      type: 'gauge',
      data: [{ value: score, name: 'Market Mood' }]
      // ... (kode styling lanjutan disembunyikan)
    }]
  };
});
```

### 4.3 Evaluasi Sistem
- **Kelebihan**: Arsitektur Frontend menggunakan SPA menjadikan transisi grafik berjalan sangat mulus dan *responsive* tanpa lag saat pengguna mengirim perintah input. Solusi grafis menggunakan *tree-shaking* dan modifikasi tipe sumbu membuat proyek ini berjalan ringan.
- **Kekurangan**: Modul analisis pintar (AI) dalam proyek ini masih bersifat simulatif (menggunakan pembobotan kata acak atau dataset tiruan *seeding*). Pada skala industri, sistem wajib diintegrasikan dengan model *Deep Learning* berarsitektur Transformer.

---

## BAB 5 Kesimpulan dan Saran

### 5.1 Kesimpulan
Proyek sistem "Katalis - Stock Market Sentiment Radar" berhasil diwujudkan sebagai purwarupa (*prototype*) aplikasi intelijen bisnis pasar modal. Sistem berhasil memadukan keandalan *backend* Python dengan ketajaman antarmuka Vue.js. Secara praktis, penggunaan bagan analitis tingkat lanjut (khususnya *Market Mood Gauge*) sukses memudahkan penarikan kesimpulan instan terhadap tren psikologis publik.

### 5.2 Saran
Pengembangan fase selanjutnya disarankan untuk mencakup:
1. Pemanfaatan protokol *WebSockets* yang memungkinkan pembaruan harga (*stock ticker*) dan grafik berjalan mulus (*real-time streaming*).
2. Memigrasikan *Database* SQLite lokal ke *Database Relasional Server* (seperti PostgreSQL) agar mampu menampung riwayat puluhan ribu berita tanpa penurunan *Query Time*.
3. Mengadopsi teknologi pengerukan web otomatis (*Web Scraping*) dari media ternama seperti Bloomberg atau Reuters sebagai sumber data primer yang aktual.

---

## Daftar Pustaka
1. S. Ramírez, "FastAPI Documentation," 2024. [Online]. Available: https://fastapi.tiangolo.com/.
2. The Nuxt Team, "Nuxt 3: The Intuitive Web Framework," 2024. [Online]. Available: https://nuxt.com/docs.
3. Apache Software Foundation, "Apache ECharts Documentation," 2024. [Online]. Available: https://echarts.apache.org/en/index.html.
4. J. Bollen, H. Mao, and X. Zeng, "Twitter mood predicts the stock market," *Journal of Computational Science*, vol. 2, no. 1, pp. 1-8, 2011.
