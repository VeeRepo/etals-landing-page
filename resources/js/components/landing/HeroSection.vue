<script setup lang="ts">
import KineticButton from './KineticButton.vue';
import { useMotion } from '@vueuse/motion';
import { ref } from 'vue';

const heroText = ref(null);

useMotion(heroText, {
    initial: { opacity: 0, y: 100 },
    enter: { opacity: 1, y: 0, transition: { duration: 800, ease: 'easeOut' } },
});
</script>

<template>
    <section class="relative min-h-screen flex flex-col justify-center items-center overflow-hidden pt-20 pb-32">
        <!-- Background Elements (Video placeholder or massive text) -->
        <div class="absolute inset-0 z-0 opacity-20 pointer-events-none overflow-hidden">
             <!-- Placeholder for video or animated background -->
             <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[150%] h-[150%] bg-[radial-gradient(circle_at_center,var(--color-accent)_0%,transparent_70%)] blur-[100px]"></div>
        </div>

        <div class="container mx-auto px-4 z-10 relative text-center">
            <!-- Label -->
            <div class="mb-8 inline-block border border-accent/30 bg-accent/10 px-4 py-2 backdrop-blur-sm">
                <span class="text-accent uppercase tracking-widest text-sm font-bold">
                    4346 of 10 000 seats left. Get your seat now!
                </span>
            </div>

            <!-- Heading -->
            <h1 ref="heroText" class="text-[clamp(3rem,10vw,12rem)] leading-[0.8] font-bold uppercase tracking-tighter mb-8 text-balance">
                Scale Product <br />
                <span class="text-accent">Content</span> Fast
            </h1>

            <!-- Tagline -->
            <p class="text-xl md:text-2xl text-muted-foreground max-w-3xl mx-auto mb-12 leading-relaxed">
                From microcopy to full catalogs, Etals creates SEO-optimized copy and translations tailored for your brand voice - ready to publish and perform.
            </p>

            <!-- CTA -->
            <div class="flex flex-col md:flex-row gap-6 justify-center items-center">
                <KineticButton href="/register" size="lg">
                    Start Free Trial
                </KineticButton>
                <KineticButton href="#demo" variant="outline" size="lg">
                    Watch Demo
                </KineticButton>
            </div>
        </div>
        
        <!-- Scroll Indicator -->
        <div class="absolute bottom-12 left-1/2 -translate-x-1/2 animate-bounce">
            <svg class="w-8 h-8 text-muted-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="square" stroke-linejoin="miter" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
            </svg>
        </div>
    </section>
</template>
