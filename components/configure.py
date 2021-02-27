from types import SimpleNamespace
import json

import Adafruit_ADS1x15
import serial
from adafruit_servokit import ServoKit

from components.Potentiometer import Potentiometer
from components.DcMotor import DcMotor
from components.SmartContinuousServo import SmartContinuousServo
from components.SmartServo import SmartServo
from components.SmartUartServo import SmartUartServo


def configPWMBoard(pwmConfig):
    return ServoKit(channels=pwmConfig.channels, address=pwmConfig.address, frequency=pwmConfig.frequency)


def configADCs(adcs):
    out = []
    for adc in adcs:
        createdADC = Adafruit_ADS1x15.ADS1115(address=adc.address)

        out.append({
            "id": adc.id,
            "adc": createdADC
        })

    return out


def configServos(servos, kit, adcs, ee):
    servosReturn = []
    kitServo = None
    servo = None
    for servo in servos:
        potConfig = servo.potentiometer

        chosenADC = None
        for adc in adcs:
            if potConfig.adc == adc["id"]:
                chosenADC = adc["adc"]

        potentiometer = Potentiometer(potConfig.pin, potConfig.min_val, potConfig.max_val, potConfig.gain, chosenADC,
                                      ee)

        if servo.is_360:
            kitServo = kit.continuous_servo[servo.pin]
            servo = SmartContinuousServo(potentiometer,
                                         ee,
                                         kitServo,
                                         servo.name,
                                         servo.pin,
                                         servo.pulse_min,
                                         servo.pulse_max,
                                         servo.max_angle,
                                         servo.speed
                                         )
        else:
            kitServo = kit.servo[servo.pin]
            servo = SmartServo(potentiometer,
                               ee,
                               kitServo,
                               servo.name,
                               servo.pin,
                               servo.pulse_min,
                               servo.pulse_max,
                               servo.max_angle,
                               )
        servosReturn.append(servo)
    return servosReturn


def dictToDns(diction):
    return SimpleNamespace(**diction)


def loadJsonConfig(configName):
    with open(configName, 'r') as f:
        return json.load(f, object_hook=dictToDns)


def configDCMotors(dc_motors, ee):
    motors = []
    for motorConfig in dc_motors:
        motor = DcMotor(motorConfig.name,
                        motorConfig.pin_forward,
                        motorConfig.pin_backward,
                        motorConfig.forward_duration,
                        motorConfig.backward_duration,
                        motorConfig.initial,
                        ee)
        motors.append(motor)
    return motors


def createSerial(serialConfig):
    return serial.Serial(
        port=serialConfig.port,
        baudrate=serialConfig.baudrate,
    )


def configUartServos(uartBoardConfig, servos, adcs, ee):
    serialCom = createSerial(uartBoardConfig)
    servosReturn = []
    for servo in servos:
        potConfig = servo.potentiometer

        chosenADC = None
        for adc in adcs:
            if potConfig.adc == adc["id"]:
                chosenADC = adc["adc"]

        potentiometer = Potentiometer(potConfig.pin, potConfig.min_val, potConfig.max_val, potConfig.gain, chosenADC,
                                      ee)
        uartServo = SmartUartServo(
            potentiometer,
            ee,
            servo.id,
            servo.name,
            servo.speed,
            servo.max_angle,
            servo.command_prefix,
            servo.command_template,
            servo.command_suffix,
            serialCom
        )
        servosReturn.append(uartServo)
    return servosReturn


def addServosToBody(body, servos):
    for servo in servos:
        body[servo.name] = servo
    return body


def addDCsToBody(body, DCs):
    for motor in DCs:
        body[motor.name] = motor
    return body


def addUartsToBody(body, uarts):
    for uart in uarts:
        body[uart.name] = uart
    return body
