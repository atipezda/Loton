import time

from gpiozero import Motor


class DcMotor:
    def __init__(self, name, pinForward, pinBackward, moveDuration, initialState):
        self.name = name
        self.actualPosition = ''
        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.duration = moveDuration
        self.initialState = initialState
        self.motor = Motor(pinForward, pinBackward)
        self.move(initialState)

    def move(self, position):
        if position not in ['forward', 'backward']:
            Exception("position must by either 'forward' or 'backward'")

        if position == 'forward':
            self.motor.forward()
        else:
            self.motor.backward()

        time.sleep(self.duration)
        self.actualPosition = position
        self.motor.stop()
