<template>
  <b-modal
    id="modal-input"
    ref="btModal"
    @ok="$emit('submit')"
  >
    <slot/>
  </b-modal>
</template>

<script lang="ts">
import {Component,Vue, Ref} from "nuxt-property-decorator"
import {BModal} from "bootstrap-vue";


@Component
export default class ModalInput extends Vue {
  @Ref() readonly btModal!: BModal

  show():void{
    this.btModal.show()
  }
  hide():void{
    this.btModal.hide()
  }
}
</script>

<style lang="scss">
#modal-input{
  .modal-header{
    display: none !important;
  }
  label{
    font-weight: bold;
  }
}
</style>
