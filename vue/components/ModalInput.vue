<template>
  <Modal ref="modal" @submit="$emit('submit', inputVal)">
    <div class="form-group">
      <label for="val" class="col-form-label">{{title}}</label>
      <input type="text" class="form-control" id="val" v-model="inputVal" :type="type" :step="step">
    </div>
  </Modal>


</template>

<script lang="ts">
import {Component, Vue, Ref, Prop} from "nuxt-property-decorator"
import {BModal} from "bootstrap-vue";
import Modal from "~/components/Modal.vue";
@Component({
  components: {Modal}
})
export default class ModalInput extends Vue {
  inputVal: string = ''
  @Prop() title!: string
  @Prop({default: ()=>'test'}) type!: 'number' | 'text' | 'password'
  @Prop({default: ()=>1}) step!: number

  @Ref() readonly modal!: modal

  reset():void{
    this.inputVal = ''
  }

  show():void{
    this.reset()
    this.modal.show()
  }
}
</script>

<style lang="scss" scoped>
</style>
