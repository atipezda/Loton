<template>
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" :width="width" :height="height" viewBox="0 0 114.999 75.001">
    <defs>
      <filter id="Union_3" x="0" y="0" width="114.999" height="75.001" filterUnits="userSpaceOnUse">
        <feOffset dy="3" input="SourceAlpha"/>
        <feGaussianBlur stdDeviation="3" result="blur"/>
        <feFlood flood-opacity="0.467"/>
        <feComposite operator="in" in2="blur"/>
        <feComposite in="SourceGraphic"/>
      </filter>
    </defs>
    <g transform="matrix(1, 0, 0, 1, 0, 0)" filter="url(#Union_3)">
      <path id="Union_3-2" data-name="Union 3" d="M-6,22.5A28.5,28.5,0,0,1,48.119,10H82a9,9,0,0,1,9,9v8a9,9,0,0,1-9,9H47.607A28.5,28.5,0,0,1-6,22.5Z" transform="translate(15 12)" :fill="color"/>
    </g>
  </svg>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"


@Component
export default class PositionBG extends Vue {
  @Prop({default: ()=>'#fff'}) color!: string
  @Prop({default: ()=>75}) height!: number
  @Prop({default: ()=>115}) width!: number
}
</script>

<style lang="scss" scoped>
</style>
