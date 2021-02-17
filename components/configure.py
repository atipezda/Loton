from types import SimpleNamespace
import json

import Adafruit_ADS1x15
from adafruit_servokit import ServoKit

from components.Potentiometer import Potentiometer
from components.ServoMotor import ServoMotor
from components.DcMotor import DcMotor


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


def performConfiguration(configFilename):
    body = {}
    config = loadJsonConfig(configFilename)
    motorsConfig = config.motors
    kit = configPWMBoard(config)
    adc = configADC()
    servos = configServos(motorsConfig.servos, kit, adc)
    motors = configDCMotors(motorsConfig.dc_motors)
    body = addServosToBody(body, servos)
    body = addDCsToBody(body, motors)
    body = dictToDns(body)
    return body


def addServosToBody(body, servos):
    print(servos)
    for servo in servos:
        body[servo.name] = servos[servo.pin]
    return body


def addDCsToBody(body, DCs):
    for motor in DCs:
        body[motor.name] = motor
    return body
