<script setup lang="ts">
import { Head } from '@inertiajs/vue3';
import Waves from '@/Shared/Components/Animations/Waves.vue';

defineProps<{
    title?: string;
}>();
</script>

<template>
    <Head :title="title" />

    <div class="relative min-h-screen w-full" style="background-color: #FDF8F3">
        <Waves
            line-color="rgba(234, 88, 12, 0.15)"
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
            <!-- Header (Simplified for now, can be extracted later) -->
            <header class="fixed top-0 left-0 right-0 z-40 border-b border-black/5 bg-transparent backdrop-blur-sm">
                <div class="container mx-auto px-4 h-20 flex items-center justify-between">
                    <div class="text-2xl font-bold uppercase tracking-tighter text-black">
                        Etals
                    </div>
                    <nav class="hidden md:flex items-center gap-8">
                        <a href="#features" class="text-sm uppercase tracking-widest text-black hover:text-orange-500 transition-colors">Features</a>
                        <a href="#products" class="text-sm uppercase tracking-widest text-black hover:text-orange-500 transition-colors">Products</a>
                    </nav>
                    <div class="flex items-center gap-4">
                        <a href="/login" class="text-sm uppercase tracking-widest text-black hover:text-orange-500 transition-colors">Login</a>
                        <a href="/register" class="px-6 py-2 bg-orange-500 text-white font-bold uppercase tracking-tighter hover:scale-105 active:scale-95 transition-transform rounded-full">
                            Get App
                        </a>
                    </div>
                </div>
            </header>

            <main class="flex-grow pt-20">
                <slot />
            </main>

            <footer class="border-t border-black/5 py-20 bg-transparent">
                <div class="container mx-auto px-4">
                    <div class="grid grid-cols-1 md:grid-cols-4 gap-12">
                        <div class="col-span-1 md:col-span-2">
                            <div class="text-6xl font-bold uppercase tracking-tighter mb-8 text-black">
                                Etals
                            </div>
                            <p class="text-gray-600 max-w-md text-lg">
                                Scale product content across markets, fast. From microcopy to full catalogs.
                            </p>
                        </div>
                        <div>
                            <h4 class="text-sm uppercase tracking-widest text-gray-500 mb-6">Product</h4>
                            <ul class="space-y-4">
                                <li><a href="#" class="text-gray-600 hover:text-orange-500 transition-colors">Setup Onboarding</a></li>
                                <li><a href="#" class="text-gray-600 hover:text-orange-500 transition-colors">Produce</a></li>
                                <li><a href="#" class="text-gray-600 hover:text-orange-500 transition-colors">Insight</a></li>
                                <li><a href="#" class="text-gray-600 hover:text-orange-500 transition-colors">Content Studio</a></li>
                            </ul>
                        </div>
                        <div>
                            <h4 class="text-sm uppercase tracking-widest text-gray-500 mb-6">Company</h4>
                            <ul class="space-y-4">
                                <li><a href="#" class="text-gray-600 hover:text-orange-500 transition-colors">About</a></li>
                                <li><a href="#" class="text-gray-600 hover:text-orange-500 transition-colors">Blog</a></li>
                                <li><a href="#" class="text-gray-600 hover:text-orange-500 transition-colors">Careers</a></li>
                                <li><a href="#" class="text-gray-600 hover:text-orange-500 transition-colors">Contact</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="mt-20 pt-8 border-t border-black/5 flex flex-col md:flex-row justify-between items-center gap-4">
                        <p class="text-gray-500 text-sm">© 2025 Etals Studio. All rights reserved.</p>
                        <div class="flex gap-6">
                            <a href="#" class="text-gray-500 hover:text-orange-500 transition-colors">Privacy</a>
                            <a href="#" class="text-gray-500 hover:text-orange-500 transition-colors">Terms</a>
                        </div>
                    </div>
                </div>
            </footer>
        </div>
    </div>
</template>
