<template>
  <div class="min-h-screen">
    <header class="border-b border-slate-200 bg-white/80 backdrop-blur">
      <div class="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <div class="flex items-center gap-3">
          <div class="flex h-9 w-9 items-center justify-center rounded-md bg-slate-900">
            <svg viewBox="0 0 24 24" class="h-5 w-5 text-white" fill="none" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 19.5V4.5l6 6 6-6v15" />
            </svg>
          </div>
          <div>
            <p class="text-sm font-semibold text-ink">Katalis</p>
            <p class="text-xs text-muted">Stock Market Sentiment Radar</p>
          </div>
        </div>
        <div class="flex items-center gap-4 text-xs text-muted">
          <div class="flex items-center gap-2">
            <svg viewBox="0 0 24 24" class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v18m9-9H3" />
            </svg>
            <span>Realtime Feed</span>
          </div>
          <button class="rounded-md border border-slate-200 px-3 py-1.5 text-xs font-medium text-ink">
            Export
          </button>
        </div>
      </div>
    </header>

    <main class="mx-auto grid max-w-6xl gap-6 px-6 py-6 lg:grid-cols-[2fr_1fr]">
      <section class="space-y-6">
        <div class="card p-5">
          <div class="flex items-center justify-between">
            <h1 class="text-lg font-semibold text-ink">Market Mood Snapshot</h1>
            <div class="flex items-center gap-3 text-xs text-muted">
              <span>Updated 5 minutes ago</span>
              <span class="h-1 w-1 rounded-full bg-slate-300"></span>
              <span>Jakarta Session</span>
            </div>
          </div>
          <div class="mt-4 grid gap-4 md:grid-cols-3">
            <div class="rounded-md border border-slate-200 p-3">
              <p class="text-xs text-muted">Total Headlines</p>
              <p class="mt-1 text-base font-semibold text-ink">284</p>
            </div>
            <div class="rounded-md border border-slate-200 p-3">
              <p class="text-xs text-muted">Model Confidence</p>
              <p class="mt-1 text-base font-semibold text-ink">87.4%</p>
            </div>
            <div class="rounded-md border border-slate-200 p-3">
              <p class="text-xs text-muted">Volatility Index</p>
              <p class="mt-1 text-base font-semibold text-ink">Low</p>
            </div>
          </div>
        </div>

        <NewsTable />
      </section>

      <aside class="space-y-6">
        <SentimentDonut />
        <div class="card p-4">
          <div class="flex items-center justify-between">
            <h2 class="text-base font-semibold text-ink">Alert Queue</h2>
            <span class="text-xs text-muted">3 active</span>
          </div>
          <div class="mt-4 space-y-3 text-xs">
            <div class="rounded-md border border-slate-200 p-3">
              <p class="font-medium text-ink">Liquidity spike on banking sector</p>
              <p class="mt-1 text-muted">Monitor for earnings impact</p>
            </div>
            <div class="rounded-md border border-slate-200 p-3">
              <p class="font-medium text-ink">Commodity export headline cluster</p>
              <p class="mt-1 text-muted">Neutral sentiment, watch FX trend</p>
            </div>
            <div class="rounded-md border border-slate-200 p-3">
              <p class="font-medium text-ink">Infrastructure policy brief released</p>
              <p class="mt-1 text-muted">Expected to stabilize Q3 outlook</p>
            </div>
          </div>
        </div>
      </aside>
    </main>
  </div>
</template>

<script setup lang="ts">
</script>
