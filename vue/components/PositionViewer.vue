<template>
  <div class="position-viewer" :class="{reverted: reverted}">
    <WrenchIcon size="25" class="icon"/>
    <template v-if="!switchable">
      <p>{{value}}&#176;</p>
    </template>
    <template v-else>
      <b-form-checkbox v-model="isOn" class="check-button" switch/>
    </template>
    <PositionBG/>
  </div>
</template>

<script lang="ts">
import {Component,Vue, Prop} from "nuxt-property-decorator"
import PositionBG from "~/components/icons/PositionBG.vue";
import WrenchIcon from "~/components/icons/WrenchIcon.vue";
@Component({
  components: {WrenchIcon, PositionBG}
})
export default class PositionViewer extends Vue {
  @Prop({default: ()=>false})reverted!:boolean
  @Prop({default: ()=>false})switchable!:boolean
  @Prop({default: ()=>0})value!:number

  isOn: boolean = false

  mounted():void{
    if(this.switchable){
      this.isOn = Boolean(this.value)
    }
  }

}
</script>

<style lang="scss" scoped>
.position-viewer{
  position: relative;
  p{
    top: 30%;
    right: 15%;
    position: absolute;
  }
  .icon{
    position: absolute;
    top:30%;
    left: 20%;
  }
  .check-button{
    position: absolute;
    top: 30%;
    right: 10%;
  }
}
.position-viewer.reverted{
  transform: scaleX(-1);
  transform-origin: center;
  transform-box: fill-box;
  p{
    transform: scaleX(-1);
  }
  .check-button{
    transform: scaleX(-1);
    right: 15%;
  }
}
</style>
