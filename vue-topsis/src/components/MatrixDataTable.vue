<script setup>
  import { computed } from 'vue'

  const props = defineProps({
    items: { type: Array, required: true },
    headers: { type: Array, default: null }, // optional
  })

  // Jika tidak ada headers manual → buat otomatis dari key object pertama
  const autoHeaders = computed(() => {
    console.log('items', props.items)

    if (!props.items.length) return []
    const keys = Object.keys(props.items[0])
    const sortedKeys = [
      ...keys.filter((k) => k === 'id'),
      ...keys.filter((k) => k === 'nama'),
      ...keys.filter((k) => k !== 'id' && k !== 'nama'),
    ]
    return [
      { title: 'No', value: 'no' },
      sortedKeys.map((k) => ({
        title: k.toUpperCase(),
        key: k,
      })),
    ].flat()
  })

  // Pilih headers dari props atau hasil generate
  const tableHeaders = computed(() => props.headers || autoHeaders.value)
</script>

<template>
  <v-data-table class="data-table" :headers="tableHeaders" :items="props.items" hover>
    <template v-slot:item.no="{ index }">
      {{ index + 1 }}
    </template>
  </v-data-table>
</template>

<style lang="css" scoped>
  .data-table {
    background-color: steelblue;
    font-size: 16px;
    text-transform: initial;
  }
</style>
