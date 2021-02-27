import Adafruit_ADS1x15
import time, curses

ADC1 = 72
ADC2 = 75

adc0 = Adafruit_ADS1x15.ADS1115(address=ADC1)
adc1 = Adafruit_ADS1x15.ADS1115(address=ADC2)
GAIN = 2 / 3

pot = [
    {
        "name": 'feet',
        "adc": 0,
        "pin": 0,
        "max": 0,
        "min": 9999999
    },
    {
        "name": 'leg',
        "adc": 0,
        "pin": 1,
        "max": 0,
        "min": 9999999
    },
    {
        "name": 'arm',
        "adc": 0,
        "pin": 2,
        "max": 0,
        "min": 9999999
    },
    {
        "name": 'hand',
        "adc": 0,
        "pin": 3,
        "max": 0,
        "min": 9999999
    },
    {
        "name": 'wrist',
        "adc": 1,
        "pin": 0,
        "max": 0,
        "min": 9999999
    }
]


def readPotentiometers(potentiometers, scr):
    i = 0
    for p in potentiometers:
        val = None
        if p['adc'] == 0:
            val = adc0.read_adc(p['pin'], GAIN)
        else:
            val = adc1.read_adc(p['pin'], GAIN)

        if val > p['max']:
            p['max'] = val
        if val < p['min']:
            p['min'] = val

        scr.addstr(i, 0, F"{p['name']} min: {p['min']} max: {p['max']} val: {val}")
        i += 1


scr = curses.initscr()
while True:
    readPotentiometers(pot, scr)
    scr.refresh()
    time.sleep(1)

# adc.stop_adc()
# 7392
# 8784


# import time, curses
# scr = curses.initscr()
# scr.addstr(0, 0, "Current Time:")
# scr.addstr(1, 0, "Hello World!")
# while True:
#     scr.addstr(0, 20, time.ctime())
