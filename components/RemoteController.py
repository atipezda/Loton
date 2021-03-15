from time import sleep
import liquidcrystal_i2c
import smbus2

from helpers.dataHelper import spaceTheString
from helpers.hardwareHelper import readRPITemp


class RemoteController:
    def __init__(self):
        self.bus = smbus2.SMBus(1)
        self.address = 0x08
        self.dataToSend = 1
        self.responsePayloadSize = 11
        self.rows = 4
        self.cols = 20
        self.lcd = liquidcrystal_i2c.LiquidCrystal_I2C(0x27, 1, numlines=self.rows)
        self.positions = {}
        self.previousPositions = {}

    def setPositionsFromData(self, data):
        self.previousPositions = self.positions
        self.positions = {
            'hand': data[0] + data[1],
            'arm': data[2] + data[3],
            'feet': data[4] + data[5],
            'wrist': data[6] + data[7],
            'leg': data[8] + data[9],
            'fing': data[10]
        }

    def setupConnection(self):
        sleep(2)
        while True:
            try:
                dataToSend = self.dataToSend
                data = self.bus.read_i2c_block_data(self.address, dataToSend, self.responsePayloadSize)
                self.setPositionsFromData(data)
                print(self.positions)
                if self.previousPositions != self.positions:
                    self.writeDisplay()
                sleep(1)
            except OSError:
                pass


    def writeDisplay(self):
        handPos = spaceTheString(self.positions['hand'], 3)
        armPos = spaceTheString(self.positions['arm'], 3)
        feetPos = spaceTheString(self.positions['feet'], 3)
        wristPos = spaceTheString(self.positions['wrist'], 3)
        legPos = spaceTheString(self.positions['leg'], 3)
        fingPos = spaceTheString(self.positions['fing'], 3)
        temp = readRPITemp()
        self.lcd.printline(0, F"HAND:{handPos}     ARM:{armPos}")
        self.lcd.printline(1, F"FEET:{feetPos}   WRIST:{wristPos}")
        self.lcd.printline(2, F"FING:{fingPos}     LEG:{legPos}")
        self.lcd.printline(3, F"TEMP:{temp}")

