<template>
  <b-row class="index-main">
    <b-col lg="12" class="macros">
      <h2>Nagrania</h2>
      <MacroElement v-for="macro in macros" v-bind="macro">
        <b-button @click="()=>false" variant="danger">usuń</b-button>
        <b-button @click="edit(macro.id)" variant="secondary">edytuj</b-button>
        <b-button @click="()=>false" variant="primary">odtwórz</b-button>
      </MacroElement>
      <b-card class="add-macro-card">
        <b-body>
          <NuxtLink to="/macros/edit">
            <b-button variant="success">
              <AddIcon color="#fff"/>
            </b-button>
          </NuxtLink>
        </b-body>
      </b-card>
    </b-col>
  </b-row>
</template>

<script lang="ts">
import {Component, Vue} from "nuxt-property-decorator"
import InstructionList, {InstructionListElement} from "~/components/InstructionList.vue";
import MacroElement from "~/components/MacroElement.vue";
import AddIcon from "~/components/icons/AddIcon.vue";


export interface MacroInterface {
  name: string,
  length: number,
  time: number,
  instructions?: InstructionListElement[]
}

@Component({components: {AddIcon, MacroElement, InstructionList}})
export default class Index extends Vue {
  macros: MacroInterface = [];

  async mounted(): void {
    const res = await this.$axios.get('/api/macros');
    this.macros = res.data;
  }

  edit(id: number): void {
    this.$router.push({
      path: `/macros/edit?id=${id}`
    })
  }


}
</script>

<style lang="scss">
.macros {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;

  > h2 {
    color: white;
    width: 100%;
    text-align: center;
  }

  .macro-element {
    width: 100%;
    @include media-breakpoint-up('md') {
      width: 40%;
      flex: 40%;
    }
  }

  .add-macro-card {
    height: fit-content;
    flex: 90%;
    margin-left: 3%;
    margin-right: 3%;
    .card-body{
      display: flex;
      justify-content: center;
    }
  }
}
</style>
