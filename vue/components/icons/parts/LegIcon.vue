<template>
  <svg xmlns="http://www.w3.org/2000/svg" :width="size" :height="size" viewBox="0 0 200 200">
      <g :fill="color" id="Group_1353" data-name="Group 1353" transform="translate(-50.569 -37.92)">
        <path id="Subtraction_3" data-name="Subtraction 3" d="M17.783,140.169h0a16.377,16.377,0,0,1-5.538-.908,14.181,14.181,0,0,1-4.931-3.034c-8.294-6.865-9.7-17.837-3.352-26.091C7.889,106.387,100.285,18.229,111.406,7.79a30.067,30.067,0,0,1,5.221-3.895A29.436,29.436,0,0,1,122.4,1.217,22.8,22.8,0,0,1,129.606,0a20.917,20.917,0,0,1,10.946,3.156C144.461,5.523,146.7,8.5,147.2,12a12.868,12.868,0,0,1-.57,5.691,22.018,22.018,0,0,1-2.336,4.955,29.474,29.474,0,0,1-3.739,4.826L44.2,128.271a36.09,36.09,0,0,1-7.737,5.877C29.039,138.2,22.928,140.169,17.783,140.169Zm-.7-24.557c-3.855,0-6.991,2.695-6.991,6.007s3.136,6.007,6.991,6.007,6.991-2.695,6.991-6.007S20.938,115.612,17.083,115.612Z" transform="translate(103.764 38.42)" stroke="#000" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"/>
        <path id="Path_369" data-name="Path 369" d="M11.054,36.319h184.9v10.29l-184.9-1.945Z" transform="translate(40.015 159.822)" stroke="#000" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"/>
        <path id="Path_370" data-name="Path 370" d="M16.648,37.589V63.6H149.809V37.589" transform="translate(62.063 163.696)" stroke="#000" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"/>
        <path id="Path_371" data-name="Path 371" d="M13.285,40.164H163.737V51.289L13.323,49.62Z" transform="translate(55.861 187.131)" stroke="#000" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"/>
        <line id="Line_1" data-name="Line 1" x1="24.308" y1="64.821" transform="translate(78.991 146.609)" fill="none" stroke="#000" stroke-linecap="round" stroke-width="19"/>
        <path id="Path_373" data-name="Path 373" d="M34.225,93.8-.333.422" transform="translate(150.235 118.989)" stroke="#000" stroke-linecap="round" stroke-width="19"/>
        <path id="Path_372" data-name="Path 372" d="M.208,26.725C-1.652,16.107-2,7.192,25.079-7.126s48.282,14.972,53.493,23.8" transform="translate(78.156 119.811)" fill="none" stroke="#000" stroke-linecap="round" stroke-linejoin="round" stroke-width="19"/>
      </g>
  </svg>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"


@Component
export default class LegIcon extends Vue {
  @Prop({default: ()=>'#000000'}) color!: string
  @Prop({default: ()=>30}) size!: number
}
</script>
