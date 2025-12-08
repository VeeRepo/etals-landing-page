<script setup lang="ts">
import LandingLayout from '@/layouts/LandingLayout.vue';
import KineticButton from '@/components/landing/KineticButton.vue';
import { Head, Link } from '@inertiajs/vue3';
import { useMotion } from '@vueuse/motion';
import { ref } from 'vue';

const heroText = ref(null);
const heroSub = ref(null);

useMotion(heroText, {
    initial: { opacity: 0, y: 50 },
    enter: { opacity: 1, y: 0, transition: { duration: 800, ease: 'easeOut' } },
});

useMotion(heroSub, {
    initial: { opacity: 0, y: 30 },
    enter: { opacity: 1, y: 0, transition: { duration: 800, delay: 200, ease: 'easeOut' } },
});
</script>

<template>
    <LandingLayout>
        <Head title="Etals - Scale Product Content" />

        <!-- Spacer for fixed header -->
        <div class="h-20 md:h-32"></div>

        <!-- HERO SECTION -->
        <section class="container mx-auto px-4 py-12 md:py-24 flex flex-col items-start gap-8 min-h-[60vh] justify-center">
            <!-- Helix AI Style: Simple, Massive, Left aligned or Justified -->
            <h1 ref="heroText" class="text-6xl md:text-9xl font-bold uppercase tracking-tighter leading-[0.85] text-black mb-6">
                Scale Product <br />
                <span class="text-orange-500">Content</span>
            </h1>

            <div ref="heroSub" class="max-w-2xl pl-1">
                <p class="text-xl md:text-2xl text-gray-600 leading-relaxed">
                    Etals is the engine of growth. <br />
                    From microcopy to full catalogs, we define the shape of your global presence.
                </p>

                <div class="mt-8 flex flex-wrap gap-4">
                    <KineticButton href="/register" size="lg" class="bg-black text-white hover:bg-black/90 hover:scale-105 active:scale-95 transition-all">
                        Get Started
                    </KineticButton>
                    <KineticButton href="#demo" variant="outline" size="lg" class="border-black text-black hover:bg-black hover:text-white transition-all">
                        View Demo
                    </KineticButton>
                </div>
            </div>
        </section>

        <!-- LARGE TEXT SECTION -->
        <section class="container mx-auto px-4 py-24 md:py-32 border-t border-black/5">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
                <h2 class="text-4xl md:text-6xl font-bold uppercase tracking-tighter leading-none text-black">
                    The <span class="text-orange-500">Language</span> <br /> of Commerce
                </h2>
                <div class="text-lg md:text-xl text-gray-600 leading-relaxed">
                    <p class="mb-6">
                        Just as Helix decodes biology, Etals decodes the complex interactions between your product data and your customers.
                    </p>
                    <p>
                        Our platform unifies creation, translation, and distribution into a single, seamless workflow.
                    </p>
                </div>
            </div>
        </section>

        <!-- FEATURES GRID (Minimal) -->
        <section class="container mx-auto px-4 py-24 mb-24">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Feature 1 -->
                <div class="group p-8 border border-black/5 hover:border-orange-500/30 transition-colors bg-white/40 backdrop-blur-sm rounded-lg">
                    <div class="h-12 w-12 bg-orange-100 text-orange-600 flex items-center justify-center rounded-full mb-6">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-zap"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                    </div>
                    <h3 class="text-2xl font-bold uppercase tracking-tighter mb-4 text-black">Instant Generation</h3>
                    <p class="text-gray-600">
                        Generate comprehensive product descriptions in seconds using our advanced AI models tailored for e-commerce.
                    </p>
                </div>

                <!-- Feature 2 -->
                <div class="group p-8 border border-black/5 hover:border-orange-500/30 transition-colors bg-white/40 backdrop-blur-sm rounded-lg">
                    <div class="h-12 w-12 bg-orange-100 text-orange-600 flex items-center justify-center rounded-full mb-6">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-globe"><circle cx="12" cy="12" r="10"/><line x1="2" x2="22" y1="12" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                    </div>
                    <h3 class="text-2xl font-bold uppercase tracking-tighter mb-4 text-black">Native Translation</h3>
                    <p class="text-gray-600">
                        Expand to new markets with context-aware translations that preserve your brand voice across every language.
                    </p>
                </div>

                <!-- Feature 3 -->
                <div class="group p-8 border border-black/5 hover:border-orange-500/30 transition-colors bg-white/40 backdrop-blur-sm rounded-lg">
                    <div class="h-12 w-12 bg-orange-100 text-orange-600 flex items-center justify-center rounded-full mb-6">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-bar-chart-3"><path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/></svg>
                    </div>
                    <h3 class="text-2xl font-bold uppercase tracking-tighter mb-4 text-black">Performance Insights</h3>
                    <p class="text-gray-600">
                        Track how your content performs with real-time analytics and data-driven optimization suggestions.
                    </p>
                </div>
            </div>
        </section>

        <!-- CTA Section -->
         <section class="container mx-auto px-4 py-24 text-center">
            <h2 class="text-5xl md:text-7xl font-bold uppercase tracking-tighter mb-8 text-black">
                Ready to <span class="text-orange-500">Scale?</span>
            </h2>
             <KineticButton href="/register" size="lg" class="bg-black text-white hover:bg-black/90 hover:scale-105 active:scale-95 transition-all">
                Start Free Now
            </KineticButton>
         </section>

    </LandingLayout>
</template>
