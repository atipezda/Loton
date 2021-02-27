<template>
  <div class="positions-widget">
    <ArmInformator v-for="pos in positions" v-bind="pos"/>
  </div>
</template>

<script lang="ts">
import {Component,Vue} from "nuxt-property-decorator"
import ArmInformator, {ArmInformatorInterface} from "~/components/ArmInformator.vue";

@Component({
  components: {
    ArmInformator
  }
})
export default class PositionsWidget extends Vue {
  private socket: any;

  get positions(){
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
        this.updateServo(servo.name, servo.value)
      })
    this.socket.on('disconnect', function() {
      console.log('Socket disconnected');
    });
    this.socket.on('connect', function() {
      console.log('Socket connected !!');
    });
  }

  updateServo(name: string, value: number): void {
    console.log(name,value)
    this.$store.commit('updatePosition', {name,value})
  }
}
</script>

<style lang="scss" scoped>
.positions-widget{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}
</style>
