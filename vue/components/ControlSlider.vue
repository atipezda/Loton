<template>
  <div class="control-slider">
    <Component :is="iconComponent" size="50"/>
    <b-form-input type="range" max="maxAngle" class="input-range" v-model="value" @update="update"/>
  </div>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"


@Component
export default class ControlSlider extends Vue {
  @Prop() readonly iconComponentPath!: string
  @Prop() readonly maxAngle!: number
  @Prop() readonly name!: string

  value: number = 0

  get iconComponent(){
    return () => import(`@/components/${this.iconComponentPath}`)
  }

  update(){
    this.$axios.post('/api/setpos',{
      name: this.name,
      value: this.value
    })
  }
}
</script>

<style lang="scss" scoped>
.control-slider{
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: 10% auto;
  border-radius: 5px;
  box-shadow: 0 0 10px #a0a0a0;
  padding: 2%;
  .input-range{
    margin: 0 5%;
  }
}

</style>
