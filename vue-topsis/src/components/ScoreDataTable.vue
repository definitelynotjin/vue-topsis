<script setup></script>

<template>
  <v-data-table hover class="data-table">
    <template v-slot:item.value="{ item }">
      <VInlineTextField v-model="item.value" name="value" :cell="true" :table-field="true">
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
