import time

from flask import jsonify, request
from flask_socketio import SocketIO
from perfume import Perfume, route

from helpers.macroHelper import listMacros, getMacro, saveMacro


class RobotServer(Perfume):
    socketio: object
    ee: object

    @route('/')
    def emitUpdate(self):
        self.ee.emit('move', 'arm', 40, 30)
        return 'ok'

    @route('/positions')
    def sendPosition(self):
        return jsonify(
            name="arm",
            value=20
        )

    @route('/macros')
    def macros(self):
        macros = listMacros()
        return jsonify(macros)

    @route('/savemacro', methods=['POST'])
    def saveMacro(self):
        macro = request.json
        saveMacro(macro)
        return "ok", 200

    @route('/getmacro')
    def macro(self):
        idNum = request.args.get('id')
        if not idNum:
            return "no id specified", 400
        macros = getMacro(idNum)
        return jsonify(macros)

    @route('/setpos', methods=['POST'])
    def setPos(self):
        positions = request.json
        print(positions)
        self.ee.emit("set", positions['name'], positions['value'])
        return 'ok', 200

    def configSocket(self, socketIo):
        self.socketio = socketIo

    def configEmitter(self, emitter):
        self.ee = emitter
        self.setupListeners(emitter)

    def EVENT_ServoMoved(self, name, angle, percent):
        # print(F'{name} has changed position to {angle} it is a {percent}%')
        self.socketio.emit('servoMove', {'name': name, 'percent': percent, 'angle': angle}, namespace='/positions',
                           broadcast=True)
        # print('emmited')

    def setupListeners(self, ee):
        ee.on("move", self.EVENT_ServoMoved)
