from helpers.dataHelper import mapValueToIntRange
from helpers.hexHelper import calcLength, encodeDec


class UartServo:
    def __init__(self, id, name, speed, maxAngle, startAngle, comPref, com, comSuff, serial):
        self.id = id
        self.name = name
        self.speed = speed
        self.maxAngle = maxAngle
        self.startAngle = startAngle
        self.comPref = comPref
        self.com = com
        self.comSuff = comSuff
        self.serial = serial

    def writeHex(self, hexString):
        command = bytes.fromhex(hexString)
        self.serial.write(command)

    def clearSerial(self):
        self.writeHex("08000000")

    def replaceCommand(self, command, position):
        speed = encodeDec(self.speed)
        position = encodeDec(position)
        command = command.replace("$id", self.id)
        command = command.replace("$position", str(position))
        command = command.replace("$speed", str(speed))
        return command

    def getValueFromAngle(self, angle):
        return mapValueToIntRange(angle, 0, 360, 0, 4095)

    def move(self, angle):
        if angle > self.maxAngle:
            raise Exception('angle over max')

        if not self.serial.isOpen():
            raise Exception('Uart is not open')

        angle += self.startAngle
        position = self.getValueFromAngle(angle)
        commandToSum = self.replaceCommand(self.com, position)
        command = self.replaceCommand(F"{self.comPref} {self.com} {self.comSuff}", position)
        comSum = calcLength(commandToSum)
        command = command.replace("$sum", comSum)

        self.clearSerial()
        self.writeHex(command)
        self.clearSerial()
