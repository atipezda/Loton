import socketio

from perfume import Perfume, route


class RobotServer(Perfume):

    @route('/')
    def hello(self):
        return "Hello World !"

    @route('/test')
    def helloWorld(self):
        return 'Hello, /test!'

    @route('/')
    def d(self):
        print('emit test')
        socketio.emit('testEvent', {'test': 1}, namespace='/test', broadcast=True)
        socketio.emit('testEvent', {'test': 2}, broadcast=True)
        return 'Hello, /'
