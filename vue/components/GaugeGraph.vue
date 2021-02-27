<template>
  <canvas class="gauge" ref="gaugeCanvas"/>
</template>

<script lang="ts">
//@ts-ignore
import {VueSvgGauge} from "vue-svg-gauge"
import {
  Component,
  Prop,
  Vue,
  Watch
} from "nuxt-property-decorator"
//@ts-ignore
import {Gauge} from 'gaugeJS'

@Component({
  components: {
    VueSvgGauge,
  }
})
export default class GaugeGraph extends Vue {
  @Prop({default: () => 0}) readonly value!: number
  private gauge: Gauge

  mounted() {
    const target = this.$refs["gaugeCanvas"];
    this.gauge = new Gauge(target).setOptions(this.gaugeConfig);
    console.log(this.gauge)
    this.gauge.maxValue = 100; // set max gauge value
    this.gauge.setMinValue(0);  // set min value
    this.gauge.set(this.value);
  }

  @Watch('value')
  onValueChanged(newVal: number, oldVal: number): void {
    if (newVal === oldVal) return;
      this.gauge.set(newVal);
  }

  gaugeConfig = {
    "renderTicks": {
      "": null,
      "divisions": 9,
      "divLength": 1,
      "divColor": "#333333",
      "divWidth": 0.7,
      "subDivisions": 7,
      "subLength": 0.5,
      "subColor": "#666666",
      "subWidth": 0.1
    },
    "animationSpeed": 1,
    "angle": -0.15,
    "lineWidth": 0.09,
    "radiusScale": 0.8,
    "pointer": {
      "length": 0.61,
      "color": "",
      "strokeWidth": 0.033
    },
    "fontSize": 0,
    "colorStart": "#545AF9",
    "colorStop": "#545AF9",
    "strokeColor": "#EEEEEE",
    "": true,
    "generateGradient": true
  }

}
</script>

<style lang="scss" scoped>

.gauge {
  margin-bottom: 20%;
}

</style>
