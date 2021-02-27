import time

from flask import jsonify

from perfume import Perfume, route


class RobotServer(Perfume):
    socketio: object
    ee: object

    def configSocket(self, socketIo):
        self.socketio = socketIo

    def configEmitter(self, emitter):
        self.ee = emitter
        self.setupListeners(emitter)

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

    def EVENT_ServoMoved(self, name, angle, percent):
        print(F'{name} has changed position to {angle} it is a {percent}%')
        self.socketio.emit('servoMove', {'name': name, 'value': percent}, namespace='/positions', broadcast=True)
        print('emmited')

    def setupListeners(self, ee):
        ee.on("move", self.EVENT_ServoMoved)
    #
    # def setupEmitters(self, RobotControllerBody):
    #     for key in RobotControllerBody:
    #         elem = RobotControllerBody[key]
    #         if not elem.pot:
    #             pass
    #         elem._listen(self.socketio.start_background_task)
