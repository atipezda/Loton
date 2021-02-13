from types import SimpleNamespace
import json

from adafruit_servokit import ServoKit


def configPWMBoard(config):
    pwmConfig = config.pwm_board
    return ServoKit(channels=pwmConfig.channels, frequency=pwmConfig.frequency)


def configServos(config, kit):
    for servo in config.servos:
        pin = servo.pin
        kit.servo[pin].actuation_range = servo.max_angle
        kit.servo[pin].set_pulse_width_range(servo.pulse_min, servo.pulse_max)


def dictToDns(diction):
    return SimpleNamespace(**diction)


def loadJsonConfig(configName):
    with open(configName, 'r') as f:
        return json.load(f, object_hook=dictToDns)


def performConfiguration(configFilename):
    config = loadJsonConfig(configFilename)
    kit = configPWMBoard(config)
    configServos(config, kit)
    body = getBody(config, kit)
    return body


def getBody(config, kit):
    body = {}
    servos = config.servos
    for servo in servos:
        body[servo.name] = kit.servo[servo.pin]
    return dictToDns(body)
