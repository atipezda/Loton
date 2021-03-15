<template>
  <b-card class="macro-element">
    <b-card-title>
      <h3>{{name}}</h3>
    </b-card-title>
    <b-card-body>
      <p>czas trwania: <span>{{time}}s</span></p>
      <p>insturkcji: <span>{{length}}</span></p>
    </b-card-body>
    <slot/>
  </b-card>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"


@Component
export default class MacroElement extends Vue {
  @Prop() name!: string
  @Prop() length!: string
  @Prop() time!: string
  @Prop() id!: number
}
</script>

<style lang="scss" scoped>
.macro-element{
  margin: 3%;
}
</style>
