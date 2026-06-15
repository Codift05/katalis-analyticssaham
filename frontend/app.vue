<template>
  <div class="min-h-screen flex flex-col font-sans">
    <!-- Header -->
    <header class="border-b border-borderdark bg-slatebg">
      <div class="flex items-center px-6 py-3">
        <div class="text-xl font-medium text-ink flex items-center gap-2">
           <span class="text-neutral">Katalis</span><span class="text-[10px] bg-cardbg px-1 rounded border border-borderdark text-muted align-top ml-1">Beta</span>
        </div>
      </div>
    </header>

    <main class="flex-1 grid gap-6 px-6 py-6 lg:grid-cols-[200px_1fr_340px]">
      <aside class="space-y-8 pr-4">
        <div>
          <div class="flex justify-between items-center text-sm mb-4">
             <span class="font-normal text-ink text-base">Daftar</span>
          </div>
          <div class="flex justify-between items-center text-xs mb-2">
            <span class="text-ink">Daftar pantauan</span>
            <span class="text-muted">+</span>
          </div>
          <div class="text-[11px] text-muted mb-6">Daftar ini kosong</div>
        </div>
        
        <div>
           <div class="text-xs text-ink mb-4">Sektor ekuitas</div>
           <div class="space-y-4 text-xs">
              <StockTicker symbol="SIXB" name="Materials" :initial-value="1068.24" :initial-change="-2.44" />
              <StockTicker symbol="SIXC" name="Communications" :initial-value="606.59" :initial-change="-0.05" />
              <StockTicker symbol="SIXE" name="Energy" :initial-value="1247.21" :initial-change="2.13" />
              <StockTicker symbol="SIXI" name="Industrials" :initial-value="1727.58" :initial-change="-1.82" />
           </div>
        </div>
      </aside>

      <section class="space-y-6">
        <div>
           <div class="text-xs text-muted mb-2 flex items-center gap-2">
             <span>← Beranda</span> <span class="text-neutral">|</span> <span>Katalis / Sentiment</span>
           </div>
           <h1 class="text-2xl text-ink font-normal mb-2">Stock Market Sentiment Radar</h1>
           <div class="flex items-end gap-3 mb-1">
             <span class="text-3xl font-medium text-ink">Market Mood</span>
             <span class="text-positive text-sm pb-1">+0,01% (+2,0639) Hari ini</span>
           </div>
           <div class="text-xs text-muted">Updated 5 minutes ago • Jakarta Session</div>
        </div>
        
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div class="flex flex-col gap-4">
            <SentimentDonut />
            <div class="bg-cardbg/30 border border-borderdark rounded-xl p-4 mt-auto">
              <h3 class="text-sm font-medium text-ink mb-1 flex items-center gap-2">
                <svg class="w-4 h-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z"></path></svg>
                Analisis Donut Chart
              </h3>
              <p class="text-xs text-muted leading-relaxed">
                Menunjukkan rasio sentimen pasar secara keseluruhan. <strong>Klik pada salah satu potongan warna</strong> untuk menyaring tabel berita di bawah.
              </p>
            </div>
          </div>
          
          <div class="flex flex-col gap-4">
            <SentimentBySource />
            <div class="bg-cardbg/30 border border-borderdark rounded-xl p-4 mt-auto">
              <h3 class="text-sm font-medium text-ink mb-1 flex items-center gap-2">
                <svg class="w-4 h-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
                Analisis Sumber Berita
              </h3>
              <p class="text-xs text-muted leading-relaxed">
                Memetakan bias media dengan membandingkan rasio sentimen 5 sumber berita paling aktif. Berfungsi melacak potensi manipulasi sentimen.
              </p>
            </div>
          </div>
        </div>

        <div class="mt-6">
           <SentimentGauge />
        </div>

        <div class="mt-8 border-b border-borderdark pb-2 mb-4">
          <div class="inline-block border-b-2 border-blue-400 pb-2 text-sm text-ink font-medium">Ringkasan Berita Terakhir</div>
        </div>

        <div class="relative max-w-full mb-6">
           <form @submit.prevent="submitNews" class="bg-cardbg border border-borderdark rounded-2xl p-2 flex items-center shadow-sm focus-within:border-muted transition-colors">
              <input 
                v-model="newsQuery" 
                type="text" 
                placeholder="Masukkan judul berita untuk dianalisis AI (lalu Enter)..." 
                class="w-full bg-transparent border-none text-sm text-ink placeholder-muted px-3 py-2 focus:outline-none focus:ring-0" 
                :disabled="isSubmitting"
              />
              <button 
                type="submit" 
                class="w-8 h-8 shrink-0 rounded-full bg-neutral flex items-center justify-center text-cardbg text-lg transition-transform hover:scale-105 disabled:opacity-50 disabled:hover:scale-100"
                :disabled="!newsQuery.trim() || isSubmitting"
              >
                <span v-if="!isSubmitting">↑</span>
                <span v-else class="w-4 h-4 border-2 border-cardbg border-t-transparent rounded-full animate-spin"></span>
              </button>
           </form>
        </div>

        <div class="pt-2">
          <NewsTable />
        </div>
      </section>

      <aside class="space-y-6">
         <div class="bg-transparent border-none h-full rounded-2xl flex flex-col">
            <h2 class="text-xl text-ink mb-2">Kamus Riset</h2>
            <p class="text-muted text-xs mb-6 leading-relaxed">Halo Miftahuddin, berikut adalah panduan klasifikasi sentimen pasar pada dashboard analisis ini.</p>
            
            <div class="space-y-4 text-xs text-ink">
               <div class="bg-cardbg/50 border border-borderdark p-4 rounded-xl flex flex-col hover:border-muted transition">
                  <div class="flex items-center gap-2 mb-2">
                     <span class="h-2 w-2 rounded-full bg-positive"></span>
                     <span class="font-medium text-[13px] text-positive">Positif (Bullish)</span>
                  </div>
                  <span class="text-muted leading-relaxed">Berita atau peristiwa yang diproyeksikan akan mendorong kenaikan harga saham atau IHSG. Contoh: Laba meroket, suku bunga turun, kebijakan pro-bisnis.</span>
               </div>
               
               <div class="bg-cardbg/50 border border-borderdark p-4 rounded-xl flex flex-col hover:border-muted transition">
                  <div class="flex items-center gap-2 mb-2">
                     <span class="h-2 w-2 rounded-full bg-negative"></span>
                     <span class="font-medium text-[13px] text-negative">Negatif (Bearish)</span>
                  </div>
                  <span class="text-muted leading-relaxed">Berita yang membawa ketakutan di pasar dan memicu aksi jual massal. Contoh: Inflasi tinggi, badai PHK, perusahaan bangkrut.</span>
               </div>
               
               <div class="bg-cardbg/50 border border-borderdark p-4 rounded-xl flex flex-col hover:border-muted transition">
                  <div class="flex items-center gap-2 mb-2">
                     <span class="h-2 w-2 rounded-full bg-neutral"></span>
                     <span class="font-medium text-[13px] text-neutral">Netral (Sideways)</span>
                  </div>
                  <span class="text-muted leading-relaxed">Berita informatif yang tidak memberikan katalis kuat untuk pergerakan harga. Contoh: Jadwal rapat dewan gubernur, libur bursa nasional.</span>
               </div>
            </div>
         </div>
      </aside>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import StockTicker from '~/components/StockTicker.vue';

const newsQuery = ref('');
const isSubmitting = ref(false);
const config = useRuntimeConfig();

const submitNews = async () => {
  const query = newsQuery.value.trim();
  if (!query) return;

  isSubmitting.value = true;
  try {
    const { data: sentimentRes, error: sentimentErr } = await useFetch<any>('/sentiment', {
      baseURL: config.public.apiBase as string,
      method: 'POST',
      body: { texts: [query] }
    });

    if (sentimentErr.value || !sentimentRes.value?.labels?.[0]) {
      console.error('Failed to analyze sentiment', sentimentErr.value);
      return;
    }

    const { error: newsErr } = await useFetch('/news', {
      baseURL: config.public.apiBase as string,
      method: 'POST',
      body: {
        source: 'User Input',
        title: query,
        sentiment: sentimentRes.value.labels[0]
      }
    });

    if (newsErr.value) {
      console.error('Failed to save news', newsErr.value);
      return;
    }

    newsQuery.value = '';
    // Force refresh News data globally
    await refreshNuxtData();
  } catch (err) {
    console.error(err);
  } finally {
    isSubmitting.value = false;
  }
};
</script>
