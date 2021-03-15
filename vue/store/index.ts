// import {ArmInformatorInterface} from "~/components/ArmInformator.vue";

import {ArmInformatorInterface} from "~/components/ArmInformator.vue";

export interface StateObjectInterface {
  positions: ArmInformatorInterface[],
  isArmInformatorVisible: boolean,
  viewMode: 'angle' | 'percent';
}


const stateObject: StateObjectInterface = {
  positions: [
    {
      id: 1,
      name: 'finger',
      iconComponentPath: 'icons/parts/FingerIcon.vue',
      percent: 50,
      angle: 90,
      maxAngle: 180,
      isSwitch: true
    },
    {
      id: 2,
      name: 'wrist',
      iconComponentPath: 'icons/parts/WristIcon.vue',
      percent: 50,
      angle: 90,
      maxAngle: 180,
    },
    {
      id: 3,
      name: 'hand',
      iconComponentPath: 'icons/parts/HandIcon.vue',
      percent: 50,
      angle: 90,
      maxAngle: 180,
    },
    {
      id: 4,
      name: 'arm',
      iconComponentPath: 'icons/parts/ArmIcon.vue',
      percent: 50,
      angle: 90,
      maxAngle: 180,
    },
    {
      id: 5,
      name: 'leg',
      iconComponentPath: 'icons/parts/LegIcon.vue',
      percent: 50,
      angle: 90,
      maxAngle: 180,
    },
    {
      id: 6,
      name: 'feet',
      iconComponentPath: 'icons/parts/FeetIcon.vue',
      percent: 50,
      angle: 90,
      maxAngle: 180,
    }
  ],
  isArmInformatorVisible: true,
  viewMode: 'angle',
}

//@ts-ignore
export const state: StateObjectInterface = () => (stateObject);

export const mutations = {
  updatePosition(state: StateObjectInterface, {name, percent, angle}: ArmInformatorInterface) :void{
    state.positions = state.positions.map((pos: ArmInformatorInterface) => {
      if (pos.name === name){
        pos.percent = percent
        pos.angle = angle
      }
      return pos
    })
  },

  toggleArmInformator(state: StateObjectInterface): void{
    state.isArmInformatorVisible = !state.isArmInformatorVisible
  },

  changeViewMode(state:StateObjectInterface, mode:StateObjectInterface['viewMode']) :void{
    state.viewMode = mode
  },

}
