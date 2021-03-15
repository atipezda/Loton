//@ts-ignore
import {MacroInterface} from "~/pages/macros/index.vue";
import {ArmInformatorInterface} from "~/components/ArmInformator.vue";
import {InstructionListElement} from "~/components/InstructionList.vue";

export function countMacroTime(macroInstructions: MacroInterface['instructions']): number {
  let time = 0
  macroInstructions.forEach((elem: InstructionListElement) => {
    if (elem.type === 'move') {
      time += 1
    }
    if (elem.type === 'wait') {
      time += elem.value
    }
  })
  return time
}
