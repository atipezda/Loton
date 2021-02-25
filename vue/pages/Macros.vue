<template>
  <b-row class="index-main">
    <b-col lg="7">
      <InstructionList/>
    </b-col>
    <b-col class="card-list" lg="5">

    </b-col>
  </b-row>
</template>

<script lang="ts">
import {Component, Vue} from "nuxt-property-decorator"
import InstructionList from "~/components/InstructionList.vue";


@Component({components: {InstructionList}})
export default class Macros extends Vue {
}
</script>

<style lang="scss" scoped>
</style>
