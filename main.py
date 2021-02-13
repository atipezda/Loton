import RPi.GPIO as GPIO
from components.configure import performConfiguration

robot = performConfiguration('config.json')

robot.wrist.angle = 135

GPIO.cleanup()