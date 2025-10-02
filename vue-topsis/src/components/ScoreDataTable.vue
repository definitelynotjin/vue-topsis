<script setup lang="ts">
  import { X } from 'lucide-vue-next'
  import { defineEmits } from 'vue'

  const emit = defineEmits<{
    (e: 'delete-request', item: any): void
    (
      e: 'edit-value',
      scoreId: number,
      updated: { value?: number; alternative_id: number; criteria_id: number },
    ): void
  }>()
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
        @update="
          (value) =>
            emit('edit-value', Number(item.score_id), {
              value: value,
              alternative_id: item.alt_id,
              criteria_id: item.criteria_id,
            })
        "
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
