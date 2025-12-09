<script setup lang="ts">
import LandingLayout from '@/layouts/LandingLayout.vue';
import KineticButton from '@/components/landing/KineticButton.vue';
import { Head, Link } from '@inertiajs/vue3';
import { useMotion } from '@vueuse/motion';
import { useIntersectionObserver } from '@vueuse/core';
import { ref } from 'vue';
import { Vue3Lottie } from 'vue3-lottie';
import snurranLightAnimation from '../../../public/snurran_orange.json';
import snurranDarkAnimation from '../../../public/snurran_orange_dark.json';


const heroCard = ref(null);
const heroText = ref(null);
const heroSub = ref(null);
const heroBadge = ref(null);
const heroButtons = ref(null);
const heroShapes = ref(null);

const featureCard = ref(null);
const featureText = ref(null);
const featureShapes = ref(null);

const videoHeading = ref(null);
const videoBox = ref(null);

const lottieRef = ref<InstanceType<typeof Vue3Lottie> | null>(null);
const lottieContainer = ref<HTMLElement | null>(null);

const { stop: stopLottieObserver } = useIntersectionObserver(
    lottieContainer,
    ([{ isIntersecting }]) => {
        if (isIntersecting) {
            setTimeout(() => {
                lottieRef.value?.play();
            }, 3000);
            stopLottieObserver();
        }
    },
    { threshold: 0.3 }
);

useMotion(heroBadge, {
    initial: { opacity: 0, y: -20 },
    enter: { opacity: 1, y: 0, transition: { duration: 600, ease: 'easeOut' } },
});

useMotion(heroText, {
    initial: { opacity: 0, y: 50 },
    enter: { opacity: 1, y: 0, transition: { duration: 800, delay: 100, ease: 'easeOut' } },
});

useMotion(heroSub, {
    initial: { opacity: 0, y: 30 },
    enter: { opacity: 1, y: 0, transition: { duration: 800, delay: 250, ease: 'easeOut' } },
});

useMotion(heroButtons, {
    initial: { opacity: 0, y: 20 },
    enter: { opacity: 1, y: 0, transition: { duration: 600, delay: 400, ease: 'easeOut' } },
});

useMotion(heroShapes, {
    initial: { opacity: 0, scale: 0.8 },
    enter: { opacity: 1, scale: 1, transition: { duration: 1000, delay: 300, ease: 'easeOut' } },
});

useMotion(featureText, {
    initial: { opacity: 0, x: -30 },
    visibleOnce: { opacity: 1, x: 0, transition: { duration: 800, ease: 'easeOut' } },
});

useMotion(featureShapes, {
    initial: { opacity: 0, x: 30 },
    visibleOnce: { opacity: 1, x: 0, transition: { duration: 800, delay: 200, ease: 'easeOut' } },
});

useMotion(videoHeading, {
    initial: { opacity: 0, y: 30 },
    visibleOnce: { opacity: 1, y: 0, transition: { duration: 700, ease: 'easeOut' } },
});

useMotion(videoBox, {
    initial: { opacity: 0, y: 50, scale: 0.95 },
    visibleOnce: { opacity: 1, y: 0, scale: 1, transition: { duration: 900, delay: 150, ease: 'easeOut' } },
});
</script>

<template>
    <LandingLayout v-slot="{ isDark }">
        <Head title="Etals - Scale Product Content" />
        
        <!-- HERO SECTION -->
        <section class="container mx-auto px-4 py-8">
            <!-- Hero Card -->
            <div 
                ref="heroCard"
                class="relative overflow-hidden rounded-[2rem] md:rounded-[3rem] p-8 md:p-16 lg:p-20 transition-colors duration-500"
                :style="{ backgroundColor: isDark ? '#1e1e1e' : '#FAFAF2' }"
            >
                <div class="relative z-10 flex flex-col lg:flex-row items-start lg:items-center justify-between gap-12 lg:gap-8">
                    <!-- Left Content -->
                    <div class="flex flex-col gap-6 max-w-2xl">
                        <!-- Badge -->
                        <div 
                            ref="heroBadge" 
                            class="inline-flex items-center gap-2 px-4 py-2 rounded-full backdrop-blur-sm border w-fit"
                            :class="isDark ? 'bg-white/10 border-white/10' : 'bg-white/80 border-black/5'"
                        >
                            <span class="w-2 h-2 rounded-full bg-[#F06D34]"></span>
                            <span 
                                class="text-sm font-medium"
                                :class="isDark ? 'text-white/90' : 'text-[#1C1D21]'"
                            >Join 50,000+ teams already using Etals</span>
                        </div>

                        <!-- Headline -->
                        <h1 
                            ref="heroText"
                            class="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight leading-[1.1]"
                            :class="isDark ? 'text-white' : 'text-[#1C1D21]'"
                        >
                        Elevate Productivity and Redefine What’s Possible
                        </h1>

                        <!-- Description -->
                        <p 
                            ref="heroSub"
                            class="text-lg md:text-xl leading-relaxed max-w-lg"
                            :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                        >
                           We offer solutions produced by seasoned professionals in the eCommerce industry, combining years of experience in the field with the latest in AI technology.


                        </p>

                        <!-- Buttons -->
                        <div ref="heroButtons" class="flex flex-wrap items-center gap-4 mt-2">
                            <a 
                                href="#" 
                                class="inline-flex items-center justify-center px-8 py-4 rounded-full text-white font-semibold text-base transition-all duration-300 hover:scale-105 active:scale-95 hover:shadow-lg bg-[#F06D34]"
                            >
                                Start free trial
                            </a>
                            <a 
                                href="#" 
                                class="inline-flex items-center justify-center gap-2 px-6 py-4 rounded-full font-semibold text-base transition-all duration-300 hover:scale-105 border-2 text-[#F06D34] border-[#F06D34] bg-transparent"
                            >
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M8 5v14l11-7z"/>
                                </svg>
                                Watch demo
                            </a>
                        </div>
                    </div>

                    <!-- Right Decorative Shapes -->
                    <div ref="heroShapes" class="relative w-full lg:w-auto flex-shrink-0">
                        <!-- Octopus images - both loaded, CSS controls visibility -->
                        <div class="relative w-[400px] h-[400px]">
                            <!-- Light mode image -->
                            <img 
                                src="/octopus-light.png" 
                                class="absolute inset-0 w-full h-full object-contain transition-opacity duration-500 delay-100"
                                :class="isDark ? 'opacity-0' : 'opacity-100'"
                                alt="Etals illustration"
                            />
                            <!-- Dark mode image -->
                            <img 
                                src="/octopus-dark.png" 
                                class="absolute inset-0 w-full h-full object-contain transition-opacity duration-500 delay-100"
                                :class="isDark ? 'opacity-100' : 'opacity-0'"
                                alt="Etals illustration"
                            />
                        </div>
                        <div class="hidden relative w-64 h-64 md:w-80 md:h-80 lg:w-96 lg:h-96 mx-auto lg:mx-0">
                            <!-- Background circle (largest, lightest) -->
                            <div 
                                class="absolute top-0 right-0 w-48 md:w-60 lg:w-72 h-48 md:h-60 lg:h-72 rounded-full bg-[#F06D34]"
                                :class="isDark ? 'opacity-20' : 'opacity-30'"
                            ></div>
                            
                            <!-- Middle rounded square -->
                            <div 
                                class="absolute top-8 md:top-12 left-4 md:left-0 w-40 md:w-52 lg:w-64 h-40 md:h-52 lg:h-64 rounded-[2rem] md:rounded-[2.5rem] bg-[#F06D34]"
                                :class="isDark ? 'opacity-60' : 'opacity-70'"
                            ></div>
                            
                            <!-- Front circle (darkest) -->
                            <div 
                                class="absolute bottom-0 left-8 md:left-4 w-36 md:w-44 lg:w-56 h-36 md:h-44 lg:h-56 rounded-full"
                                :class="isDark ? 'bg-white/20' : 'bg-[#1C1D21] opacity-85'"
                            ></div>
                        </div>
                    </div>
                </div>
                <div class="h-[250px]"></div>
            </div>
        </section>

         <!-- VIDEO SECTION -->
         <section class="relative container mx-auto px-4 z-20 pb-16 md:pb-24 mt-[-240px]">
            <!-- Heading -->
            <div ref="videoHeading" class="text-center mb-8 md:mb-12">
                <h2 
                    class="text-2xl md:text-3xl lg:text-4xl font-bold tracking-tight"
                    :class="isDark ? 'text-white' : 'text-[#1C1D21]'"
                >
                    Watch how Etals transforms your business
                </h2>
            </div>

            <!-- Video Box -->
            <div 
                ref="videoBox"
                class="relative w-full max-w-5xl mx-auto aspect-video rounded-[1.5rem] md:rounded-[2rem] overflow-hidden shadow-2xl cursor-pointer group"
                :style="{ background: isDark ? 'linear-gradient(to bottom right, #0a0a0a, #1a1a1a)' : 'linear-gradient(to bottom right, #1C1D21, #2d2e33)' }"
            >
                <!-- Subtle gradient overlay -->
                <div class="absolute inset-0 opacity-40 bg-[radial-gradient(ellipse_at_30%_20%,rgba(240,109,52,0.3)_0%,transparent_50%),radial-gradient(ellipse_at_70%_80%,rgba(240,109,52,0.2)_0%,transparent_50%)]"></div>

                <!-- Decorative shapes in background -->
                <div class="absolute top-8 left-8 w-20 md:w-32 h-20 md:h-32 rounded-full opacity-10 bg-[#F06D34]"></div>
                <div class="absolute bottom-12 right-12 w-24 md:w-40 h-24 md:h-40 rounded-[1rem] rotate-12 opacity-10 bg-[#F06D34]"></div>

                <!-- Play Button -->
                <div class="absolute inset-0 flex items-center justify-center">
                    <div class="relative w-20 h-20 md:w-28 md:h-28 rounded-full flex items-center justify-center transition-all duration-500 group-hover:scale-110 bg-[#F06D34]">
                        <!-- Pulse ring -->
                        <div class="absolute inset-0 rounded-full animate-ping opacity-30 bg-[#F06D34]"></div>
                        <!-- Play icon -->
                        <svg class="w-8 h-8 md:w-10 md:h-10 text-white ml-1" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M8 5v14l11-7z"/>
                        </svg>
                    </div>
                </div>

                <!-- Bottom text hint -->
                <div class="absolute bottom-6 md:bottom-8 left-0 right-0 text-center">
                    <span class="text-white/60 text-sm md:text-base font-medium tracking-wide">Click to play • 2:34</span>
                </div>

            </div>
        </section>

        <!-- FEATURE SECTION -->
        <section class="container mx-auto px-4">
            <!-- Feature Card -->
            <div 
                ref="featureCard"
                class="relative overflow-hidden rounded-[2rem] md:rounded-[3rem] p-8 md:p-16 lg:p-20 transition-colors duration-500"
                :style="{ backgroundColor: isDark ? '#1e1e1e' : '#FAFAF2' }"
            >
                <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-12 lg:gap-16">
                    <!-- Left Content -->
                    <div ref="featureText" class="flex flex-col gap-6 max-w-xl lg:max-w-lg">
                        <!-- Headline -->
                        <h2 
                            class="text-3xl md:text-4xl font-bold tracking-tight leading-[1.2]"
                            :class="isDark ? 'text-white' : 'text-[#1C1D21]'"
                        >
                        We Let Brands Focus On What Really Matters
                        </h2>

                        <!-- Description Paragraphs -->
                        <p 
                            class="text-base md:text-lg leading-relaxed"
                            :class="isDark ? 'text-white/55' : 'text-[#1C1D21]/65'"
                        >
                            Etals Platform centralizes your entire workflow into one intuitive interface, eliminating the need for disjointed tools. By harnessing the power of real-time data and smart automation, we empower your team to focus on high-impact innovation.
                        </p>

                        <p 
                            class="text-base md:text-lg leading-relaxed"
                            :class="isDark ? 'text-white/55' : 'text-[#1C1D21]/65'"
                        >
                            Designed with scalability in mind, our infrastructure adapts seamlessly to your growing needs, ensuring performance never falters. Join a community of forward-thinking organizations that have redefined productivity and achieved unparalleled success with our comprehensive solution.
                        </p>
                    </div>

                    <!-- Right Lottie Animation -->
                    <div ref="featureShapes" class="w-full lg:w-auto flex-shrink-0">
                        <div ref="lottieContainer" class="relative w-full max-w-md lg:w-96 aspect-square mx-auto lg:mx-0">
                            <Vue3Lottie 
                                ref="lottieRef"
                                :animation-data="isDark ? snurranDarkAnimation : snurranLightAnimation"
                                :loop="true"
                                :auto-play="false"
                                class="w-full h-full"
                            />
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <div class="mb-[200px]"></div>

     
    </LandingLayout>
</template>
