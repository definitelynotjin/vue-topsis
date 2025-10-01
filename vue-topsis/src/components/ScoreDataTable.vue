<script setup lang="ts">
  import { addScoreData, editScoreData } from '../services/api.ts'
  import { X } from 'lucide-vue-next'
  import { defineEmits } from 'vue'

  const emit = defineEmits<{
    (e: 'delete-request', item: any): void
  }>()

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
  <v-data-table hover class="score-data-table">
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

    <template v-slot:item.actions="{ item }">
      <div class="hover-delete">
        <v-btn variant="plain" icon @click="emit('delete-request', item)">
          <X :size="20" />
        </v-btn>
      </div>
    </template>
  </v-data-table>
</template>

<style lang="css" scoped>
  .score-data-table {
    background-color: steelblue;
    font-size: 16px;
  }

  .score-data-table:deep(.v-data-table__tr) .hover-delete {
    visibility: hidden;
  }
  .score-data-table:deep(.v-data-table__tr:hover) .hover-delete {
    visibility: visible;
    color: red;
  }
</style>
