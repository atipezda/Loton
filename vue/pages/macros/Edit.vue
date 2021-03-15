<template>
  <b-row class="edit-main">
    <b-col lg="7">
      <MacroElement :length="macro.instructions.length" :name="macro.name" :time="macroTime">
        <NuxtLink to="/macros">
          <b-button variant="danger">anuluj</b-button>
        </NuxtLink>
        <b-button @click="saveList" variant="primary">zapisz</b-button>
      </MacroElement>
      <hr/>
      <InstructionList ref="instructionList" :preloadedList="macro.instructions"/>
    </b-col>
    <b-col class="card-list" lg="5">
    </b-col>
  </b-row>
</template>

<script lang="ts">
import {Component, Ref, Vue} from "nuxt-property-decorator"
import InstructionList, {InstructionListElement} from "~/components/InstructionList.vue";
import MacroElement from "~/components/MacroElement.vue";
import {MacroInterface} from "~/pages/macros/index.vue";
import {getDateString} from "~/helpers/dateHelper";
import {countMacroTime} from "~/helpers/macroHelper";


@Component({components: {MacroElement, InstructionList}})
export default class Index extends Vue {
  macro: MacroInterface = {
    time: 0,
    instructions: [],
    length: 0,
    name: getDateString()
  }

  @Ref() instructionList!: InstructionList

  mounted():void{
    this.preloadList()
  }

  get macroTime(){
    return countMacroTime(this.macro.instructions)
  }

  async preloadList(): Promise<void> {
    const id = this.$route.query.id
    if(!id) return;
    const res = await this.$axios.get('/api/getmacro', {params: {id}})
    console.log(res)
    this.macro = res.data
  }

  async saveList():void{
    const instructions: InstructionListElement[] = this.$refs.instructionList.list;
    this.macro.instructions = instructions;
    const macro = {
      ...this.macro,
      length: instructions.length,
      time: this.macroTime
    }
    console.log(macro)
    await this.$axios.post('/api/savemacro', macro)
    this.$router.push('/macros')
  }
}
</script>

<style lang="scss">
.edit-main{
  @include media-breakpoint-up('lg'){
    height: 90vh;
    overflow-y: auto;
  }
  .macro-element{
    @include media-breakpoint-up('lg'){
      position: fixed;
      top: 20%;
      right: 0;
      z-index: 2;
      width: 25%;
    }
  }
  .instruction-manager {
    @include media-breakpoint-up('lg') {
      margin: 0;
      position: fixed;
      top: 55%;
      right: -2%;
      z-index: 2;
      width: 25%;
    }
  }
}
</style>
