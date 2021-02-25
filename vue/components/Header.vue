<template>
  <header class="nav-header">
    <img src="@/assets/logo.png">
    <b-button class="logout" variant="danger">Wyloguj</b-button>
  </header>
</template>

<script lang="ts">
import {Component,Vue} from "nuxt-property-decorator"


@Component
export default class Header extends Vue {

}
</script>

<style lang="scss" scoped>
</style>
