import _thread
import time

from flask_socketio import SocketIO

from components.Servo import Servo
from helpers.dataHelper import mapValueToIntRange


class SmartServo(Servo):
    def __init__(self, potentiometer, ee, kitServo, name, pin, pulse_min, pulse_max, max_angle):
        super().__init__(kitServo, name, pin, pulse_min, pulse_max, max_angle)
        self.pot = potentiometer
        self.ee = ee
        self.thread = None

    def angleToPotential(self, angle):
        return mapValueToIntRange(angle, 0, self.max_angle, self.pot.minVal, self.pot.maxVal)

    def potentialToAngle(self, potential):
        return mapValueToIntRange(potential, self.pot.minVal, self.pot.maxVal, 0, self.max_angle)

    def angleToPercent(self, angle):
        return mapValueToIntRange(angle, 0, self.max_angle, 0, 100)

    def _listen(self, asyncSleepProvider, sleepInterval=0.3):
        previousPercent = 0
        while True:
            potential = self.pot.readRawValue()
            angle = self.potentialToAngle(potential)
            percent = self.angleToPercent(angle)
            if previousPercent != percent:
                self.ee.emit('move', self.name, angle, percent)
                previousPercent = percent
            asyncSleepProvider(sleepInterval)

    # def startListening(self, threadProvider):
    #     # self.thread = _thread.Thread(name=F"{self.name}.listener", target=self._listen)
    #     # _thread.start_new_thread(self._listen, ())
    #     threadProvider(self._listen)
    #     # self.thread.daemon = True
    #     # self.thread.start()
    #     return
