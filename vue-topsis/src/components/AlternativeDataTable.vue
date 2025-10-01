<script setup lang="ts">
  import { X } from 'lucide-vue-next'
  import { defineEmits } from 'vue'

  const emit = defineEmits<{
    (e: 'delete-request', item: any): void
  }>()
</script>

<template>
  <v-data-table hover class="alternative-data-table">
    <template v-slot:item.no="{ index }">
      {{ index + 1 }}
    </template>
    <template v-slot:item.name="{ item }">
      <VInlineTextField v-model="item.name" name="name" :cell="true" :table-field="true">
      </VInlineTextField>
    </template>

    <template v-slot:item.id_alt="{ item }">
      <VInlineTextField v-model="item.id_alt" name="id_alt" :cell="true" :table-field="true">
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
  .alternative-data-table {
    background-color: steelblue;
    font-size: 16px;
  }

  .alternative-data-table:deep(.v-data-table__tr) .hover-delete {
    visibility: hidden;
  }
  .alternative-data-table:deep(.v-data-table__tr:hover) .hover-delete {
    visibility: visible;
    color: red;
  }
</style>
