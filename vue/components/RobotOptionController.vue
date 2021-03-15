<template>
  <div class="option-controller">
    <p class="status">połączono</p>
    <DualStateToggle :class="{toggleHidden: !isVisible}" leftOption="2%" rightOption="2°" @toggle="toggleMode"/>
    <b-button @click="toggleVisible" :pressed="isVisible" variant="primary" class="arm-toggle">
      <EyeIcon :closed="!isVisible" />
    </b-button>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from "nuxt-property-decorator"
import DualStateToggle from "~/components/DualStateToggle.vue";
import EyeIcon from "~/components/icons/EyeIcon.vue";
import {StateObjectInterface} from "~/store";
@Component({
  components: {EyeIcon, DualStateToggle}
})
export default class RobotOptionController extends Vue {

  get isVisible(): boolean{
    return (this.$store.state as StateObjectInterface).isArmInformatorVisible
  }

  toggleVisible(): void{
    this.$store.commit('toggleArmInformator');
  }

  toggleMode(selected: 'left' | 'right') {
    const mode = selected === 'right' ? 'angle' : 'percent'
    this.$store.commit('changeViewMode', mode)
  }




}
</script>

<style lang="scss" scoped>
.option-controller {
  padding: 3%;
  margin: 0 auto;
  background-color: white;
  display: flex;
  flex-direction: row;
  //align-items: center;
  .status{
    margin: auto auto auto 0;
  }
  .arm-toggle{
    @include media-breakpoint-up('lg'){
      display: none;
    }
    margin: 0 2%;
  }
  .toggleHidden{
    pointer-events: none;
    opacity: 0;
  }
}

</style>
