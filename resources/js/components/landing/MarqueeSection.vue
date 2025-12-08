<script setup lang="ts">
import { Vue3Marquee } from 'vue3-marquee';

const logos = [
    'Acme Corp', 'Globex', 'Soylent', 'Initech', 'Umbrella', 'Stark Ind', 'Cyberdyne', 'Massive Dynamic'
];
</script>

<template>
    <section class="py-20 border-y-2 border-border bg-background overflow-hidden">
        <Vue3Marquee :duration="20" :clone="true">
            <div v-for="(logo, index) in logos" :key="index" class="mx-12 flex items-center gap-4 opacity-50 hover:opacity-100 transition-opacity">
                <!-- Placeholder for Logo -->
                <div class="h-12 w-12 bg-muted rounded-none"></div>
                <span class="text-2xl font-bold uppercase tracking-widest">{{ logo }}</span>
            </div>
        </Vue3Marquee>
    </section>
</template>
