<template>
  <div class="armInformator">
    <GaugeGraph :value="value"/>
    <h1 class="text">{{ value }}<i>%</i></h1>
    <div class="extra-dot">
      <img :src="icon">
    </div>
  </div>
</template>

<script lang="ts">
//@ts-ignore
import {VueSvgGauge} from "vue-svg-gauge"
import {
  Component,
  Prop,
  Vue,
} from "nuxt-property-decorator"
//@ts-ignore
import {Gauge} from 'gaugeJS'
import {getAsset} from "~/helpers/assetHelper";

export interface ArmInformatorInterface {
  id: number;
  value: number;
  name: string;
  iconName: string;
  isSwitch?: boolean
}

@Component({
  components: {
    VueSvgGauge,
  }
})
export default class ArmInformator extends Vue {
  @Prop({default: () => 0}) readonly value!: number
  @Prop({default: () => ''}) readonly iconName!: string


  get icon(): string {
    return getAsset(this.iconName)
  }

  mounted(): void {
    this.socket = this.$nuxtSocket({
      name: 'main',
      channel: '/positions'
    })
    this.socket
      .on('move', (servo: ServoInfo) => {
        this.$store.commit('updatePosition', {name: servo.name, value: servo.value})
      })
  }


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
