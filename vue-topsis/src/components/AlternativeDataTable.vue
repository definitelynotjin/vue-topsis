<script setup></script>

<template>
  <v-data-table hover class="data-table">
    <template v-slot:item.name="{ item }">
      <VInlineTextField v-model="item.name" name="name" :cell="true" :table-field="true">
      </VInlineTextField>
    </template>

    <template v-slot:item.id_alt="{ item }">
      <VInlineTextField v-model="item.id_alt" name="id_alt" :cell="true" :table-field="true">
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
