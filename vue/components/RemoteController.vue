<template>
  <b-card>
    <b-card-body>
      <ControlSlider v-for="position in positions" v-bind="position"/>
    </b-card-body>
  </b-card>

</template>

<script lang="ts">
import {Component,Vue} from "nuxt-property-decorator"
import 'vue-slider-component/theme/antd.css'
import {ArmInformatorInterface} from "~/components/ArmInformator.vue";
import ControlSlider from "~/components/ControlSlider.vue";
@Component({
  components: {ControlSlider}
})
export default class RemoteController extends Vue {
  value: 10

  get positions(): ArmInformatorInterface[]{
    return this.$store.state.positions
  }
}
</script>

<style lang="scss" scoped>
</style>
