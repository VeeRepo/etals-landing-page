<script setup lang="ts">
import { Head } from '@inertiajs/vue3';
import Waves from '@/Shared/Components/Animations/Waves.vue';
import EtalsLogo from '@/components/landing/EtalsLogo.vue';
import { ref, onMounted, computed, provide } from 'vue';

defineProps<{
    title?: string;
}>();

const isDark = ref(false);

// Provide dark mode state to all child components
provide('isDark', isDark);

const waveColor = computed(() => isDark.value ? 'rgba(240, 109, 52, 0.12)' : 'rgba(234, 88, 12, 0.08)');

const toggleDarkMode = () => {
    isDark.value = !isDark.value;
    localStorage.setItem('darkMode', isDark.value ? 'true' : 'false');
};

onMounted(() => {
    const savedMode = localStorage.getItem('darkMode');
    if (savedMode === 'true') {
        isDark.value = true;
    } else if (savedMode === 'false') {
        isDark.value = false;
    } else {
        // Only use system preference if no saved preference
        isDark.value = window.matchMedia('(prefers-color-scheme: dark)').matches;
    }
});
</script>

<template>
    <Head :title="title" />

    <div 
        :class="['relative min-h-screen w-full transition-colors duration-500', isDark ? 'dark' : '']"
        :style="{ backgroundColor: isDark ? 'rgb(22, 22, 22)' : 'rgb(245 245 239)' }"
    >
        <Waves
            :line-color="waveColor"
            background-color="transparent"
            :wave-speed-x="0.02"
            :wave-speed-y="0.01"
            :wave-amp-x="40"
            :wave-amp-y="20"
            :friction="0.9"
            :tension="0.01"
            :max-cursor-move="120"
            :x-gap="12"
            :y-gap="36"
            class-name="pointer-events-none"
        />

        <div class="relative z-10 flex flex-col min-h-screen">
            <!-- Floating Header -->
            <header class="fixed top-0 left-0 right-0 z-40 pt-4 md:pt-6">
                <div class="container mx-auto px-4">
                    <nav 
                        class="relative flex items-center justify-between h-16 md:h-[72px] px-4 md:px-8 rounded-full backdrop-blur-xl transition-all duration-500"
                        :class="isDark 
                            ? 'bg-[#1e1e1e]/90 shadow-[0_8px_32px_rgba(0,0,0,0.4),0_0_0_1px_rgba(255,255,255,0.05)_inset]' 
                            : 'bg-[#FAFAF2]/90 shadow-[0_8px_32px_rgba(0,0,0,0.08),0_0_0_1px_rgba(255,255,255,0.8)_inset]'"
                    >
                        <!-- Logo -->
                        <a href="/" class="flex items-center flex-shrink-0">
                            <EtalsLogo class="h-7 md:h-9 w-auto" :is-dark="isDark" />
                        </a>

                        <!-- Center Navigation -->
                        <div class="hidden md:flex items-center gap-8 absolute left-1/2 -translate-x-1/2">
                            <a 
                                href="#features" 
                                class="text-sm font-medium hover:text-[#F06D34] transition-colors"
                                :class="isDark ? 'text-white/80' : 'text-[#1C1D21]/80'"
                            >Features</a>
                            <a 
                                href="#products" 
                                class="text-sm font-medium hover:text-[#F06D34] transition-colors"
                                :class="isDark ? 'text-white/80' : 'text-[#1C1D21]/80'"
                            >Products</a>
                            <a 
                                href="#about" 
                                class="text-sm font-medium hover:text-[#F06D34] transition-colors"
                                :class="isDark ? 'text-white/80' : 'text-[#1C1D21]/80'"
                            >About</a>
                        </div>

                        <!-- Right Actions -->
                        <div class="flex items-center gap-3 md:gap-4">
                            <!-- Dark Mode Toggle -->
                            <button 
                                @click="toggleDarkMode"
                                class="relative w-12 h-7 rounded-full p-1 transition-colors duration-300 flex-shrink-0"
                                :style="{ backgroundColor: isDark ? '#F06D34' : '#e5e5e5' }"
                                aria-label="Toggle dark mode"
                            >
                                <div 
                                    class="absolute top-0.5 w-6 h-6 rounded-full bg-white shadow-md transition-all duration-300 flex items-center justify-center"
                                    :class="isDark ? 'left-[22px]' : 'left-0.5'"
                                >
                                    <!-- Sun icon -->
                                    <svg v-if="!isDark" class="w-3.5 h-3.5 text-[#F06D34]" fill="currentColor" viewBox="0 0 20 20">
                                        <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd"/>
                                    </svg>
                                    <!-- Moon icon -->
                                    <svg v-else class="w-3.5 h-3.5 text-[#F06D34]" fill="currentColor" viewBox="0 0 20 20">
                                        <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
                                    </svg>
                                </div>
                            </button>

                            <!-- Login Link -->
                            <a 
                                href="/login" 
                                class="hidden sm:block text-sm font-medium hover:text-[#F06D34] transition-colors"
                                :class="isDark ? 'text-white/80' : 'text-[#1C1D21]/80'"
                            >Log In</a>

                            <!-- Get Started Button -->
                            <a 
                                href="/register" 
                                class="px-5 md:px-6 py-2.5 bg-gradient-to-r from-[#F06D34] to-[#ff8c5a] text-white text-sm font-semibold hover:scale-105 active:scale-95 transition-all duration-300 rounded-full shadow-[0_4px_16px_rgba(240,109,52,0.4)]"
                            >
                                Get Started
                            </a>
                        </div>
                    </nav>
                </div>
            </header>

            <main class="flex-grow pt-24 md:pt-28">
                <slot :is-dark="isDark" />
            </main>

            <footer 
                class="relative overflow-hidden transition-colors duration-500"
                :style="{ backgroundColor: isDark ? 'rgb(22, 22, 22)' : '#FAFAF2' }"
            >
                <!-- Top Section with Navigation -->
                <div class="container mx-auto px-4 pt-24 pb-12">
                    <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-8 lg:gap-12">
                        <!-- Brand Column -->
                        <div class="col-span-2 lg:col-span-1">
                            <p 
                                class="text-base leading-relaxed mb-8 max-w-sm"
                                :class="isDark ? 'text-white/50' : 'text-[#1C1D21]/60'"
                            >
                                Scale product content across markets, fast. From microcopy to full catalogs.
                            </p>
                            <!-- Social Icons -->
                            <div class="flex items-center gap-3">
                                <a 
                                    href="#" 
                                    class="group w-9 h-9 rounded-full flex items-center justify-center transition-all duration-300 hover:scale-110"
                                    :class="isDark ? 'bg-white/5 hover:bg-[#F06D34]' : 'bg-black/5 hover:bg-[#F06D34]'"
                                >
                                    <svg class="w-4 h-4 transition-colors" :class="isDark ? 'text-white/60 group-hover:text-white' : 'text-[#1C1D21]/60 group-hover:text-white'" fill="currentColor" viewBox="0 0 24 24">
                                        <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                                    </svg>
                                </a>
                                <a 
                                    href="#" 
                                    class="group w-9 h-9 rounded-full flex items-center justify-center transition-all duration-300 hover:scale-110"
                                    :class="isDark ? 'bg-white/5 hover:bg-[#F06D34]' : 'bg-black/5 hover:bg-[#F06D34]'"
                                >
                                    <svg class="w-4 h-4 transition-colors" :class="isDark ? 'text-white/60 group-hover:text-white' : 'text-[#1C1D21]/60 group-hover:text-white'" fill="currentColor" viewBox="0 0 24 24">
                                        <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                                    </svg>
                                </a>
                                <a 
                                    href="#" 
                                    class="group w-9 h-9 rounded-full flex items-center justify-center transition-all duration-300 hover:scale-110"
                                    :class="isDark ? 'bg-white/5 hover:bg-[#F06D34]' : 'bg-black/5 hover:bg-[#F06D34]'"
                                >
                                    <svg class="w-4 h-4 transition-colors" :class="isDark ? 'text-white/60 group-hover:text-white' : 'text-[#1C1D21]/60 group-hover:text-white'" fill="currentColor" viewBox="0 0 24 24">
                                        <path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
                                    </svg>
                                </a>
                            </div>
                        </div>

                        <!-- Product Column -->
                        <div>
                            <h4 
                                class="text-xs font-semibold uppercase tracking-[0.2em] mb-5"
                                :class="isDark ? 'text-white/30' : 'text-[#1C1D21]/40'"
                            >Product</h4>
                            <ul class="space-y-3">
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Setup Onboarding</a>
                                </li>
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Produce</a>
                                </li>
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Insight</a>
                                </li>
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Content Studio</a>
                                </li>
                            </ul>
                        </div>

                        <!-- Resources Column -->
                        <div>
                            <h4 
                                class="text-xs font-semibold uppercase tracking-[0.2em] mb-5"
                                :class="isDark ? 'text-white/30' : 'text-[#1C1D21]/40'"
                            >Resources</h4>
                            <ul class="space-y-3">
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Documentation</a>
                                </li>
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >API Reference</a>
                                </li>
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Guides</a>
                                </li>
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Status</a>
                                </li>
                            </ul>
                        </div>

                        <!-- Company Column -->
                        <div>
                            <h4 
                                class="text-xs font-semibold uppercase tracking-[0.2em] mb-5"
                                :class="isDark ? 'text-white/30' : 'text-[#1C1D21]/40'"
                            >Company</h4>
                            <ul class="space-y-3">
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >About</a>
                                </li>
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Blog</a>
                                </li>
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Careers</a>
                                </li>
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Contact</a>
                                </li>
                            </ul>
                        </div>

                        <!-- Legal Column -->
                        <div>
                            <h4 
                                class="text-xs font-semibold uppercase tracking-[0.2em] mb-5"
                                :class="isDark ? 'text-white/30' : 'text-[#1C1D21]/40'"
                            >Legal</h4>
                            <ul class="space-y-3">
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Privacy</a>
                                </li>
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Terms</a>
                                </li>
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Cookies</a>
                                </li>
                                <li>
                                    <a 
                                        href="#" 
                                        class="text-sm transition-colors duration-200 hover:text-[#F06D34]"
                                        :class="isDark ? 'text-white/60' : 'text-[#1C1D21]/70'"
                                    >Licenses</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Full-Width Giant Etals Logo Section -->
                <div class="relative overflow-hidden pt-8">
                    <!-- Giant Etals Logo - Full Width -->
                    <div class="relative flex justify-center items-center px-4">
                        <svg 
                            xmlns="http://www.w3.org/2000/svg" 
                            viewBox="0 0 405.672 134.53" 
                            class="w-full max-w-[1600px] h-auto select-none transition-all duration-500"
                            style="opacity: 1;"
                        >
                            <defs>
                                <clipPath clipPathUnits="userSpaceOnUse" id="footerClipPath">
                                    <path d="M 0,1080 H 1920 V 0 H 0 Z" transform="translate(-599.29991,-599.30872)"/>
                                </clipPath>
                                <linearGradient id="footerLogoGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                                    <stop offset="0%" :style="{ stopColor: isDark ? 'rgba(240,109,52,0.15)' : 'rgba(240,109,52,0.2)' }" />
                                    <stop offset="50%" :style="{ stopColor: isDark ? 'rgba(240,109,52,0.35)' : 'rgba(240,109,52,0.45)' }" />
                                    <stop offset="100%" :style="{ stopColor: isDark ? 'rgba(240,109,52,0.15)' : 'rgba(240,109,52,0.2)' }" />
                                </linearGradient>
                                <linearGradient id="footerTextGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                                    <stop offset="0%" :style="{ stopColor: isDark ? 'rgba(255,255,255,0.04)' : 'rgba(28,29,33,0.06)' }" />
                                    <stop offset="50%" :style="{ stopColor: isDark ? 'rgba(255,255,255,0.12)' : 'rgba(28,29,33,0.14)' }" />
                                    <stop offset="100%" :style="{ stopColor: isDark ? 'rgba(255,255,255,0.04)' : 'rgba(28,29,33,0.06)' }" />
                                </linearGradient>
                            </defs>
                            <g transform="matrix(0.369925, 0, 0, 0.369925, 128.7173, 4.679648)">
                                <g transform="matrix(1, 0, 0, 1, -1051.206299, -536.998596)">
                                    <!-- Orange icon part with gradient -->
                                    <path 
                                        d="M 0,0 C 7.375,0 13.354,-5.979 13.354,-13.354 H -13.354 C -13.354,-5.979 -7.375,0 0,0 m 138.008,-119.102 c -0.243,-0.555 -0.581,-1.08 -1.035,-1.534 -19.611,-19.612 -45.684,-30.411 -73.417,-30.411 -27.734,0 -53.807,10.799 -73.417,30.411 -19.611,19.609 -30.411,45.682 -30.411,73.416 0,2.763 2.241,5.004 5.004,5.004 2.764,0 5.005,-2.241 5.005,-5.004 0,-16.878 4.432,-33.072 12.736,-47.262 0.085,0 0.168,0.006 0.253,0.006 4.005,-6.824 8.904,-13.184 14.646,-18.927 17.679,-17.678 41.183,-27.414 66.184,-27.414 25,0 48.504,9.736 66.182,27.414 4.886,4.886 4.886,12.808 0,17.693 -4.886,4.885 -12.806,4.885 -17.692,0 -12.953,-12.953 -30.174,-20.085 -48.49,-20.085 -18.318,0 -35.539,7.132 -48.491,20.085 -1.547,1.547 -2.995,3.163 -4.369,4.829 -0.171,0.206 -0.337,0.414 -0.505,0.622 -0.461,0.571 -0.912,1.148 -1.353,1.731 -0.24,0.317 -0.48,0.634 -0.715,0.955 -0.11,0.152 -0.228,0.299 -0.338,0.452 0.005,0.003 0.009,0.006 0.013,0.009 -8.306,11.558 -12.803,25.376 -12.803,39.892 0,2.763 2.241,5.004 5.005,5.004 2.764,0 5.004,-2.241 5.004,-5.004 0,-15.64 6.091,-30.344 17.15,-41.403 11.059,-11.058 25.762,-17.149 41.402,-17.149 15.639,0 30.342,6.091 41.401,17.149 0.34,0.34 0.725,0.599 1.125,0.821 3.943,4.912 3.64,12.108 -0.917,16.665 -4.885,4.884 -12.806,4.884 -17.692,0 -6.389,-6.389 -14.883,-9.907 -23.917,-9.907 -9.035,0 -17.529,3.518 -23.918,9.907 -6.389,6.387 -9.907,14.882 -9.907,23.917 0,3.467 0.523,6.854 1.523,10.074 h 90.22 v 0.015 c 11.901,0.146 23.757,4.749 32.837,13.829 18.457,18.457 18.456,48.382 -0.001,66.838 -24.242,24.241 -56.472,37.592 -90.754,37.592 -34.283,0 -66.514,-13.351 -90.757,-37.593 -24.241,-24.242 -37.592,-56.473 -37.592,-90.755 0,-0.013 0.001,-0.025 0.001,-0.038 0.01,-34.268 13.359,-66.485 37.592,-90.717 24.24,-24.242 56.472,-37.593 90.756,-37.593 34.283,0 66.514,13.351 90.755,37.593 4.886,4.886 4.886,12.806 0,17.692 -4.448,4.447 -11.404,4.833 -16.303,1.181" 
                                        fill="url(#footerLogoGradient)"
                                        class="transition-all duration-500"
                                        transform="matrix(1.3333333,0,0,-1.3333333,799.06653,640.92173)" 
                                        clip-path="url(#footerClipPath)"
                                    />
                                    <!-- "etals" text with gradient -->
                                    <path 
                                        d="M 1169.91 641.517 C 1156.73 641.517 1144.54 643.888 1133.33 648.627 C 1122.12 653.357 1112.41 659.884 1104.2 668.205 C 1096.01 676.529 1089.65 686.353 1085.14 697.673 C 1080.64 708.998 1078.39 721.361 1078.39 734.767 C 1078.39 748.404 1080.88 760.884 1085.85 772.205 C 1090.81 783.529 1097.74 793.295 1106.64 801.502 C 1115.54 809.712 1126.05 816.127 1138.19 820.752 C 1150.32 825.365 1163.44 827.673 1177.53 827.673 C 1192.78 827.673 1206.53 825.65 1218.78 821.611 C 1231.03 817.572 1242.7 810.58 1253.8 800.642 L 1226.06 763.189 C 1221.21 767.587 1214.79 771.517 1206.81 774.986 C 1198.85 778.455 1189.66 780.189 1179.27 780.189 C 1174.18 780.189 1169.21 779.556 1164.36 778.283 C 1159.51 777.013 1155.17 774.994 1151.36 772.22 C 1147.55 769.439 1144.37 766.087 1141.83 762.158 C 1139.29 758.232 1137.66 753.607 1136.97 748.283 L 1253.45 748.283 C 1253.91 746.212 1254.43 743.041 1255 738.767 C 1255.58 734.486 1255.88 729.689 1255.88 724.377 C 1255.88 712.357 1253.8 701.322 1249.64 691.267 C 1245.49 681.216 1239.59 672.494 1231.95 665.095 C 1224.33 657.701 1215.26 651.923 1204.74 647.767 C 1194.22 643.603 1182.61 641.517 1169.91 641.517 L 1169.91 641.517 Z M 1169.56 687.283 C 1174.18 687.283 1178.33 687.978 1182.03 689.361 C 1185.73 690.748 1188.91 692.654 1191.56 695.08 C 1194.23 697.509 1196.43 700.455 1198.16 703.923 C 1199.9 707.384 1200.88 711.197 1201.11 715.361 L 1136.28 715.361 C 1136.97 711.197 1138.24 707.384 1140.08 703.923 C 1141.93 700.455 1144.24 697.509 1147.02 695.08 C 1149.8 692.654 1153.1 690.748 1156.91 689.361 C 1160.72 687.978 1164.94 687.283 1169.56 687.283 L 1169.56 687.283 Z M 1334.93 823.517 L 1334.93 685.892 L 1330.76 690.048 L 1372.36 690.048 L 1372.36 645.673 L 1330.07 645.673 L 1334.22 649.83 L 1334.22 593.33 L 1278.41 593.33 L 1278.41 649.83 L 1282.57 645.673 L 1244.79 645.673 L 1244.79 690.048 L 1281.88 690.048 L 1277.72 685.892 L 1277.72 823.517 L 1334.93 823.517 Z M 1453.83 778.111 C 1459.14 778.111 1464.16 777.127 1468.91 775.158 C 1473.65 773.189 1477.75 770.298 1481.22 766.486 C 1484.69 762.673 1487.4 758.111 1489.36 752.798 C 1491.33 747.486 1492.31 741.591 1492.31 735.111 C 1492.31 728.642 1491.33 722.752 1489.36 717.439 C 1487.4 712.119 1484.69 707.607 1481.22 703.908 C 1477.75 700.212 1473.7 697.326 1469.08 695.252 C 1464.45 693.17 1459.37 692.127 1453.83 692.127 C 1448.52 692.127 1443.55 693.17 1438.92 695.252 C 1434.3 697.326 1430.25 700.212 1426.78 703.908 C 1423.32 707.607 1420.61 712.119 1418.64 717.439 C 1416.67 722.752 1415.69 728.642 1415.69 735.111 C 1415.69 741.591 1416.67 747.486 1418.64 752.798 C 1420.61 758.111 1423.32 762.673 1426.78 766.486 C 1430.25 770.298 1434.3 773.189 1438.92 775.158 C 1443.55 777.127 1448.52 778.111 1453.83 778.111 Z M 1496.47 798.564 C 1494.38 802.951 1491.44 806.935 1487.63 810.517 C 1483.81 814.103 1479.48 817.107 1474.63 819.533 C 1469.77 821.962 1464.57 823.923 1459.02 825.423 C 1453.47 826.923 1447.58 827.673 1441.35 827.673 C 1430.02 827.673 1419.39 825.478 1409.45 821.095 C 1399.52 816.701 1390.79 810.404 1383.28 802.205 C 1375.77 793.998 1369.82 784.173 1365.42 772.736 C 1361.04 761.291 1358.85 748.517 1358.85 734.423 C 1358.85 720.33 1361.04 707.564 1365.42 696.127 C 1369.82 684.681 1375.71 674.857 1383.11 666.658 C 1390.51 658.451 1399.11 652.213 1408.94 647.939 C 1418.76 643.658 1429.1 641.517 1439.95 641.517 C 1445.51 641.517 1450.99 642.154 1456.42 643.423 C 1461.86 644.697 1466.83 646.486 1471.33 648.798 C 1475.84 651.111 1479.83 653.888 1483.3 657.127 C 1486.77 660.357 1489.66 663.822 1491.97 667.517 L 1489.88 668.908 L 1489.88 645.673 L 1546.74 645.673 L 1546.74 823.517 L 1494.39 823.517 L 1494.39 797.517 L 1496.47 798.564 Z M 1563.37 823.517 L 1620.58 823.517 L 1620.58 564.205 L 1563.37 564.205 L 1563.37 823.517 Z M 1710.35 827.673 C 1721.22 827.673 1731.1 826.228 1739.99 823.345 C 1748.9 820.462 1756.47 816.478 1762.71 811.392 C 1768.95 806.298 1773.8 800.345 1777.26 793.533 C 1780.73 786.712 1782.46 779.486 1782.46 771.861 C 1782.46 764.697 1781.36 758.513 1779.16 753.314 C 1776.98 748.119 1773.63 743.384 1769.12 739.111 C 1764.62 734.83 1758.78 730.841 1751.62 727.142 C 1744.45 723.447 1736.01 719.861 1726.31 716.392 C 1720.06 714.08 1714.69 712.119 1710.18 710.502 C 1705.68 708.888 1701.98 707.388 1699.09 706.002 C 1696.2 704.607 1694.12 703.158 1692.85 701.658 C 1691.58 700.158 1690.95 698.369 1690.95 696.283 C 1690.95 694.212 1691.41 692.423 1692.34 690.923 C 1693.26 689.416 1694.59 688.201 1696.32 687.283 C 1698.05 686.357 1700.01 685.666 1702.21 685.205 C 1704.41 684.736 1706.66 684.502 1708.98 684.502 C 1716.6 684.502 1723.13 686.236 1728.56 689.705 C 1733.99 693.173 1738.33 697.564 1741.56 702.877 L 1777.96 676.533 C 1775.19 671.212 1771.49 666.357 1766.87 661.97 C 1762.24 657.576 1757.04 653.877 1751.26 650.877 C 1745.49 647.869 1739.19 645.556 1732.37 643.939 C 1725.56 642.326 1718.45 641.517 1711.06 641.517 C 1700.42 641.517 1690.71 642.791 1681.93 645.33 C 1673.15 647.873 1665.58 651.572 1659.23 656.423 C 1652.87 661.279 1647.85 666.998 1644.15 673.58 C 1640.45 680.166 1638.6 687.502 1638.6 695.595 C 1638.6 702.994 1639.87 709.525 1642.41 715.189 C 1644.95 720.845 1648.6 725.873 1653.34 730.267 C 1658.08 734.654 1663.85 738.58 1670.66 742.048 C 1677.49 745.517 1685.29 748.638 1694.07 751.408 C 1700.31 753.72 1705.68 755.689 1710.18 757.314 C 1714.69 758.931 1718.45 760.545 1721.45 762.158 C 1724.45 763.775 1726.71 765.392 1728.21 767.017 C 1729.71 768.634 1730.46 770.712 1730.46 773.252 C 1730.46 775.095 1729.94 776.716 1728.9 778.111 C 1727.87 779.498 1726.48 780.654 1724.74 781.58 C 1723.01 782.498 1720.93 783.248 1718.51 783.83 C 1716.08 784.404 1713.25 784.689 1710.01 784.689 C 1701 784.689 1692.85 782.322 1685.57 777.58 C 1678.29 772.841 1672.45 766.892 1668.07 759.736 L 1632.01 787.47 C 1635.48 794.17 1639.92 800.002 1645.35 804.97 C 1650.79 809.939 1656.86 814.103 1663.56 817.455 C 1670.26 820.798 1677.54 823.337 1685.4 825.064 C 1693.25 826.802 1701.57 827.673 1710.35 827.673 L 1710.35 827.673 Z M 1710.35 827.673" 
                                        fill="url(#footerTextGradient)"
                                        class="transition-all duration-500"
                                    />
                                </g>
                            </g>
                        </svg>
                    </div>

                    <!-- Decorative accent line -->
                    <div class="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-[#F06D34]/40 to-transparent"></div>
                </div>

                <!-- Bottom Bar -->
                <div 
                    class="border-t transition-colors duration-500"
                    :class="isDark ? 'border-white/5' : 'border-black/5'"
                >
                    <div class="container mx-auto px-4 py-5">
                        <div class="flex flex-col sm:flex-row justify-between items-center gap-4">
                            <p 
                                class="text-xs transition-colors duration-200"
                                :class="isDark ? 'text-white/30' : 'text-[#1C1D21]/40'"
                            >
                                © 2025 Etals Studio. All rights reserved.
                            </p>
                            <div class="flex items-center gap-6">
                                <span 
                                    class="text-xs"
                                    :class="isDark ? 'text-white/30' : 'text-[#1C1D21]/40'"
                                >
                                    Built with 
                                    <span class="text-[#F06D34]">♥</span> 
                                    in Stockholm
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </footer>
        </div>
    </div>
</template>
