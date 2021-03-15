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
    LotonController.setupEmitters(socketio.start_background_task, socketio.sleep)
    print('socketIo start')
    socketio.run(LotonServer.app, host='0.0.0.0', debug=True)
