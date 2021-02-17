from helpers.dataHelper import mapValueToIntRange


class Potentiometer:
    def __init__(self, pin, minVal, maxVal, gain, adc):
        self.pin = pin
        self.minVal = minVal
        self.maxVal = maxVal
        self.gain = gain
        self.adc = adc
        self.startAdc()

    def readPercentValue(self, value):
        mapValueToIntRange(value, self.minVal, self.maxVal, 0, 100)

    def startAdc(self):
        gan = 2/3
        self.adc.start_adc(self.pin, gain=gan)

    def readRawValue(self):
        return self.adc.get_last_result()

    def readValue(self):
        val = self.readRawValue()
        cut = str(val)[0:3]
        return int(cut)
