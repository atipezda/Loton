<template>
  <div class="main">
    <Header/>
    <div class="tilesWrapper">
      <b-row class="main-row">
        <b-col lg="4" class="statuses">
          <div class="option-controller-wrapper">
            <RobotOptionController/>
          </div>
          <b-collapse :visible="arePositionsVisible" id="collapse-statuses">
            <PositionsWidget/>
          </b-collapse>
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
import RobotOptionController from "~/components/RobotOptionController.vue";
import {StateObjectInterface} from "~/store";

@Component({
  components: {
    RobotOptionController,
    ArmInformator,
    PositionsWidget,
    Header
  }
})
export default class Default extends Vue {

  get arePositionsVisible(): boolean {
   return (this.$store.state as StateObjectInterface).isArmInformatorVisible
  }
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
    margin: 0 auto;
    @include media-breakpoint-up(md) {
      margin-left: 0;
      margin-right: auto;
    }
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

.option-controller-wrapper {
  width: 85%;
  background-color: white;
  margin: 0 auto;
  border-radius: 5px;
  height: fit-content;
}


@keyframes moveBG {
  0% {
    background-position: 0 10%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0 20%;
  }
}

.main {
  background: linear-gradient(30deg, #ad2969 0%, #654ea3 25%, #ad2969 50%, #654ea3 75%, #ad2969 100%);
  min-height: 100vh;
  width: 100vw;
  padding: 0 10px;
  margin: 0;
  animation: moveBG 20s infinite;
  background-size: 400% 400%;

  .position-toggle {
    width: 100%;
    display: flex;

    .btn {
      margin: 0 auto;
    }

  }

  .statuses {
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
    padding: 0;
    margin-bottom: 5%;
    display: flex;
  }

  .tilesWrapper {
    padding: 0 0;
  }
}
hr {
  width: 50%;
  background-color: #fff;
  height: 2px;
  border: none;
  margin: 5% auto;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}
</style>
