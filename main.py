import time

import RPi.GPIO as GPIO
from components.configure import performConfiguration

robot = performConfiguration('config.json')

robot.feet.move(4095)
time.sleep(4)
robot.feet.move(3000)
time.sleep(2)
robot.feet.move(0)
