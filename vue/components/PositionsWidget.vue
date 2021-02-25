<template>
  <div class="positions-widget">
    <ArmInformator v-for="pos in positions" v-bind="pos"/>
  </div>
</template>

<script lang="ts">
import {Component,Vue} from "nuxt-property-decorator"
import ArmInformator, {ArmInformatorInterface} from "~/components/ArmInformator.vue";

@Component({
  components: {
    ArmInformator
  }
})
export default class PositionsWidget extends Vue {
  get positions(){
    const pos = this.$store.state.positions
    return pos
  }
}
</script>

<style lang="scss" scoped>
.positions-widget{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}
</style>
