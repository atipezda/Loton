<template>
  <div class="main">
    <header class="nav-header">
      <img src="@/assets/logo.png">
      <b-button class="logout" variant="danger">Wyloguj</b-button>
    </header>
    <div class="tilesWrapper">

      <b-row class="main-row">
        <b-col lg="4" class="statuses">
          <ArmInformator v-for="armInfo in armInformations" v-bind="armInfo"/>
        </b-col>
        <b-col lg="5">
          <ModelViewer/>

        </b-col>
        <b-col class="card-list" lg="3">
          <b-container>
            <IconCard v-for="card in cards" v-bind="cards"/>
          </b-container>
        </b-col>

      </b-row>
    </div>
  </div>
</template>

<script lang="ts">
import {
  Component,
  Prop,
  Vue,
} from "nuxt-property-decorator"
import {IconCardInterface} from "~/components/IconCard.vue";
import {ArmInformatorInterface} from "~/components/ArmInformator.vue";
import {log} from "three";

@Component
export default class Index extends Vue {
  cards: IconCardInterface[] = [
    {
      buttonText: 'zarządzaj',
      text: 'zmień ustawienia robota',
      iconName: 'arm.jpg',
      title: 'Ustawienia'
    },
    {
      buttonText: 'zarządzaj',
      text: 'zmień ustawienia robota',
      iconName: 'arm.jpg',
      title: 'Ustawienia'
    }
  ]
  armInformations: ArmInformatorInterface[] = [
    {
    iconName: 'arm.jpg',
    value: 20,
    },
    {
      iconName: 'arm.jpg',
      value: 80,
    },
    {
      iconName: 'arm.jpg',
      value: 10,
    },
    {
      iconName: 'arm.jpg',
      value: 50,
    },
    {
      iconName: 'arm.jpg',
      value: 22,
    },
    {
      iconName: 'arm.jpg',
      value: 0,
    },
  ]

  async mounted(): Promise<void>{
    const res = await this.$axios.get('/api/test');
    console.log(res.data);
  }
}
</script>

<style lang="scss">
.main {
  background: linear-gradient(to left, #ad2969 0%, #654ea3 100%);
  min-height: 100vh;
  width: 100vw;
  padding: 0 10px;
  margin: 0;

  .nav-header {
    display: flex;

    .logo {
      margin-left: auto;
      margin-right: 0;
    }

    .logout {
      display: none;
      height: 40px;
      margin: auto 0;
      @include media-breakpoint-up(md) {
        display: block;
      }
    }
  }

  .statuses {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
    padding: 0;
    margin-bottom: 10%;
  }

  .tilesWrapper {
    padding: 0 0;
  }

  .main-row {

  }

  //.card-list{
  //  margin-right: 5px;
  //}
}
</style>
