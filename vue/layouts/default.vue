<template>
  <div class="main">
    <Header/>
    <div class="tilesWrapper">
      <b-row class="main-row">
        <b-col lg="4" class="statuses">
          <PositionsWidget/>
        </b-col>
        <b-col>
          <Nuxt/>
        </b-col>
      </b-row>
    </div>
  </div>

</template>

<script lang="ts">

import {Component, Vue} from "nuxt-property-decorator";
import ArmInformator, {ArmInformatorInterface} from "~/components/ArmInformator.vue";
import Header from '~/components/Header.vue'
import PositionsWidget from '~/components/PositionsWidget.vue'
import {Socket} from "socket.io";

@Component({
  components: {
    ArmInformator,
    PositionsWidget,
    Header
  }
})
export default class Default extends Vue {


}
</script>

<style lang="scss">
html {
  font-family: 'Source Sans Pro',
  -apple-system,
  BlinkMacSystemFont,
  'Segoe UI',
  Roboto,
  'Helvetica Neue',
  Arial,
  sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

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

.main {
  background: linear-gradient(to left, #ad2969 0%, #654ea3 100%);
  min-height: 100vh;
  width: 100vw;
  padding: 0 10px;
  margin: 0;
}

.statuses {
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-around;
  padding: 0;
  margin-bottom: 10%;
  display: none;
  @include media-breakpoint-up(sm){
    display: flex;
  }
}

.tilesWrapper {
  padding: 0 0;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}
</style>
