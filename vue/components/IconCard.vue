<template>
  <div class="icon-card">
    <b-card>
      <b-card-title>{{title}}</b-card-title>
      <b-card-body class="icon-card-body">
        <img :src="icon"/>
        <b-card-text class="icon-card-text">
          {{text}}
        </b-card-text>
        <NuxtLink :to="href" v-if="href">
          <b-btn variant="primary" class="icon-card-button">{{buttonText}}</b-btn>
        </NuxtLink>
          <b-btn v-else variant="primary" class="icon-card-button" @click="emitButton">{{buttonText}}</b-btn>

      </b-card-body>
<!--      <b-card-text class="small text-muted">Last updated 3 mins ago</b-card-text>-->
    </b-card>
  </div>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "nuxt-property-decorator"
import {getAsset} from '@/helpers/assetHelper';

export interface IconCardInterface{
  title:string;
  text:string;
  buttonText:string;
  iconName:string;
  href?: string
}

@Component
export default class IconCard extends Vue {
  @Prop({required: true})readonly  title!:string
  @Prop({required: true})readonly  text!:string
  @Prop({required: true})readonly  buttonText!:string
  @Prop({required: false})readonly  href!:string
  @Prop({required: true, default: ()=>''})readonly  iconName!:string

  emitButton():void{
    this.$emit('buttonClick');
  }

  get icon():string{
    return getAsset(this.iconName)
  }

}
</script>

<style lang="scss" scoped>
.icon-card {
  width: auto;
  margin-bottom: 10%;

  @include media-breakpoint-up(lg) {
    width: 90%;
  }

  img{
    width: 50px;
    height: 50px;
    margin: auto 2% auto 0;
  }

  .icon-card-body{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;

    .icon-card-text{
      width: 80%;
      @include media-breakpoint-up(md){
        width: 60%;
      }
    }

    .icon-card-button{
      min-width: 30px;
      margin-left: auto;
      margin-right: 0;
    }
  }
}
</style>
