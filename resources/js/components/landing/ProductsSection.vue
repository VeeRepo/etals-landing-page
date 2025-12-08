<script setup lang="ts">
import KineticButton from './KineticButton.vue';

const products = [
    {
        title: 'Setup Onboarding',
        description: 'Get started in minutes with our automated setup wizard.',
        icon: '01'
    },
    {
        title: 'Produce',
        description: 'Generate high-quality content at scale with AI agents.',
        icon: '02'
    },
    {
        title: 'Insight',
        description: 'Real-time analytics and performance tracking for your content.',
        icon: '03'
    },
    {
        title: 'Content Studio',
        description: 'A centralized hub for managing all your creative assets.',
        icon: '04'
    }
];
</script>

<template>
    <section id="products" class="py-32 container mx-auto px-4">
        <div class="mb-20">
            <h2 class="text-[clamp(2.5rem,6vw,6rem)] font-bold uppercase tracking-tighter leading-none mb-8">
                Products
            </h2>
            <div class="h-1 w-full bg-border"></div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div v-for="(product, index) in products" :key="index" 
                class="group relative border-2 border-border bg-card p-12 hover:bg-accent hover:border-accent transition-colors duration-300">
                
                <div class="absolute top-8 right-8 text-6xl font-bold text-muted opacity-20 group-hover:text-black group-hover:opacity-10 transition-all">
                    {{ product.icon }}
                </div>

                <h3 class="text-3xl md:text-4xl font-bold uppercase tracking-tight mb-6 group-hover:text-black transition-colors">
                    {{ product.title }}
                </h3>
                
                <p class="text-xl text-muted-foreground mb-12 group-hover:text-black/80 transition-colors">
                    {{ product.description }}
                </p>

                <div class="flex items-center gap-2 text-accent group-hover:text-black font-bold uppercase tracking-widest text-sm">
                    Learn More 
                    <svg class="w-4 h-4 transform group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="square" stroke-linejoin="miter" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                    </svg>
                </div>
            </div>
        </div>
    </section>
</template>
