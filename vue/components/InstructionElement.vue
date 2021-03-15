<template>
  <b-card class="instruction-element">
    <b-card-title>
      <slot name="title"/>
      <div class="instruction-buttons">
        <b-button variant="primary">
          <UpIcon size="15"/>
        </b-button>
        <b-button variant="primary">
          <DownIcon size="15"/>
        </b-button>
        <b-button variant="danger" @click="$emit('delete')">X</b-button>
      </div>
    </b-card-title>
    <b-card-body v-if="$slots.body" class="instruction-element-body">
      <slot name="body"/>
    </b-card-body>
  </b-card>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"
import MoveIcon from "~/components/icons/MoveIcon.vue";
import UpIcon from "~/components/icons/UpIcon.vue";
import DownIcon from "~/components/icons/DownIcon.vue";
@Component({
  components: {DownIcon, UpIcon, MoveIcon}
})
export default class InstructionElement extends Vue {
  @Prop({default: () => 'instruction'}) type: 'time' | 'instruction'
  @Prop() val!: number | string
}
</script>

<style lang="scss" scoped>
.instruction-element{
  display: flex;
  flex-direction: row;
  .card-body{
    padding: 2%;
    //display: flex;
    //flex-direction: row;
    //flex-wrap: wrap;
  }
  .card-title{
    width: auto;
    margin: auto auto;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 2%;
    p{
      margin: auto auto;
    }
  }
  .instruction-element-body{
    padding-top: 2%;
    display: flex;
    flex-direction: row;
    justify-content: start;
    p{
      margin-left: 2%;
      width: auto;
    }
  }
  .instruction-buttons{
    margin-left: auto;
    margin-right: 0;
  }
}
</style>
