import os

import json

MACROS_PATH = 'macros/'

def generateId():
    highest = 0
    fileNames = os.listdir(MACROS_PATH)
    for file in fileNames:
        if not file.endswith('.json'):
            continue
        macroId = int(os.path.splitext(file)[0])
        if macroId > highest:
            highest = macroId

    return highest + 1


def openJson(jsonPath):
    with open(jsonPath, 'r') as f:
        return json.load(f)


def writeJson(path, filename, data):
    with open(os.path.join(path, str(filename) + '.json'), 'w') as f:
        json.dump(data, f)


def listMacros():
    fileNames = os.listdir(MACROS_PATH)
    macros = []
    for file in fileNames:
        if not file.endswith('.json'):
            continue
        macro = openJson(MACROS_PATH + file)
        del macro['instructions']
        macros.append(macro)
    print(macros)
    return macros


def getMacro(idNum):
    macro = openJson(MACROS_PATH + idNum + '.json')
    if macro:
        return macro
    return 'not found', 500


def saveMacro(macro):
    idNum = None
    if 'id' in macro:
        idNum = macro['id']
    if not idNum:
        idNum = generateId()
    macro['id'] = idNum
    print(macro)
    writeJson(MACROS_PATH, idNum, macro)
