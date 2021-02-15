from types import SimpleNamespace
import json

from adafruit_servokit import ServoKit

from components.ServoMotor import ServoMotor
from components.DcMotor import DcMotor


def configPWMBoard(config):
    pwmConfig = config.pwm_board
    return ServoKit(channels=pwmConfig.channels, address=pwmConfig.address, frequency=pwmConfig.frequency)


def configServos(servos, kit):
    servosReturn = []
    for servo in servos:
        kitServo = kit.servo[servo.pin]
        servo = ServoMotor(kitServo,
                           servo.name,
                           servo.pin,
                           servo.is_360,
                           servo.pulse_min,
                           servo.pulse_max,
                           servo.max_angle)
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
    kit = configPWMBoard(config)
    motorsConfig = config.motors
    servos = configServos(motorsConfig.servos, kit)
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
