<template>
  <div class="armInformator">
    <GaugeGraph :value="percent"/>
    <h1 class="text">{{ value }}<i>{{ symbol }}</i></h1>
    <div class="extra-dot">
      <Component v-if="iconComponentPath" :is="iconComponent"/>
    </div>
  </div>
</template>

<script lang="ts">
//@ts-ignore
import {VueSvgGauge} from "vue-svg-gauge"
import {defineAsyncComponent} from "vue";
import {
  Component,
  Prop,
  Vue,
} from "nuxt-property-decorator"
//@ts-ignore
import {Gauge} from 'gaugeJS'
import {getAsset} from "~/helpers/assetHelper";
import GaugeGraph from "~/components/GaugeGraph.vue";
import FeetIcon from "~/components/icons/parts/FeetIcon.vue";

export interface ArmInformatorInterface {
  id: number;
  percent: number;
  angle: number;
  maxAngle: number;
  name: string;
  iconComponentPath: string;
  isSwitch?: boolean
}

@Component({
  components: {
    GaugeGraph
  }
})
export default class ArmInformator extends Vue {
  @Prop({default: () => 0}) readonly angle!: number
  @Prop({default: () => 0}) readonly percent!: number
  @Prop({default: () => 0}) readonly mode!: 'angle' | 'percent'
  @Prop() readonly iconComponentPath!: string

  get value(): string {
    return this.mode === 'angle' ? `${this.angle}` : `${this.percent}`
  }

  get symbol(): string {
    return this.mode === 'angle' ? '°' : '%'
  }

  get iconComponent(){
    return () => import(`@/components/${this.iconComponentPath}`)
  }

  // mounted(): void {
  //   this.socket = this.$nuxtSocket({
  //     name: 'main',
  //     channel: '/positions'
  //   })
  //   this.socket
  //     .on('move', (servo: ServoInfo) => {
  //       this.$store.commit('updatePosition', {name: servo.name, value: servo.value})
  //     })
  // }


}
</script>

<style lang="scss" scoped>
.armInformator {
  position: relative;
  background-color: white;
  width: 150px;
  height: 150px;
  font-size: 25px;
  margin: 25px 5%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 5px;

  @include media-breakpoint-up(lg) {
    height: 130px;
    width: 130px;
  }
  @include media-breakpoint-up(xl) {
    height: 160px;
    width: 160px;
  }

  .extra-dot {
    position: absolute;
    bottom: 0;
    background-color: white;
    height: 70px;
    width: 70px;
    border-radius: 50%;
    transform: translateY(50%);
    display: flex;
    justify-content: center;
    align-items: center;

    img {
      width: 70%;
      border-radius: 30%;
    }
  }


  .text {
    position: absolute;
    bottom: 15%;
    z-index: 2;
    color: $primary;
    font-weight: 300;
    font-size: 1em;

    i {
      font-size: 0.7em;
    }
  }

}

</style>
