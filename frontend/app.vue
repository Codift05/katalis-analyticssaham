<template>
  <div class="min-h-screen flex flex-col font-sans">
    <!-- Header -->
    <header class="border-b border-borderdark bg-slatebg">
      <div class="flex items-center px-6 py-3">
        <div class="text-xl font-medium text-ink flex items-center gap-2">
           <span class="text-neutral">Katalis</span><span class="text-[10px] bg-cardbg px-1 rounded border border-borderdark text-muted align-top ml-1">Beta</span>
        </div>
        <!-- Search bar -->
        <div class="ml-10 flex-1 max-w-3xl relative">
          <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
            <svg class="h-4 w-4 text-muted" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
          <input type="text" class="block w-full bg-cardbg border border-borderdark rounded-full py-2.5 pl-12 pr-4 text-sm placeholder-muted focus:outline-none focus:border-neutral text-ink" placeholder="Bagaimana keadaan pasar hari ini?">
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
              <div class="flex justify-between items-center">
                 <div><div class="text-ink">SIXB</div><div class="text-muted text-[10px]">Materials</div></div>
                 <div class="text-right"><div class="text-ink">1.068,24</div><div class="text-negative text-[10px]">-2,44% ↓</div></div>
              </div>
              <div class="flex justify-between items-center">
                 <div><div class="text-ink">SIXC</div><div class="text-muted text-[10px]">Communications</div></div>
                 <div class="text-right"><div class="text-ink">606,59</div><div class="text-negative text-[10px]">-0,05% ↓</div></div>
              </div>
              <div class="flex justify-between items-center">
                 <div><div class="text-ink">SIXE</div><div class="text-muted text-[10px]">Energy</div></div>
                 <div class="text-right"><div class="text-ink">1.247,21</div><div class="text-positive text-[10px]">+2,13% ↑</div></div>
              </div>
              <div class="flex justify-between items-center">
                 <div><div class="text-ink">SIXI</div><div class="text-muted text-[10px]">Industrials</div></div>
                 <div class="text-right"><div class="text-ink">1.727,58</div><div class="text-negative text-[10px]">-1,82% ↓</div></div>
              </div>
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
        
        <SentimentDonut />

        <div class="mt-8 border-b border-borderdark">
          <div class="inline-block border-b-2 border-blue-400 pb-2 text-sm text-ink font-medium">Ringkasan</div>
        </div>

        <div class="pt-4">
          <NewsTable />
        </div>
      </section>

      <aside class="space-y-6">
         <!-- "Riset" equivalent with Alert Queue integrated -->
         <div class="bg-transparent border-none h-full rounded-2xl flex flex-col">
            <h2 class="text-xl text-ink mb-6">Riset</h2>
            <p class="text-ink text-sm mb-6">Halo Miftahuddin, ajukan pertanyaan terkait sentimen pasar</p>
            
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-sm text-ink font-medium">Alert Queue</h3>
              <span class="text-xs text-muted">3 active</span>
            </div>
            
            <div class="space-y-3 mb-8 text-xs text-ink">
               <div class="bg-cardbg border border-borderdark p-3 rounded-xl flex flex-col cursor-pointer hover:border-muted transition">
                  <span class="font-medium">Liquidity spike on banking sector</span>
                  <span class="text-muted mt-1 text-[11px]">Monitor for earnings impact</span>
               </div>
               <div class="bg-cardbg border border-borderdark p-3 rounded-xl flex flex-col cursor-pointer hover:border-muted transition">
                  <span class="font-medium">Commodity export headline cluster</span>
                  <span class="text-muted mt-1 text-[11px]">Neutral sentiment, watch FX trend</span>
               </div>
               <div class="bg-cardbg border border-borderdark p-3 rounded-xl flex flex-col cursor-pointer hover:border-muted transition">
                  <span class="font-medium">Infrastructure policy brief released</span>
                  <span class="text-muted mt-1 text-[11px]">Expected to stabilize Q3 outlook</span>
               </div>
            </div>

            <h3 class="text-sm text-ink mb-4 mt-4">Jelajahi berbagai kemungkinan</h3>
            <div class="flex flex-col gap-3 mb-8 text-xs text-ink items-start">
               <div class="inline-flex items-center gap-2 bg-cardbg border border-borderdark px-4 py-2 rounded-full cursor-pointer hover:border-muted transition">
                 <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg> Deep Search
               </div>
               <div class="inline-flex items-center gap-2 bg-cardbg border border-borderdark px-4 py-2 rounded-full cursor-pointer hover:border-muted transition">
                 <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg> Analisis Daftar Pantauan saya
               </div>
            </div>

            <div class="mt-auto">
               <div class="bg-cardbg border border-borderdark rounded-2xl p-4 flex justify-between items-center">
                  <span class="text-muted text-sm">Tanyakan apa saja</span>
                  <div class="w-8 h-8 rounded-full bg-[#3c4043] flex items-center justify-center text-ink text-lg">↑</div>
               </div>
            </div>
         </div>
      </aside>
    </main>
  </div>
</template>

<script setup lang="ts">
</script>
