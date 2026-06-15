<template>
  <div class="card p-4">
    <div class="flex items-center justify-between">
      <div class="flex items-center gap-3">
        <h2 class="text-base font-semibold text-ink">Latest Headlines</h2>
        <span v-if="sentimentFilter" class="bg-cardbg border border-borderdark text-muted text-[10px] px-2 py-0.5 rounded flex items-center gap-1 cursor-pointer hover:text-ink" @click="sentimentFilter = null">
          Filtered: {{ sentimentFilter }} <span class="text-neutral">&times;</span>
        </span>
      </div>
      <button
        class="text-xs text-muted hover:text-ink disabled:cursor-not-allowed disabled:opacity-50"
        :disabled="pending"
        @click="refresh"
      >
        {{ pending ? "Refreshing..." : "Refresh" }}
      </button>
    </div>
    <div class="mt-4 overflow-hidden rounded-md border border-borderdark">
      <table class="min-w-full text-xs">
        <thead class="bg-cardbg text-muted">
          <tr>
            <th class="px-3 py-2 text-left font-medium border-b border-borderdark">Source</th>
            <th class="px-3 py-2 text-left font-medium border-b border-borderdark">Headline</th>
            <th class="px-3 py-2 text-left font-medium border-b border-borderdark">Sentiment</th>
            <th class="px-3 py-2 text-left font-medium border-b border-borderdark">Time</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-borderdark">
          <tr v-if="pending">
            <td class="px-3 py-3 text-muted" colspan="4">Loading data...</td>
          </tr>
          <tr v-else-if="error">
            <td class="px-3 py-3 text-muted" colspan="4">Failed to load data.</td>
          </tr>
          <tr v-else-if="filteredRows.length === 0">
            <td class="px-3 py-3 text-muted" colspan="4">No headlines available.</td>
          </tr>
          <tr v-else v-for="item in filteredRows" :key="item.id">
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
            <td class="px-3 py-2 text-muted">{{ formatTime(item.created_at) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onBeforeUnmount, onMounted, computed } from "vue";

const { data: rows, pending, error, refresh } = useNews();
const sentimentFilter = useSentimentFilter();

const filteredRows = computed(() => {
  if (!rows.value) return [];
  if (!sentimentFilter.value) return rows.value;
  return rows.value.filter(item => item.sentiment === sentimentFilter.value);
});
const refreshIntervalMs = 30000;
let timer: ReturnType<typeof setInterval> | null = null;

onMounted(() => {
  timer = setInterval(() => {
    refresh();
  }, refreshIntervalMs);
});

onBeforeUnmount(() => {
  if (timer) {
    clearInterval(timer);
  }
});

const formatTime = (value?: string | null) => {
  if (!value) {
    return "-";
  }
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    return "-";
  }
  return new Intl.DateTimeFormat("en-GB", {
    hour: "2-digit",
    minute: "2-digit"
  }).format(date);
};

const badgeClass = (sentiment: string) => {
  if (sentiment === "Positive") {
    return "bg-[#81c995]/10 text-positive border border-[#81c995]/20";
  }
  if (sentiment === "Negative") {
    return "bg-[#f28b82]/10 text-negative border border-[#f28b82]/20";
  }
  return "bg-cardbg text-neutral border border-borderdark";
};
</script>
