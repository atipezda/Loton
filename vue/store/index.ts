// import {ArmInformatorInterface} from "~/components/ArmInformator.vue";

import {ArmInformatorInterface} from "~/components/ArmInformator.vue";

interface StateObjectInterface {
  positions: ArmInformatorInterface[]
}


const stateObject: StateObjectInterface = {
  positions: [
    {
      id: 1,
      name: 'finger',
      iconName: 'arm.jpg',
      value: 20,
      isSwitch: true
    },
    {
      id: 2,
      name: 'wrist',
      iconName: 'arm.jpg',
      value: 80,
    },
    {
      id: 3,
      name: 'hand',
      iconName: 'arm.jpg',
      value: 45,
    },
    {
      id: 4,
      name: 'arm',
      iconName: 'arm.jpg',
      value: 10,
    },
    {
      id: 5,
      name: 'leg',
      iconName: 'arm.jpg',
      value: 95,
    },
    {
      id: 6,
      name: 'feet',
      iconName: 'arm.jpg',
      value: 55,
    }
  ]
}

export const state = () => (stateObject)

export const mutations = {
  updatePosition(state: StateObjectInterface, {name, value}: ArmInformatorInterface) {
    state.positions = state.positions.map((pos: ArmInformatorInterface) => {
      if (pos.name === name) {
        pos.value = value
      }
      return pos
    })
  }
}
