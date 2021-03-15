<template>
  <svg xmlns="http://www.w3.org/2000/svg" :width="size" :height="size" viewBox="0 0 200 200">
      <g :fill="color" id="Group_1350" data-name="Group 1350" transform="translate(0.05 0.05)">
        <path id="Path_363" data-name="Path 363" d="M88.558,204.15h41.969V150.525h5.05l28.161-22.748,2-1,2.711-1.693,3-3.213L208.58,72.183l.873-1.693V68.462l-.873-2.872-2.7-5.663-24.757-53-1.17-1.752h-12.96V18.526a60.015,60.015,0,0,1,0,44.788v8.448L143.3,103.028l-17.02,8.7-1.157-.763H93.491l-1.238,1.184-16.829-9.13L51.039,71.172V60.863a54.385,54.385,0,0,1,0-42.338c-.1-13.775,0-14.365,0-14.365H39.626a25.787,25.787,0,0,0-6.288,11.152c-3.287,8.875-23.884,51.97-23.884,51.97V71.61l40.422,53.576q3.046,1.511,5.9,3.294c0,.254,27.27,22.056,27.27,22.056h5.515s.142,40.217,0,53.625" transform="translate(-9.453 -4.161)" stroke="#707070" stroke-width="0.1"/>
        <path id="Path_364" data-name="Path 364" d="M17.52,41.141" transform="translate(162.984 -17.148)" fill="none" stroke="#707070" stroke-width="1"/>
      </g>
  </svg>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"


@Component
export default class FingerIcon extends Vue {
  @Prop({default: ()=>'#000000'}) color!: string
  @Prop({default: ()=>30}) size!: number
}
</script>
