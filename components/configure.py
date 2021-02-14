from types import SimpleNamespace
import json

from adafruit_servokit import ServoKit
from components.DcMotor import DcMotor


def configPWMBoard(config):
    pwmConfig = config.pwm_board
    return ServoKit(channels=pwmConfig.channels, address=pwmConfig.address, frequency=pwmConfig.frequency)


def configServos(servos, kit):
    for servo in servos:
        pin = servo.pin
        kit.servo[pin].actuation_range = servo.max_angle
        kit.servo[pin].set_pulse_width_range(servo.pulse_min, servo.pulse_max)
    return kit


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
    kit = configPWMBoard(config)
    motorsConfig = config.motors
    servoKit = configServos(motorsConfig.servos, kit)
    motors = configDCMotors(motorsConfig.dc_motors)
    body = addServosToBody(body, motorsConfig, servoKit)
    body = addDCsToBody(body, motors)
    body = dictToDns(body)
    return body


def addServosToBody(body, motorsConfig, kit):
    servos = motorsConfig.servos
    for servo in servos:
        body[servo.name] = kit.servo[servo.pin]
    return body


def addDCsToBody(body, DCs):
    for motor in DCs:
        body[motor.name] = motor
    return body
