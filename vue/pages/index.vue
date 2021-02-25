<template>
    <b-row class="index-main">
      <b-col lg="7">
        <ModelViewer/>
      </b-col>
      <b-col class="card-list" lg="5">
        <b-container>
          <IconCard v-for="card in cards" v-bind="card"/>
        </b-container>
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


@Component({
  components: {
    ArmInformator,
    ModelViewer,
    IconCard
  }
})
export default class Index extends Vue {
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
.index-main{
  height: 90%;
}


.main-row {

}

//.card-list{
//  margin-right: 5px;
//}

</style>
