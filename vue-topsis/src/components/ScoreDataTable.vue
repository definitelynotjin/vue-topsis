<script setup lang="ts">
  import { addScoreData, editScoreData } from '../services/api.ts'

  async function handleScoreUpdate(item: any) {
    try {
      if (!item.value || item.value === '') {
        return
      }

      if (item.score_id) {
        await editScoreData(item.score_id, Number(item.value))
      } else {
        const newScore = await addScoreData({
          value: Number(item.value),
          alternative_id: Number(item.alt_id),
          criteria_id: Number(item.criteria_id),
        })
        item.score_id = newScore.id
      }
    } catch (err) {
      console.error('Failed to save score:', err)
    }
  }
</script>

<template>
  <v-data-table hover class="data-table">
    <template v-slot:item.no="{ index }">
      {{ index + 1 }}
    </template>
    <template v-slot:item.value="{ item }">
      <VInlineTextField
        v-model="item.value"
        name="value"
        :cell="true"
        @update="handleScoreUpdate(item)"
        :table-field="true"
      >
      </VInlineTextField>
    </template>
  </v-data-table>
</template>

<style lang="css" scoped>
  .data-table {
    background-color: steelblue;
    font-size: 16px;
  }
</style>
