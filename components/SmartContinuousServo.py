import time

from components.SmartServo import SmartServo


class SmartContinuousServo(SmartServo):
    def __init__(self, potentiometer, ee, continuousServoKit, name, pin, pulse_min, pulse_max, max_angle, speed):
        super().__init__(potentiometer, ee, continuousServoKit, name, pin, pulse_min, pulse_max, max_angle)
        self.speed = speed

    def _move(self, angle):
        done = False
        speed = self.speed

        while not done:
            wishedToSet = self.angleToPotential(angle)
            currentVal = self.pot.readRawValue()
            print(F"to set:{wishedToSet} current: {currentVal}")

            if abs(currentVal - wishedToSet) < 20:
                self.move360Servo('stop', 0)
                done = True

            if abs(currentVal - wishedToSet) < 800:
                speed = 0.1

            if currentVal > wishedToSet:
                self.move360Servo('forward', speed)

            elif currentVal < wishedToSet:
                self.move360Servo('backward', speed)

            else:
                self.move360Servo('stop', 0)
                done = True

    def move360Servo(self, direction, speed):
        print(direction)
        if direction == 'forward':
            self.servo.throttle = speed
        elif direction == 'backward':
            self.servo.throttle = -speed
        elif direction == 'stop':
            self.servo.throttle = 0
