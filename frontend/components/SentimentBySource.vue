<template>
  <div class="card p-4 flex flex-col h-full min-h-[300px]">
    <div class="flex items-center justify-between text-xs text-muted mb-4">
      <h2 class="text-base font-semibold text-ink">Sentiment by Source</h2>
      <span>Distribution</span>
    </div>
    <div class="flex-1 relative min-h-0">
      <ClientOnly>
        <VChart class="h-full w-full" :option="option" autoresize />
      </ClientOnly>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { use } from "echarts/core";
import { BarChart } from "echarts/charts";
import { TooltipComponent, LegendComponent, GridComponent } from "echarts/components";
import { CanvasRenderer } from "echarts/renderers";
import VChart from "vue-echarts";

use([BarChart, TooltipComponent, LegendComponent, GridComponent, CanvasRenderer]);

const { data: rows } = useNews();

const option = computed(() => {
  const sourceMap: Record<string, { positive: number, negative: number, neutral: number }> = {};
  
  for (const item of rows.value ?? []) {
    if (!sourceMap[item.source]) {
      sourceMap[item.source] = { positive: 0, negative: 0, neutral: 0 };
    }
    if (item.sentiment === "Positive") sourceMap[item.source].positive++;
    else if (item.sentiment === "Negative") sourceMap[item.source].negative++;
    else sourceMap[item.source].neutral++;
  }

  // Get top sources by total volume
  const sources = Object.keys(sourceMap).sort((a, b) => {
    const totalA = sourceMap[a].positive + sourceMap[a].negative + sourceMap[a].neutral;
    const totalB = sourceMap[b].positive + sourceMap[b].negative + sourceMap[b].neutral;
    return totalB - totalA;
  }).slice(0, 5);

  const posData = sources.map(s => sourceMap[s].positive);
  const negData = sources.map(s => sourceMap[s].negative);
  const neuData = sources.map(s => sourceMap[s].neutral);

  return {
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' },
      borderWidth: 0,
      backgroundColor: '#111827',
      textStyle: { color: '#ccd6f6', fontSize: 12 },
    },
    legend: {
      data: ['Positive', 'Negative', 'Neutral'],
      textStyle: { color: '#8892b0', fontSize: 10 },
      bottom: 0,
      icon: 'circle',
      itemWidth: 8,
      itemHeight: 8
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '15%',
      top: '5%',
      containLabel: true
    },
    xAxis: {
      type: 'value',
      splitLine: { lineStyle: { color: '#23304a' } },
      axisLabel: { color: '#8892b0' }
    },
    yAxis: {
      type: 'category',
      data: sources,
      axisLabel: { color: '#ccd6f6', fontSize: 11, width: 80, overflow: 'truncate' },
      axisLine: { lineStyle: { color: '#23304a' } }
    },
    series: [
      {
        name: 'Positive',
        type: 'bar',
        stack: 'total',
        label: { show: false },
        emphasis: { focus: 'series' },
        itemStyle: { color: '#81c995' },
        data: posData
      },
      {
        name: 'Negative',
        type: 'bar',
        stack: 'total',
        label: { show: false },
        emphasis: { focus: 'series' },
        itemStyle: { color: '#f28b82' },
        data: negData
      },
      {
        name: 'Neutral',
        type: 'bar',
        stack: 'total',
        label: { show: false },
        emphasis: { focus: 'series' },
        itemStyle: { color: '#8892b0' },
        data: neuData
      }
    ]
  };
});
</script>
