<template>
  <div class="card p-4">
    <div class="flex items-center justify-between">
      <h2 class="text-base font-semibold text-ink">Latest Headlines</h2>
      <button class="text-xs text-muted hover:text-ink">Refresh</button>
    </div>
    <div class="mt-4 overflow-hidden rounded-md border border-slate-200">
      <table class="min-w-full text-xs">
        <thead class="bg-slate-50 text-muted">
          <tr>
            <th class="px-3 py-2 text-left font-medium">Source</th>
            <th class="px-3 py-2 text-left font-medium">Headline</th>
            <th class="px-3 py-2 text-left font-medium">Sentiment</th>
            <th class="px-3 py-2 text-left font-medium">Time</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-200">
          <tr v-for="item in rows" :key="item.id">
            <td class="px-3 py-2 text-muted">{{ item.source }}</td>
            <td class="px-3 py-2 text-ink">{{ item.title }}</td>
            <td class="px-3 py-2">
              <span
                class="inline-flex items-center rounded-full px-2 py-0.5 text-[11px] font-medium"
                :class="badgeClass(item.sentiment)"
              >
                {{ item.sentiment }}
              </span>
            </td>
            <td class="px-3 py-2 text-muted">{{ item.time }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
const rows = [
  {
    id: 1,
    source: "IDX Market",
    title: "Banking sector leads late-session rebound on liquidity news",
    sentiment: "Positive",
    time: "09:12"
  },
  {
    id: 2,
    source: "Jakarta Wire",
    title: "Commodity exporters face margin pressure amid FX volatility",
    sentiment: "Negative",
    time: "08:44"
  },
  {
    id: 3,
    source: "Asia Macro",
    title: "Government reiterates infrastructure spending outlook for 2026",
    sentiment: "Neutral",
    time: "08:05"
  }
];

const badgeClass = (sentiment: string) => {
  if (sentiment === "Positive") {
    return "bg-green-50 text-positive border border-green-200";
  }
  if (sentiment === "Negative") {
    return "bg-red-50 text-negative border border-red-200";
  }
  return "bg-slate-50 text-neutral border border-slate-200";
};
</script>
