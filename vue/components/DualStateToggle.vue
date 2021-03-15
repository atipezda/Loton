<template>
  <div class="dualtoggle-container" :class="{right: isRightSelected}">
    <button @click="toggle('left')" class="dualtoggle-slot">{{leftOption}}</button>
    <button @click="toggle('right')" class="dualtoggle-slot">{{rightOption}}</button>
    <div class="dualtoggle-switch"/>
  </div>

</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"


@Component
export default class DualStateToggle extends Vue {
  isRightSelected: boolean = true

  @Prop() leftOption!: string
  @Prop() rightOption!: string

  toggle(selected: 'left' | 'right'): void {
    this.isRightSelected = selected === 'right';
    this.$emit('toggle', selected)
  }
}
</script>

<style lang="scss" scoped>
.dualtoggle-container {
  border-radius: 3px;
  width: 150px;
  background-color: #d0d0d0;
  display: flex;
  flex-direction: row;
  justify-content: center;
  color: white;
  position: relative;

  .dualtoggle-switch {
    border-radius: 2px;
    height: 70%;
    top: 15%;
    position: absolute;
    width: 42%;
    background-color: #654ea3;
    z-index: 1;
    left: 5%;
    right: auto;
    transition: 1s;
  }


  button {
    z-index: 2;
    margin: 0 auto;
    background: none;
    border: none;
    transition: 0.5s;
    font-weight: bold;
  }
  button:first-of-type{
    color: white;
  }
  button:nth-child(2){
    color: #654ea3;
  }

  &.right {
    .dualtoggle-switch {
      transition: 1s;
      left: 53%;
    }
    button:first-of-type{
      color: #654ea3;
    }
    button:nth-child(2){
      color: white;
    }
  }


}
</style>
