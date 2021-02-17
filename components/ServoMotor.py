import time

from gpiozero import Motor

import asyncio

from helpers.dataHelper import mapValueToIntRange


class ServoMotor:
    def __init__(self, kitServo, name, pin, is_360, pulse_min, pulse_max, max_angle, potentiometer):
        self.servo = kitServo  # kit_servo or kit_continuous_servo
        self.name = name
        self.pin = pin
        self.is_360 = is_360
        self.pulse_min = pulse_min
        self.pulse_max = pulse_max
        self.max_angle = max_angle
        self.pot = potentiometer

        self.configure()

    def configure(self):
        self.servo.set_pulse_width_range(self.pulse_min, self.pulse_max)
        if not self.is_360:
            self.servo.actuation_range = self.max_angle

    async def set360ServoPosition(self, angle):
        done = False
        speed = 0.3

        while not done:
            wishedToSet = self.mapAngleToPotentiometerValue(angle)
            currentVal = self.pot.readRawValue()
            currentPos = self.mapPotentiometerToAngleValue(currentVal)
            # print(f"ServoAngle: {currentVal} toSet: {wishedToSet}")
            print(f"ServoAngle: {currentPos} toSet: {angle} speed: {speed}")
            # print(self.pot.readRawValue())
            # time.sleep(1)

            print(abs(currentVal - wishedToSet))

            if abs(currentVal - wishedToSet) < 10:
                print('Servo in right position')
                self.move360Servo('stop')
                done = True
                pass

            if abs(currentVal - wishedToSet) < 600:
                speed = 0.25

            if abs(currentVal - wishedToSet) < 300:
                speed = 0.1

            elif currentVal > wishedToSet:
                self.move360Servo('backward', speed)

            elif currentVal < wishedToSet:
                self.move360Servo('forward', speed)

            else:
                self.move360Servo('stop')
                done = True

    def move360Servo(self, direction, speed=0.3):
        if direction == 'forward':
            self.servo.throttle = speed
        elif direction == 'backward':
            self.servo.throttle = -speed
        elif direction == 'stop':
            self.servo.throttle = 0

    async def setAngle(self, angle):
        if not self.is_360:
            self.servo.angle = angle
        else:
            await self.set360ServoPosition(angle)

    def mapAngleToPotentiometerValue(self, value):
        return mapValueToIntRange(value, 0, self.max_angle, self.pot.minVal, self.pot.maxVal)

    def mapPotentiometerToAngleValue(self, value):
        return mapValueToIntRange(value, self.pot.minVal, self.pot.maxVal, 0, self.max_angle)
