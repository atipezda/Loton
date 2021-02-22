from types import SimpleNamespace
import json

import Adafruit_ADS1x15
import serial
from adafruit_servokit import ServoKit

from components.Potentiometer import Potentiometer
from components.ServoMotor import ServoMotor
from components.DcMotor import DcMotor
from components.UartServo import UartServo


def configPWMBoard(config):
    pwmConfig = config.pwm_board
    return ServoKit(channels=pwmConfig.channels, address=pwmConfig.address, frequency=pwmConfig.frequency)


def configADC():
    return Adafruit_ADS1x15.ADS1115()


def configServos(servos, kit, adc):
    servosReturn = []
    for servo in servos:
        potConfig = servo.potentiometer
        potentiometer = Potentiometer(potConfig.pin, potConfig.min_val, potConfig.max_val, potConfig.gain, adc)
        kitServo = kit.continuous_servo[servo.pin] if servo.is_360 else kit.servo[servo.pin]

        servo = ServoMotor(kitServo,
                           servo.name,
                           servo.pin,
                           servo.is_360,
                           servo.pulse_min,
                           servo.pulse_max,
                           servo.max_angle,
                           potentiometer
                           )
        servosReturn.append(servo)
        print(servos)
    return servosReturn


def dictToDns(diction):
    return SimpleNamespace(**diction)


def loadJsonConfig(configName):
    with open(configName, 'r') as f:
        return json.load(f, object_hook=dictToDns)


def configDCMotors(dc_motors):
    motors = []
    for motorConfig in dc_motors:
        motor = DcMotor(motorConfig.name,
                        motorConfig.pin_forward,
                        motorConfig.pin_backward,
                        motorConfig.move_duration,
                        motorConfig.initial)
        motors.append(motor)
    return motors


def createSerial(serialConfig):
    return serial.Serial(
        port=serialConfig.port,
        baudrate=serialConfig.baudrate,
    )


def configUartServos(uartBoardConfig, servos, adc):
    serialCom = createSerial(uartBoardConfig)
    servosReturn = []
    for servo in servos:
        potConfig = servo.potentiometer
        potentiometer = Potentiometer(potConfig.pin, potConfig.min_val, potConfig.max_val, potConfig.gain, adc)
        uartServo = UartServo(servo.id,
                              servo.name,
                              servo.speed,
                              servo.command_prefix,
                              servo.command_template,
                              servo.command_suffix,
                              serialCom,
                              potentiometer)
        servosReturn.append(uartServo)
    return servosReturn


def performConfiguration(configFilename):
    body = {}
    config = loadJsonConfig(configFilename)
    motorsConfig = config.motors

    adc = configADC()

    if motorsConfig.servos:
        kit = configPWMBoard(config)
        servos = configServos(motorsConfig.servos, kit, adc)
        body = addServosToBody(body, servos)

    if motorsConfig.dc_motors:
        motors = configDCMotors(motorsConfig.dc_motors)
        body = addDCsToBody(body, motors)

    if motorsConfig.uart_servos:
        uartServos = configUartServos(config.uart_board, motorsConfig.uart_servos, adc)
        body = addUartsToBody(body, uartServos)

    body = dictToDns(body)
    return body


def addServosToBody(body, servos):
    for servo in servos:
        body[servo.name] = servos[servo.pin]
    return body


def addDCsToBody(body, DCs):
    for motor in DCs:
        body[motor.name] = motor
    return body


def addUartsToBody(body, uarts):
    for uart in uarts:
        body[uart.name] = uart
    return body
