<template>
  <b-card class="instruction-manager">
     <b-card-body>
       <AddIcon/>
       <b-button @click="$emit('waitAdd')" variant="secondary">czas</b-button>
       <b-button @click="$emit('moveAdd')" variant="success">pozycja</b-button>
     </b-card-body>
  </b-card>
</template>

<script lang="ts">
import {Component,Vue} from "nuxt-property-decorator"
import AddIcon from "~/components/icons/AddIcon.vue";
@Component({
  components: {AddIcon}
})
export default class InstructionManager extends Vue {

}
</script>

<style lang="scss" scoped>
.instruction-manager{
  .card-body{
    display: flex;
    padding: 2%;
    align-items: center;
    flex-wrap: wrap;
    .btn{
      margin: 0 auto;
      width: 30%;
    }
    //@include media-breakpoint-up('lg'){
    //  justify-content: space-around;
    //  .btn{
    //    width: 90%;
    //    margin: 5% auto;
    //  }
    //}
  }
}
</style>
