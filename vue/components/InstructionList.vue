<template>
  <draggable :v-model="list" group="people" @start="drag=true" @end="drag=false">
<!--    <InstructionElement v-for="element in list" :key="element.id" :type="element.type" :val="element.value"/>-->
    <template  v-for="element in list">
      <InstructionWait v-if="element.type === 'wait'" :key="element.id" :val="element.value"/>
      <InstructionMove v-if="element.type === 'wait'" :key="element.id" :val="element.value"/>
    </template>
  </draggable>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"
import draggable from 'vuedraggable'
import InstructionElement from '~/components/InstructionElement.vue'
import InstructionWait from "~/components/InstructionWait.vue";
import InstructionMove from "~/components/InstructionMove.vue";

@Component({
  components: {
    InstructionMove,
    InstructionWait,
    draggable,
    InstructionElement
  },
})
export default class InstructionList extends Vue {
  list = [
    {
      id: 0,
      type: "wait",
      value: 2
    },
    {
      id: 1,
      type: "move",
      value: 10
    }
  ]

}
</script>

<style lang="scss">
  .instruction-element{
    margin: 2% 5%;
  }
</style>
