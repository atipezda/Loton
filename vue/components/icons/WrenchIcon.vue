<template>
  <svg xmlns="http://www.w3.org/2000/svg" :width="size" :height="size" viewBox="0 0 110.414 110.414">
    <path id="Icon_awesome-wrench" fill="color" data-name="Icon awesome-wrench" d="M109.493,23.527a2.586,2.586,0,0,0-4.339-1.188L89.118,38.375,74.48,35.936,72.041,21.3,88.077,5.262A2.592,2.592,0,0,0,86.856.914a30.9,30.9,0,0,0-36.8,39.924L4.042,86.856a13.8,13.8,0,1,0,19.516,19.516L69.537,60.393a30.951,30.951,0,0,0,39.956-36.866ZM13.8,101.787a5.176,5.176,0,1,1,5.176-5.176A5.177,5.177,0,0,1,13.8,101.787Z" transform="translate(0 0)"/>
  </svg>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"


@Component
export default class WrenchIcon extends Vue {
  @Prop({default: ()=>'#000'}) color!: string
  @Prop({default: ()=>20}) size!: number
}
</script>

<style lang="scss" scoped>
</style>
