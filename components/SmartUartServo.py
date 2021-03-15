import time

from components.UartServo import UartServo
from helpers.dataHelper import mapValueToIntRange


class SmartUartServo(UartServo):
    def __init__(self, potentiometer, ee, iD, name, speed, maxAngle, startAngle, comPref, com, comSuff, serial):
        super().__init__(iD, name, speed, maxAngle, startAngle, comPref, com, comSuff, serial)
        self.pot = potentiometer
        self.ee = ee

    def angleToPotential(self, angle):
        return mapValueToIntRange(angle, 0, self.maxAngle, self.pot.minVal, self.pot.maxVal)

    def potentialToAngle(self, potential):
        return mapValueToIntRange(potential, self.pot.minVal, self.pot.maxVal, 0, self.maxAngle)

    def angleToPercent(self, angle):
        return mapValueToIntRange(angle, 0, self.maxAngle, 0, 100)

    # async def startListening(self):
    #     previousAngle = 0
    #     while True:
    #         potential = self.pot.readValue()
    #         angle = self.potentialToAngle(potential)
    #         # percent = self.potentialToAngle(potential)
    #
    #         if previousAngle != angle:
    #             self.ee.emit('move', self.name, angle)
    #
    #         previousAngle = angle
    #         time.sleep(0.1)

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