<template>
  <div class="positions-widget">
    <ArmInformator v-for="pos in positions" :mode="mode" v-bind="pos"/>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from "nuxt-property-decorator"
import ArmInformator, {ArmInformatorInterface} from "~/components/ArmInformator.vue";
import DualStateToggle from "~/components/DualStateToggle.vue";
import {StateObjectInterface} from "~/store";

@Component({
  components: {
    DualStateToggle,
    ArmInformator
  }
})
export default class PositionsWidget extends Vue {
  private socket: any;

  get mode(): StateObjectInterface['viewMode'] {
    return this.$store.state.viewMode
  }

  get positions() {
    const pos = this.$store.state.positions
    return pos
  }


  async mounted(): Promise<void> {
    this.socket = this.$nuxtSocket({
      transports: ['websocket', 'polling', 'flashsocket'],
      name: 'main',
      channel: '/positions',
      reconnect: true
    })
    this.socket
      .on('servoMove', (servo: any) => {
        this.updateServo(servo.name, servo.percent, servo.angle)
      })
    this.socket.on('disconnect', function() {
      console.log('Socket disconnected');
    });
    this.socket.on('connect', function() {
      console.log('Socket connected !!');
    });
  }

  updateServo(name: string, percent: number, angle: number): void {
    this.$store.commit('updatePosition', {name, percent, angle})
  }
}
</script>

<style lang="scss" scoped>
.positions-widget{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-around;
  height: 100%;
}
</style>
