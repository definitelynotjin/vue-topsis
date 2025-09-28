<script setup></script>

<template>
  <v-data-table hover class="data-table">
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
  </v-data-table>
</template>

<style lang="css" scoped>
  .data-table {
    background-color: steelblue;
    font-size: 16px;
  }
</style>
