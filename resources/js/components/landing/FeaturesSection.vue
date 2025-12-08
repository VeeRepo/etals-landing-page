<script setup lang="ts">
const features = [
    {
        title: 'Data Harmonization',
        description: 'Etals harmonizes data from across tools and channels to surface real-time, contextual insights your team can actually use.',
        tags: ['Integration', 'Real-time']
    },
    {
        title: 'Data Enrichment',
        description: 'Automatically enrich your product data with external sources to improve searchability and relevance.',
        tags: ['AI', 'Automation']
    },
    {
        title: 'Localization',
        description: 'Scale product content across markets, fast. From microcopy to full catalogs, Etals creates SEO-optimized copy.',
        tags: ['Global', 'Translation']
    },
    {
        title: 'Cross-system Integration',
        description: 'From opportunity to outcome - fast. Agentic turns insight into execution by planning and completing tasks across your stack.',
        tags: ['Workflow', 'Agents']
    }
];
</script>

<template>
    <section id="features" class="py-32 bg-muted/10">
        <div class="container mx-auto px-4">
            <div class="mb-20">
                <h2 class="text-[clamp(2.5rem,6vw,6rem)] font-bold uppercase tracking-tighter leading-none mb-8">
                    Features
                </h2>
                <div class="h-1 w-full bg-border"></div>
            </div>

            <div class="flex flex-col gap-32">
                <div v-for="(feature, index) in features" :key="index" 
                    class="sticky top-32 min-h-[50vh] border-2 border-border bg-background p-8 md:p-16 flex flex-col md:flex-row gap-12 items-start shadow-2xl">
                    
                    <div class="w-full md:w-1/2">
                        <div class="text-accent font-mono text-xl mb-4">0{{ index + 1 }}</div>
                        <h3 class="text-4xl md:text-6xl font-bold uppercase tracking-tighter mb-8 text-balance">
                            {{ feature.title }}
                        </h3>
                        <div class="flex flex-wrap gap-2">
                            <span v-for="tag in feature.tags" :key="tag" class="px-3 py-1 border border-border text-xs uppercase tracking-widest">
                                {{ tag }}
                            </span>
                        </div>
                    </div>

                    <div class="w-full md:w-1/2 pt-4">
                        <p class="text-xl md:text-2xl text-muted-foreground leading-relaxed">
                            {{ feature.description }}
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
