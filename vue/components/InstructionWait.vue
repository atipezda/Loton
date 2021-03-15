<template>
  <InstructionElement @delete="$emit('delete', id)">
    <template v-slot:title>
      <TimeIcon/>
      <p>{{val}}s</p>
    </template>
  </InstructionElement>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"
import MoveIcon from "~/components/icons/MoveIcon.vue";
import InstructionElement from "~/components/InstructionElement.vue";
import TimeIcon from "~/components/icons/TimeIcon.vue";
import VueNumberInput from '@chenfengyuan/vue-number-input';

@Component({
  components: {TimeIcon, InstructionElement, MoveIcon, VueNumberInput}
})
export default class InstructionWait extends Vue {
  @Prop() val: number | string
  @Prop() id: number

  currentValue: number = 0
}
</script>

<style lang="scss" scoped>
>>>.instruction-element-body{
  padding: 0;
}
</style>
