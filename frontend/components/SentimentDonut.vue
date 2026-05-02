<template>
  <div class="card p-4">
    <div class="flex items-center justify-between">
      <h2 class="text-base font-semibold text-ink">Sentiment Overview</h2>
      <span class="text-xs text-muted">24h rolling</span>
    </div>
    <div class="mt-4">
      <ClientOnly>
        <VChart class="h-56" :option="option" autoresize />
      </ClientOnly>
    </div>
    <div class="mt-4 grid grid-cols-3 gap-2 text-xs">
      <div class="flex items-center gap-2">
        <span class="h-2 w-2 rounded-full bg-positive"></span>
        <span class="text-muted">Positive</span>
        <span class="ml-auto font-medium text-ink">{{ values.positive }}</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="h-2 w-2 rounded-full bg-negative"></span>
        <span class="text-muted">Negative</span>
        <span class="ml-auto font-medium text-ink">{{ values.negative }}</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="h-2 w-2 rounded-full bg-neutral"></span>
        <span class="text-muted">Neutral</span>
        <span class="ml-auto font-medium text-ink">{{ values.neutral }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import VChart from "vue-echarts";
import { use } from "echarts/core";
import { PieChart } from "echarts/charts";
import {
  TooltipComponent,
  LegendComponent
} from "echarts/components";
import { CanvasRenderer } from "echarts/renderers";

use([PieChart, TooltipComponent, LegendComponent, CanvasRenderer]);

const { data: rows } = useNews();

const values = computed(() => {
  const base = { positive: 0, negative: 0, neutral: 0 };
  for (const item of rows.value ?? []) {
    if (item.sentiment === "Positive") {
      base.positive += 1;
    } else if (item.sentiment === "Negative") {
      base.negative += 1;
    } else {
      base.neutral += 1;
    }
  }
  return base;
});

const option = computed(() => ({
  tooltip: {
    trigger: "item",
    borderWidth: 0,
    textStyle: {
      fontSize: 12
    }
  },
  legend: {
    show: false
  },
  series: [
    {
      type: "pie",
      radius: ["55%", "78%"],
      avoidLabelOverlap: true,
      itemStyle: {
        borderRadius: 4,
        borderColor: "#ffffff",
        borderWidth: 2
      },
      label: {
        show: false
      },
      data: [
        { value: values.value.positive, name: "Positive", itemStyle: { color: "#16a34a" } },
        { value: values.value.negative, name: "Negative", itemStyle: { color: "#dc2626" } },
        { value: values.value.neutral, name: "Neutral", itemStyle: { color: "#64748b" } }
      ]
    }
  ]
}));
</script>
