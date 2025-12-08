<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
    variant?: 'primary' | 'outline' | 'ghost';
    size?: 'sm' | 'default' | 'lg';
    href?: string;
    as?: string;
}>();

const baseClasses = "inline-flex items-center justify-center uppercase tracking-tighter font-bold transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-accent focus:ring-offset-2 focus:ring-offset-background disabled:opacity-50 disabled:pointer-events-none";

const variantClasses = computed(() => {
    switch (props.variant) {
        case 'outline':
            return "border-2 border-border bg-transparent text-black hover:bg-foreground hover:text-background";
        case 'ghost':
            return "bg-transparent text-foreground hover:text-accent";
        case 'primary':
        default:
            return "bg-accent text-accent-foreground hover:scale-105 active:scale-95";
    }
});

const sizeClasses = computed(() => {
    switch (props.size) {
        case 'sm':
            return "h-10 px-4 text-sm";
        case 'lg':
            return "h-20 px-12 text-2xl";
        case 'default':
        default:
            return "h-14 px-8 text-lg";
    }
});

const componentTag = computed(() => {
    if (props.href) return 'a';
    return props.as || 'button';
});
</script>

<template>
    <component :is="componentTag" :href="href" :class="[baseClasses, variantClasses, sizeClasses]">
        <slot />
    </component>
</template>
