<template>
  <div class="flex justify-between items-center transition-opacity duration-300" :class="{ 'opacity-70': blink }">
     <div>
       <div class="text-ink font-medium">{{ symbol }}</div>
       <div class="text-muted text-[10px]">{{ name }}</div>
     </div>
     <div class="text-right">
       <div class="text-ink font-mono transition-colors duration-300" :class="{ 'text-positive': blink && isUp, 'text-negative': blink && !isUp }">{{ formattedValue }}</div>
       <div class="text-[10px] font-mono" :class="isUp ? 'text-positive' : 'text-negative'">
         {{ formattedChange }}% {{ isUp ? '↑' : '↓' }}
       </div>
     </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';

const props = defineProps<{
  symbol: string;
  name: string;
  initialValue: number;
  initialChange: number;
}>();

const value = ref(props.initialValue);
const change = ref(props.initialChange);
const blink = ref(false);

const isUp = computed(() => change.value >= 0);

const formattedValue = computed(() => {
  return new Intl.NumberFormat('id-ID', { minimumFractionDigits: 2, maximumFractionDigits: 2 }).format(value.value);
});

const formattedChange = computed(() => {
  const prefix = isUp.value ? '+' : '';
  const val = new Intl.NumberFormat('id-ID', { minimumFractionDigits: 2, maximumFractionDigits: 2 }).format(change.value);
  return `${prefix}${val}`;
});

let timer: ReturnType<typeof setInterval> | null = null;

onMounted(() => {
  // Randomly update between 3 to 8 seconds
  const randomize = () => {
    const delay = Math.floor(Math.random() * 5000) + 3000;
    timer = setTimeout(() => {
      // Small fluctuation
      const fluc = (Math.random() - 0.5) * (props.initialValue * 0.005);
      value.value += fluc;
      
      const changeFluc = (Math.random() - 0.5) * 0.2;
      change.value += changeFluc;
      
      blink.value = true;
      setTimeout(() => { blink.value = false; }, 500);
      
      randomize();
    }, delay);
  };
  randomize();
});

onBeforeUnmount(() => {
  if (timer) clearTimeout(timer);
});
</script>
