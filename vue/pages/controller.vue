<template>
  <b-row class="controller-main">
    <b-col lg="7">
      <RemoteController/>
    </b-col>
  </b-row>
</template>

<script lang="ts">
import {
  Component,
  Prop,
  Vue,
} from "nuxt-property-decorator"
import IconCard, {IconCardInterface} from "~/components/IconCard.vue";
import {ArmInformatorInterface} from "~/components/ArmInformator.vue";
import ArmInformator from "~/components/ArmInformator.vue";
import {io} from 'socket.io-client';
import ModelViewer from "~/components/ModelViewer.vue";
import RemoteController from "~/components/RemoteController.vue";


@Component({
  components: {
    RemoteController,
    ArmInformator,
    ModelViewer,
    IconCard
  }
})
export default class Controller extends Vue {
  cards: IconCardInterface[] = [
    {
      buttonText: 'Macro',
      text: 'Nagraj i odtwarzaj ruchy robota',
      iconName: 'arm.jpg',
      title: 'Macros',
      href: 'macros'
    },
    {
      buttonText: 'zarządzaj',
      text: 'zmień ustawienia robota',
      iconName: 'arm.jpg',
      title: 'Ustawienia'
    }
  ]
}
</script>

<style lang="scss">
.controller-main{
  width: 90%;
  margin: 0 auto;
}

</style>
