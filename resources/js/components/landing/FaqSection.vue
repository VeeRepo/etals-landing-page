<script setup lang="ts">
import { ref } from 'vue';

const faqs = [
    {
        question: "Do I need a credit card for the trial?",
        answer: "No, you can start your 14-day free trial without a credit card. We believe in letting you experience the value first."
    },
    {
        question: "Can I cancel self-service subscription anytime?",
        answer: "Yes, you can cancel your subscription at any time from your dashboard. There are no long-term contracts for self-service plans."
    },
    {
        question: "Does it integrate with X tool?",
        answer: "Etals plugs into your existing stack via APIs or MCP servers. We support major e-commerce platforms, PIMs, and CMSs out of the box."
    }
];

const openIndex = ref<number | null>(0);

const toggle = (index: number) => {
    openIndex.value = openIndex.value === index ? null : index;
};
</script>

<template>
    <section id="faq" class="py-32 container mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-20">
            <div>
                <h2 class="text-[clamp(2.5rem,6vw,6rem)] font-bold uppercase tracking-tighter leading-none mb-8">
                    FAQ
                </h2>
                <p class="text-xl text-muted-foreground max-w-md">
                    Everything you need to know about Etals and how we can help you scale.
                </p>
            </div>

            <div class="space-y-4">
                <div v-for="(faq, index) in faqs" :key="index" class="border-b-2 border-border">
                    <button @click="toggle(index)" class="w-full py-8 flex justify-between items-center text-left focus:outline-none group">
                        <span class="text-xl md:text-2xl font-bold uppercase tracking-tight group-hover:text-accent transition-colors">
                            {{ faq.question }}
                        </span>
                        <span class="text-2xl font-mono transition-transform duration-300" :class="{ 'rotate-45 text-accent': openIndex === index }">
                            +
                        </span>
                    </button>
                    <div v-show="openIndex === index" class="pb-8 text-lg text-muted-foreground leading-relaxed animate-in slide-in-from-top-2 fade-in duration-300">
                        {{ faq.answer }}
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
