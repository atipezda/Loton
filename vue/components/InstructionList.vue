<template>
  <div class="instruction-list">
    <ModalInput ref="modalInput" @submit="(val) => addElement(Number(val))" title="odczekaj sekund:" type="number"/>
    <draggable v-model="list" draggable=".instruction-element">
      <template v-for="element in list">
        <InstructionWait :name="element.id" :id="element.id" v-if="element && element.type === 'wait'" :key="element.id" :val="element.value" @delete="deleteElement"/>
        <InstructionMove :name="element.id" :id="element.id" v-else :key="element.id" :val="element.value" @delete="deleteElement"/>
      </template>
    </draggable>
    <hr v-if="list.length"/>
    <InstructionManager
      @waitAdd="launchModal('wait')"
      @moveAdd="launchModal('move')"
    />
  </div>
</template>

<script lang="ts">
import {Component, Prop, Ref, Vue, Watch} from "nuxt-property-decorator"
import draggable from 'vuedraggable'
import InstructionElement from '~/components/InstructionElement.vue'
import InstructionWait from "~/components/InstructionWait.vue";
import InstructionMove from "~/components/InstructionMove.vue";
import InstructionManager from "~/components/InstructionManager.vue";
import {ArmInformatorInterface} from "~/components/ArmInformator.vue";
import ModalInput from "~/components/ModalInput.vue";
import Modal from "~/components/Modal.vue";
import {StateObjectInterface} from "~/store";

export interface InstructionListElement {
  id: number,
  type: 'wait' | 'move',
  value?: number | ArmInformatorInterface
}

@Component({
  components: {
    Modal,
    ModalInput,
    InstructionManager,
    InstructionMove,
    InstructionWait,
    draggable,
    InstructionElement
  },
})
export default class InstructionList extends Vue {
  @Prop() preloadedList!: InstructionListElement[]

  @Ref() modalInput!: ModalInput

  public list: InstructionListElement[] = []
  lastElementInsertedType!: InstructionListElement['type']
  //
  // get elementList(): InstructionListElement[] {
  //   return this.list.map((element: InstructionListElement)=>{
  //
  //     return {
  //        type: element.type,
  //         id: element.id,
  //       value: extendedValues
  //
  //     }
  //   })
  // }
  //
  @Watch('preloadedList', { immediate: true, deep: true })
  onPropertyChanged(list: InstructionListElement[]) {
    this.list = list
  }
  //
  // @Watch('list', { immediate: true, deep: true })
  // onPropertyChangedList(list: InstructionListElement[]) {
  //   this.list = list
  //   this.$emit('update', list)
  //   console.log(list)
  // }

  mounted(): void {
    this.list = this.preloadedList
  }

  getHighestListId(): number {
    let highestId = 0;
    this.list.forEach((elem: InstructionListElement) => {
      if (elem.id > highestId) {
        highestId = elem.id
      }
    })
    return highestId
  }

  addElement(value: number | ArmInformatorInterface): void {
    const highestId = this.getHighestListId() + 1
    this.list.push({
      id: highestId,
      type: this.lastElementInsertedType,
      value
    })
    this.$emit('update', this.list)
  }

  launchModal(type: InstructionListElement['type']): void {
    this.lastElementInsertedType = type
    if (type === 'move') {
      const {positions} = this.$store.state
      const preparedPositions = positions.map((position: ArmInformatorInterface) => (
        {
          id: position.id,
          angle: position.angle,
          percent: position.percent,
          name: position.name
        }
      ))
      this.addElement(preparedPositions)
    } else {
      this.modalInput.show();
    }
  }

  deleteElement(id: number): void {
    console.log(id);
    this.list = this.list.filter((element: InstructionListElement) => element.id !== id)
    this.$emit('update', this.list)
  }

}
</script>

<style lang="scss" scoped>
.instruction-list {
  .instruction-element {
    margin: 2% 5%;
  }

  .instruction-manager {
    margin: 2% 5%;
    //@include media-breakpoint-up('lg'){
    //  position: fixed;
    //  right: 0;
    //  top: 35%;
    //  height: 20vh;
    //  width: 10vw;
    //  z-index: 10;
    //}
  }

}
</style>
