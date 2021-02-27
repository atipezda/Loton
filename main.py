import time

from gevent import monkey

monkey.patch_all()
from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO
from flask_cors import CORS

from components.RobotController import RobotController
from components.RobotServer import RobotServer
from pymitter import EventEmitter

from components.configure import loadJsonConfig


def testFunction(part, io):
    previousPercent = 0
    while True:
        potential = part.pot.readRawValue()
        angle = part.potentialToAngle(potential)
        percent = part.angleToPercent(angle)
        if previousPercent != percent:
            part.ee.emit('move', part.name, angle, percent)
            previousPercent = percent
        io.sleep(0.3)


ee = EventEmitter()
if __name__ == '__main__':
    print('starting....')
    LotonServer = RobotServer(__name__)
    config = loadJsonConfig('config.json')
    app = LotonServer.app
    socketio = SocketIO(LotonServer.app, async_mode='eventlet', cors_allowed_origins='*')
    LotonController = RobotController(config, ee)
    LotonServer.configSocket(socketio)
    LotonServer.configEmitter(ee)
    # for key in LotonController.body:
    #     # LotonController.body[key].startListening(socketio.start_background_task)
    #     # arm = LotonController.body[key]
    #     # socketio.start_background_task(testFunction,arm,socketio)
    LotonController.setupEmitters(socketio.start_background_task, socketio.sleep)

    LotonController.body['feet'].move(0)
    time.sleep(5)
    LotonController.body['feet'].move(90)
    time.sleep(5)
    LotonController.body['feet'].move(180)
    time.sleep(5)
    LotonController.body['feet'].move(360)


    print('socketIo start')
    socketio.run(LotonServer.app, host='0.0.0.0', debug=True)
