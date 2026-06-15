<template>
  <div class="card p-4 flex flex-col h-full min-h-[300px]">
    <div class="flex items-center justify-between text-xs text-muted mb-4">
      <h2 class="text-base font-semibold text-ink">Sentiment Trend (24h)</h2>
      <span>Cumulative Series</span>
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
import { useNews } from "~/composables/useNews";
import { use } from "echarts/core";
import { LineChart } from "echarts/charts";
import { TooltipComponent, LegendComponent, GridComponent } from "echarts/components";
import { CanvasRenderer } from "echarts/renderers";
import VChart from "vue-echarts";

use([LineChart, TooltipComponent, LegendComponent, GridComponent, CanvasRenderer]);

const { data: rows } = useNews();

const option = computed(() => {
  const parseTime = (dateStr?: string | null) => {
    if (!dateStr) return Date.now();
    const clean = dateStr.split('.')[0]; // remove microseconds
    const t = new Date(clean).getTime();
    return isNaN(t) ? Date.now() : t;
  };

  const items = [...(rows.value || [])].sort((a, b) => {
    return parseTime(a.created_at) - parseTime(b.created_at);
  });

  let posSum = 0;
  let negSum = 0;
  let neuSum = 0;

  const posData: number[] = [];
  const negData: number[] = [];
  const neuData: number[] = [];
  const timeLabels: string[] = [];

  for (const item of items) {
    const t = parseTime(item.created_at);
    const d = new Date(t);
    const label = `${d.getHours().toString().padStart(2, '0')}:${d.getMinutes().toString().padStart(2, '0')}`;
    timeLabels.push(label);

    if (item.sentiment === 'Positive') posSum++;
    else if (item.sentiment === 'Negative') negSum++;
    else neuSum++;

    posData.push(posSum);
    negData.push(negSum);
    neuData.push(neuSum);
  }

  return {
    tooltip: { trigger: 'axis' },
    legend: {
      data: ['Positive', 'Negative', 'Neutral'],
      textStyle: { color: '#8892b0', fontSize: 10 },
      bottom: 0,
      icon: 'circle'
    },
    grid: { left: '3%', right: '4%', bottom: '15%', top: '5%', containLabel: true },
    xAxis: {
      type: 'category',
      data: timeLabels,
      splitLine: { show: false },
      axisLabel: { color: '#8892b0' }
    },
    yAxis: {
      type: 'value',
      splitLine: { lineStyle: { color: '#23304a' } },
      axisLabel: { color: '#8892b0' }
    },
    series: [
      { name: 'Positive', type: 'line', showSymbol: false, itemStyle: { color: '#81c995' }, lineStyle: { width: 2 }, data: posData },
      { name: 'Negative', type: 'line', showSymbol: false, itemStyle: { color: '#f28b82' }, lineStyle: { width: 2 }, data: negData },
      { name: 'Neutral', type: 'line', showSymbol: false, itemStyle: { color: '#8892b0' }, lineStyle: { width: 2, type: 'dashed' }, data: neuData }
    ]
  };
});
</script>
