<template>
  <svg xmlns="http://www.w3.org/2000/svg" :width="size" :height="size" viewBox="0 0 129.601 133">
    <path id="Icon_awesome-arrow-up" data-name="Icon awesome-arrow-up" d="M9.08,78.7l-6.59-6.59a7.1,7.1,0,0,1,0-10.063L60.166,4.339a7.1,7.1,0,0,1,10.063,0l57.676,57.676a7.1,7.1,0,0,1,0,10.063l-6.59,6.59a7.132,7.132,0,0,1-10.182-.119L77.086,42.81v85.312a7.107,7.107,0,0,1-7.124,7.124h-9.5a7.107,7.107,0,0,1-7.124-7.124V42.81L19.262,78.579A7.081,7.081,0,0,1,9.08,78.7Z" transform="translate(-0.397 -2.246)" :fill="color"/>
  </svg>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"


@Component
export default class UpIcon extends Vue {
  @Prop({default: ()=>'#fff'}) color: string
  @Prop({default: ()=>30}) size: number
}
</script>

<style lang="scss" scoped>
</style>
