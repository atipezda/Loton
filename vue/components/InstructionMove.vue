<template>
  <InstructionElement @delete="$emit('delete', id)">
    <template v-slot:title>
      <MoveIcon/>
    </template>
    <template v-slot:body>
      <div class="positions">
        <template v-for="position in val">
          <div class="position-wrapper">
            <PositionViewer :value="position.percent" :reverted="isOdd(position.id)" :switchable="position.isSwitch"/>
          </div>
        </template>
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
  components: {PositionViewer, InstructionElement, MoveIcon}
})
export default class InstructionMove extends Vue {
  @Prop() val!: ArmInformatorInterface[]
  @Prop() id: number

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
    margin: auto;
    width: fit-content;
  }
  .position-wrapper{
    flex: 50%;
    position: relative;
  }
}
</style>
