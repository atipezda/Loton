<template>
  <svg xmlns="http://www.w3.org/2000/svg" :width="size" :height="size" viewBox="0 0 133 133">
    <path :fill="color" id="Icon_ionic-ios-add-circle" data-name="Icon ionic-ios-add-circle" d="M69.875,3.375a66.5,66.5,0,1,0,66.5,66.5A66.49,66.49,0,0,0,69.875,3.375ZM98.809,74.99H74.99V98.809a5.115,5.115,0,0,1-10.231,0V74.99H40.941a5.115,5.115,0,1,1,0-10.231H64.76V40.941a5.115,5.115,0,1,1,10.231,0V64.76H98.809a5.115,5.115,0,1,1,0,10.231Z" transform="translate(-3.375 -3.375)"/>
  </svg>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"


@Component
export default class AddIcon extends Vue {
  @Prop({default: ()=>'#000000'}) color: string
  @Prop({default: ()=>30}) size: number
}
</script>

<style lang="scss" scoped>
</style>
