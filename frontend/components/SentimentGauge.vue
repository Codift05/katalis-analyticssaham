<template>
  <div class="card p-4 flex flex-col h-full min-h-[300px]">
    <div class="flex items-center justify-between text-xs text-muted mb-4">
      <h2 class="text-base font-semibold text-ink">Market Mood Index</h2>
      <span>Fear & Greed Gauge</span>
    </div>
    <div class="flex-1 relative min-h-0 mt-4">
      <ClientOnly>
        <VChart style="min-height: 300px; height: 100%; width: 100%;" :option="option" autoresize />
      </ClientOnly>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useNews } from "~/composables/useNews";
import { use } from "echarts/core";
import { GaugeChart } from "echarts/charts";
import { TooltipComponent } from "echarts/components";
import { CanvasRenderer } from "echarts/renderers";
import VChart from "vue-echarts";

use([GaugeChart, TooltipComponent, CanvasRenderer]);

const { data: rows } = useNews();

const option = computed(() => {
  const items = rows.value || [];
  
  let pos = 0;
  let neg = 0;
  
  for (const item of items) {
    if (item.sentiment === 'Positive') pos++;
    else if (item.sentiment === 'Negative') neg++;
  }
  
  const total = items.length || 1;
  // Calculate score 0 to 100
  let score = ((pos - neg) / total) * 50 + 50;
  score = Math.round(score);

  let moodStr = "Neutral";
  let color = "#8892b0";
  if (score <= 35) { moodStr = "Fear"; color = "#f28b82"; }
  else if (score >= 65) { moodStr = "Greed"; color = "#81c995"; }

  return {
    series: [
      {
        type: 'gauge',
        startAngle: 180,
        endAngle: 0,
        center: ['50%', '70%'],
        radius: '90%',
        min: 0,
        max: 100,
        splitNumber: 4,
        axisLine: {
          lineStyle: {
            width: 15,
            color: [
              [0.35, '#f28b82'],
              [0.65, '#8892b0'],
              [1, '#81c995']
            ]
          }
        },
        pointer: {
          length: '60%',
          width: 5,
          itemStyle: { color: '#ccd6f6' }
        },
        axisTick: {
          length: 12,
          lineStyle: { color: 'auto', width: 2 }
        },
        splitLine: {
          length: 20,
          lineStyle: { color: 'auto', width: 3 }
        },
        axisLabel: {
          color: '#ccd6f6',
          distance: -40,
          fontSize: 10,
          formatter: function (value: number) {
            if (value === 0) return 'Fear';
            else if (value === 50) return 'Neutral';
            else if (value === 100) return 'Greed';
            return '';
          }
        },
        title: {
          offsetCenter: [0, '-25%'],
          fontSize: 18,
          color: color,
          fontWeight: '500'
        },
        detail: {
          fontSize: 32,
          offsetCenter: [0, '20%'],
          valueAnimation: true,
          formatter: '{value}',
          color: 'inherit',
          fontWeight: 'bold'
        },
        data: [
          {
            value: score,
            name: moodStr
          }
        ]
      }
    ]
  };
});
</script>
