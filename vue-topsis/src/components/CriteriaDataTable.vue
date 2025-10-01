<script setup lang="ts">
  import { X } from 'lucide-vue-next'
  import { defineEmits } from 'vue'

  const emit = defineEmits<{
    (e: 'delete-request', item: any): void
  }>()
</script>

<template>
  <v-data-table hover class="criteria-data-table">
    <template v-slot:item.no="{ index }">
      {{ index + 1 }}
    </template>
    <template v-slot:item.name="{ item }">
      <VInlineTextField v-model="item.name" name="name" :cell="true" :table-field="true">
      </VInlineTextField>
    </template>

    <template v-slot:item.type="{ item }">
      <VInlineSelect v-model="item.type" name="type" :cell="true" :table-field="true">
      </VInlineSelect>
    </template>

    <template v-slot:item.weight="{ item }">
      <VInlineTextField v-model="item.weight" name="weight" :cell="true" :table-field="true">
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
  .criteria-data-table {
    background-color: steelblue;
    font-size: 16px;
  }
  .criteria-data-table:deep(.v-data-table__tr) .hover-delete {
    visibility: hidden;
    transition: ease-in-out;
  }
  .criteria-data-table:deep(.v-data-table__tr:hover) .hover-delete {
    visibility: visible;
    transition: ease-in-out;
    color: red;
  }
</style>
