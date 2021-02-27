def decToHex(dec):
    return hex(dec).split('x')[-1]


def addBytesTo4(hexVal):
    hexLen = len(hexVal)
    toAdd = 4 - hexLen
    return "0" * toAdd + hexVal


def decTo4Hex(dec):
    hexVal = decToHex(dec)
    return addBytesTo4(hexVal)


def hexToDec(hexval):
    return int(hexval, 16)


def splitStrByNth(seq, n):
    o = []
    while seq:
        o.append(seq[:n])
        seq = seq[n:]
    return o


def switchBits(hexVal):
    spliced = splitStrByNth(hexVal, 2)
    ret = ""
    for hexNum in spliced[::-1]:
        ret += " " + hexNum
    return ret.strip()


def encodeDec(dec):
    hexVal = decTo4Hex(dec)
    return switchBits(hexVal)


def calcDecSumInHexString(hexString):
    decSum = 0
    for value in hexString.split(" "):
        decSum += hexToDec(value)
    return decSum


def bitand(val, andVal):
    return val & andVal


def bitXOr(val, orVal):
    return val ^ orVal


def calcLength(command):
    decSum = calcDecSumInHexString(command)
    bitAnd = bitand(decSum, 255)
    bitXor = bitXOr(bitAnd, 255)
    toHex = decToHex(bitXor)

    if len(toHex) < 2:
        return F"0{toHex}"
    return toHex
