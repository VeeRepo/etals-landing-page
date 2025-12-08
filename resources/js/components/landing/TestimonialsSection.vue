<script setup lang="ts">
import { Vue3Marquee } from 'vue3-marquee';

const testimonials = [
    {
        quote: "Etals has completely transformed how we manage our product content globally.",
        author: "Sarah J.",
        role: "Head of Product, TechFlow"
    },
    {
        quote: "The agentic workflow allows us to scale 10x faster than before.",
        author: "Mike R.",
        role: "CTO, ScaleUp Inc"
    },
    {
        quote: "Finally, a tool that understands the complexity of modern e-commerce data.",
        author: "Jessica L.",
        role: "Director of Ops, ShopMax"
    },
    {
        quote: "Seamless integration with our existing stack. It just works.",
        author: "David K.",
        role: "VP Engineering, DataCorp"
    }
];
</script>

<template>
    <section id="testimonials" class="py-32 border-y-2 border-border bg-background overflow-hidden">
        <div class="container mx-auto px-4 mb-20">
            <h2 class="text-[clamp(2.5rem,6vw,6rem)] font-bold uppercase tracking-tighter leading-none mb-8">
                Testimonials
            </h2>
        </div>

        <Vue3Marquee :duration="40" :pause-on-hover="true" :clone="true">
            <div v-for="(testimonial, index) in testimonials" :key="index" 
                class="mx-8 w-[400px] md:w-[600px] p-12 border-2 border-border bg-card flex flex-col justify-between h-[300px] hover:border-accent transition-colors">
                <p class="text-xl md:text-2xl font-medium leading-relaxed mb-8">
                    "{{ testimonial.quote }}"
                </p>
                <div>
                    <div class="font-bold uppercase tracking-widest">{{ testimonial.author }}</div>
                    <div class="text-muted-foreground text-sm uppercase tracking-wider">{{ testimonial.role }}</div>
                </div>
            </div>
        </Vue3Marquee>
    </section>
</template>
