<script setup lang="ts">
  import { defineEmits } from 'vue'

  const typeItems = [
    {
      title: 'Benefit',
      value: 'benefit',
    },

    {
      title: 'Cost',
      value: 'cost',
    },
  ]

  const emit = defineEmits<{
    (e: 'delete-request', item: any): void
    (
      e: 'edit-criteria',
      criteriaId: number,
      updated: { name?: string; type?: string; weight?: string },
    ): void
  }>()
</script>

<template>
  <v-data-table hover class="criteria-data-table">
    <template v-slot:item.no="{ index }">
      {{ index + 1 }}
    </template>
    <template v-slot:item.name="{ item }">
      <VInlineTextField
        save-icon-color="cyan"
        v-model="item.name"
        @update="(value) => emit('edit-criteria', Number(item.id), { name: value })"
        name="name"
        :cell="true"
        :table-field="true"
      >
      </VInlineTextField>
    </template>

    <template v-slot:item.type="{ item }">
      <VInlineSelect
        v-model="item.type"
        save-icon-color="cyan"
        :list-props="{ bgColor: 'cyan-darken-1' }"
        :items="typeItems"
        @update="(value) => emit('edit-criteria', Number(item.id), { type: value })"
        name="type"
        :cell="true"
        :table-field="true"
      >
      </VInlineSelect>
    </template>

    <template v-slot:item.weight="{ item }">
      <VInlineTextField
        v-model="item.weight"
        @update="(value) => emit('edit-criteria', Number(item.id), { weight: value })"
        name="weight"
        :cell="true"
        save-icon-color="green"
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
