<template>
  <b-container class="model-viewer">
    <P5 v-on="{preload, setup, draw}"/>
  </b-container>
</template>

<script lang="ts">
import {
  Component,
  Prop,
  Vue,
} from "nuxt-property-decorator"
//@ts-ignore
import P5, {P5Sketch, P5Geometry} from "vue-p5-component";
import {getAsset} from "~/helpers/assetHelper";

@Component({
  components: {
    P5
  }
})
export default class ModelViewer extends Vue {
  model!: P5Geometry

  preload(sketch: P5Sketch) {
    this.model = sketch.loadModel('/ocean.obj');
  }

  setup(sketch: P5Sketch) {
    const element:HTMLElement = document.getElementsByClassName('model-viewer')[0];

    sketch.createCanvas(element.offsetWidth, element.offsetHeight, sketch.WEBGL);
  }

  draw(sketch: P5Sketch) {
    sketch.background(255);
    sketch.rotateX(sketch.frameCount * 0.01);
    sketch.rotateY(sketch.frameCount * 0.01);
    sketch.model(this.model);
  }
}
</script>

<style lang="scss" scoped>
.model-viewer {
  background-color: white;
  padding: 0;
  height: 70vh;
  width: 100%;
  border-radius: 4px;
  margin-bottom: 10%;
  @include media-breakpoint-up(md) {
    margin-bottom: initial;
    height: 95%;
  }
}

</style>
