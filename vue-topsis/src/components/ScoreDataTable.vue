<script setup lang="ts">
  import { defineEmits, defineProps } from 'vue'

  const props = defineProps<{
    items: any[]
    headers: any[]
  }>()

  const emit = defineEmits<{
    (e: 'delete-request', item: any): void
    (e: 'edit-value', scoreId: number | null, updated: { value?: number }): void
  }>()

  const onUpdateValue = (value: any, item: any) => {
    emit('edit-value', item.score_id ?? null, {
      value: Number(value),
      alternative_id: item.alt_id,
    })
  }
</script>

<template>
  <v-data-table :items="props.items" :headers="props.headers" hover class="score-data-table">
    <template v-slot:item.no="{ index }">
      {{ index + 1 }}
    </template>
    <template v-slot:item.value="{ item }">
      <VInlineTextField
        v-model="item.value"
        save-icon-color="cyan"
        name="value"
        :cell="true"
        @update="onUpdateValue($event, item)"
        :table-field="true"
      >
      </VInlineTextField>
    </template>

    <template v-slot:item.actions="{ item }">
      <div class="">
        <v-btn variant="plain" icon @click="emit('delete-request', item)">
          <v-icon color="red">mdi-delete</v-icon>
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
