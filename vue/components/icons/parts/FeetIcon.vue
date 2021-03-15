<template>
  <svg xmlns="http://www.w3.org/2000/svg" :width="size" :height="size" :fill="color" viewBox="0 0 201 206.5">
    <g id="Group_1352" data-name="Group 1352" transform="translate(-10.554 -17.5)">
      <path id="Path_369" data-name="Path 369" d="M11.054,36.319h200v13.77l-200-2.6Z" transform="translate(0 129.561)" stroke="#000" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"/>
      <path id="Path_370" data-name="Path 370" d="M16.648,37.589v34.8H159.585v-34.8" transform="translate(23.468 136.219)" stroke="#000" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"/>
      <path id="Path_371" data-name="Path 371" d="M13.285,40.164h153.9V55.051L13.324,52.817Z" transform="translate(21.959 168.449)" stroke="#000" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"/>
      <path id="Path_372" data-name="Path 372" d="M0,140.952V0" transform="translate(56.124 23.5)" fill="none" stroke="#000" stroke-linecap="round" stroke-width="12"/>
      <line id="Line_2" data-name="Line 2" y1="140.952" transform="translate(163.708 23.5)" fill="none" stroke="#000" stroke-linecap="round" stroke-width="12"/>
    </g>
  </svg>

</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"


@Component
export default class FeetIcon extends Vue {
  @Prop({default: ()=>'#000000'}) color!: string
  @Prop({default: ()=>30}) size!: number
}
</script>
