import time

from gpiozero import Motor


class ServoMotor:
    def __init__(self, kitServo, name, pin,is_360,pulse_min, pulse_max,max_angle):
        self.servo = kitServo
        self.name = name
        self.pin = pin
        self.is_360 = is_360
        self.pulse_min = pulse_min
        self.pulse_max = pulse_max
        self.max_angle = max_angle
        self.configure()

    def configure(self):
        self.servo.actuation_range = self.max_angle
        self.servo.set_pulse_width_range(self.pulse_min, self.pulse_max)

    def setAngle(self, angle):
        self.servo.angle = angle
