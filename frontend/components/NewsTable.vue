<template>
  <div class="card p-4">
    <div class="flex items-center justify-between">
      <h2 class="text-base font-semibold text-ink">Latest Headlines</h2>
      <button
        class="text-xs text-muted hover:text-ink disabled:cursor-not-allowed disabled:opacity-50"
        :disabled="pending"
        @click="refresh"
      >
        {{ pending ? "Refreshing..." : "Refresh" }}
      </button>
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
          <tr v-if="pending">
            <td class="px-3 py-3 text-muted" colspan="4">Loading data...</td>
          </tr>
          <tr v-else-if="error">
            <td class="px-3 py-3 text-muted" colspan="4">Failed to load data.</td>
          </tr>
          <tr v-else-if="rows.length === 0">
            <td class="px-3 py-3 text-muted" colspan="4">No headlines available.</td>
          </tr>
          <tr v-else v-for="item in rows" :key="item.id">
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
import { onBeforeUnmount, onMounted } from "vue";

const { data: rows, pending, error, refresh } = useNews();
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
    return "bg-green-50 text-positive border border-green-200";
  }
  if (sentiment === "Negative") {
    return "bg-red-50 text-negative border border-red-200";
  }
  return "bg-slate-50 text-neutral border border-slate-200";
};
</script>
