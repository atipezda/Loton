<template>
  <svg v-if="closed" :fill="color" :width="fixedSize" :height="fixedSize" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 133 106.401">
    <path id="Icon_awesome-eye-slash" data-name="Icon awesome-eye-slash" d="M66.5,83.125A29.813,29.813,0,0,1,36.8,55.463L15,38.616A69.262,69.262,0,0,0,7.373,50.168a6.723,6.723,0,0,0,0,6.066C18.643,78.223,40.953,93.1,66.5,93.1a64.551,64.551,0,0,0,16.186-2.174L71.9,82.583A29.952,29.952,0,0,1,66.5,83.125ZM131.715,95.2,108.741,77.443a68.837,68.837,0,0,0,16.885-21.211,6.723,6.723,0,0,0,0-6.066C114.356,28.178,92.046,13.3,66.5,13.3a64.037,64.037,0,0,0-30.615,7.834L9.447.7a3.325,3.325,0,0,0-4.667.584L.7,6.536A3.325,3.325,0,0,0,1.284,11.2l122.268,94.5a3.325,3.325,0,0,0,4.667-.584l4.081-5.251a3.325,3.325,0,0,0-.586-4.665ZM93.536,65.69l-8.167-6.313A19.691,19.691,0,0,0,61.24,34.038,9.9,9.9,0,0,1,63.174,39.9a9.692,9.692,0,0,1-.32,2.078l-15.3-11.822A29.574,29.574,0,0,1,66.5,23.275,29.908,29.908,0,0,1,96.424,53.2a29.215,29.215,0,0,1-2.889,12.492Z" transform="translate(0 0)"/>
  </svg>

  <svg v-else :fill="color" :width="fixedSize" :height="fixedSize" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 133 88.667">
    <path id="Icon_awesome-eye" data-name="Icon awesome-eye" d="M132.2,45.462C119.675,21.03,94.885,4.5,66.5,4.5S13.318,21.042.8,45.465a7.47,7.47,0,0,0,0,6.74C13.325,76.636,38.115,93.167,66.5,93.167S119.682,76.625,132.2,52.2A7.47,7.47,0,0,0,132.2,45.462ZM66.5,82.083a33.25,33.25,0,1,1,33.25-33.25A33.25,33.25,0,0,1,66.5,82.083Zm0-55.417a22.007,22.007,0,0,0-5.844.875A11.049,11.049,0,0,1,45.208,42.989,22.116,22.116,0,1,0,66.5,26.667Z" transform="translate(0 -4.5)"/>
  </svg>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"


@Component
export default class EyeIcon extends Vue {
  @Prop({default: () => '#FFF'}) color!: string
  @Prop({default: () => 30}) size!: number
  @Prop({default: () => false}) closed!: boolean


  get fixedSize() {
    return this.closed ? this.size : this.size
  }
}
</script>

<style lang="scss" scoped>
</style>
