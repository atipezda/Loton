<template>
  <InstructionElement>
    <template v-slot:title>
      <MoveIcon/>
    </template>
    <template v-slot:body>
      <div class="positions">
        <PositionViewer v-for="position in positions" :value="position.value" :reverted="isOdd(position.id)" :switchable="position.isSwitch"/>
      </div>
    </template>
  </InstructionElement>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"
import MoveIcon from "~/components/icons/MoveIcon.vue";
import InstructionElement from "~/components/InstructionElement.vue";
import PositionViewer from "~/components/PositionViewer.vue";
import {ArmInformatorInterface} from "~/components/ArmInformator.vue";

@Component({
  components: {PositionViewer, InstructionElement, MoveIcon, VueNumberInput}
})
export default class InstructionMove extends Vue {
  @Prop() val!: number | string

  get positions(): ArmInformatorInterface[]{
    return this.$store.state.positions
  }

  isOdd(num: number):boolean{
    return num%2===0
  }

}
</script>

<style lang="scss" scoped>
.positions {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  ::v-deep .position-viewer{
    margin: 0 5%;
  }
}
</style>
