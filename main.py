import time

import RPi.GPIO as GPIO

from components.RobotController import RobotController
from components.configure import loadJsonConfig

config = loadJsonConfig('config.json')

controller = RobotController(config)
