<script setup lang="ts">
  import { X } from 'lucide-vue-next'
  import { defineEmits } from 'vue'

  const emit = defineEmits<{
    (e: 'delete-request', item: any): void
    (
      e: 'edit-alternative',
      alternative_id: number,
      updated: { name?: string; id_alt?: string },
    ): void
  }>()
</script>

<template>
  <v-data-table hover class="alternative-data-table">
    <template v-slot:item.no="{ index }">
      {{ index + 1 }}
    </template>
    <template v-slot:item.name="{ item }">
      <VInlineTextField
        v-model="item.name"
        save-icon-color="cyan"
        name="name"
        @update="(value) => emit('edit-alternative', Number(item.id), { name: value })"
        :cell="true"
        :table-field="true"
      >
      </VInlineTextField>
    </template>

    <template v-slot:item.id_alt="{ item }">
      <VInlineTextField
        v-model="item.id_alt"
        save-icon-color="cyan"
        @update="(value) => emit('edit-alternative', Number(item.id), { id_alt: value })"
        name="id_alt"
        :cell="true"
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
