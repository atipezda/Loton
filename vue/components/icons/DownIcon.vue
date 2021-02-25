<template>
  <svg xmlns="http://www.w3.org/2000/svg" :width="size" :height="size" viewBox="0 0 129.601 133">
      <path id="Icon_awesome-arrow-down" data-name="Icon awesome-arrow-down" d="M121.345,58.8l6.59,6.59a7.1,7.1,0,0,1,0,10.063L70.259,133.157a7.1,7.1,0,0,1-10.063,0L2.49,75.451a7.1,7.1,0,0,1,0-10.063L9.08,58.8a7.132,7.132,0,0,1,10.182.119L53.339,94.687V9.374A7.107,7.107,0,0,1,60.463,2.25h9.5a7.107,7.107,0,0,1,7.124,7.124V94.687l34.077-35.769a7.081,7.081,0,0,1,10.182-.119Z" transform="translate(-0.397 -2.25)" :fill="color"/>
  </svg>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"


@Component
export default class DownIcon extends Vue {
  @Prop({default: ()=>'#fff'}) color: string
  @Prop({default: ()=>30}) size: number
}
</script>

<style lang="scss" scoped>
</style>
