import {ArmInformatorInterface} from "~/components/ArmInformator.vue";

interface ServoInfo{
  name: string,
  value: number
}
interface ServoWidget extends  ServoInfo{
  iconName: string
}
