import time

from gpiozero import Motor


class DcMotor:
    def __init__(self, name, pinForward, pinBackward, frontDuration ,backDuration, initialState, ee):
        self.name = name
        self.actualPosition = ''
        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.frontDuration = frontDuration
        self.backDuration = backDuration
        self.initialState = initialState
        self.ee = ee
        self.motor = Motor(pinForward, pinBackward)
        self.move(initialState)

    def move(self, position):
        if position not in ['forward', 'backward']:
            Exception("position must by either 'forward' or 'backward'")

        angle = 100 if position == 'forward' else 0
        percent = 100 if position == 'forward' else 0
        self.ee.emit('move', self.name, angle, percent)
        if position == 'forward':
            self.motor.forward()
            time.sleep(self.frontDuration)
        else:
            self.motor.backward()
            time.sleep(self.backDuration)

        self.actualPosition = position
        self.motor.stop()
