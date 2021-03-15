from gpiozero import CPUTemperature


def readRPITemp():
    cpu = CPUTemperature()
    return int(cpu.temperature)
