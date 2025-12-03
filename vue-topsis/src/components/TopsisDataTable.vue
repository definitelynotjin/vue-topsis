<script setup>
  const props = defineProps({
    items: { type: Array, required: true },
    headers: { type: Array, required: true },
    skipped: { type: Number, default: 0 },
    total: { type: Number, default: 0 },
  })
</script>
<template>
  <v-data-table class="data-table" hover :items="props.items" :headers="props.headers">
    <template v-slot:item.no="{ index }">
      {{ index + 1 }}
    </template>

    <!-- kalau mau custom kolom nama -->
    <template v-slot:item.name="{ item }">
      <strong>{{ item.name }}</strong>
    </template>

    <!-- score -->
    <template v-slot:item.score="{ item }">
      {{ item.score.toFixed(3) }}
    </template>

    <!-- rank -->
    <template v-slot:item.rank="{ item }"> 🏆 {{ item.rank }} </template>
  </v-data-table>
</template>

<style lang="css" scoped>
  .data-table {
    background-color: steelblue;
    font-size: 16px;
  }
</style>
