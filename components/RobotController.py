from components.configure import configPWMBoard, configADCs, configServos, addServosToBody, configDCMotors, \
    addDCsToBody, \
    configUartServos, addUartsToBody


class RobotController:
    def __init__(self, config, ee):
        self.config = config
        self.kit = None
        self.adcs = None
        self.body = None
        self.ee = ee
        self.configure()
        self.setupListeners()

    def createBody(self):
        body = {}
        config = self.config
        motorsConfig = config.motors
        ee = self.ee
        if motorsConfig.servos:
            servos = configServos(motorsConfig.servos, self.kit, self.adcs, ee)
            body = addServosToBody(body, servos)

        if motorsConfig.dc_motors:
            motors = configDCMotors(motorsConfig.dc_motors, ee)
            body = addDCsToBody(body, motors)

        if motorsConfig.uart_servos:
            uartServos = configUartServos(config.uart_board, motorsConfig.uart_servos, self.adcs, ee)
            body = addUartsToBody(body, uartServos)

        return body

    def configure(self):
        config = self.config
        self.kit = configPWMBoard(config.pwm_board)
        self.adcs = configADCs(config.adcConverters)
        self.body = self.createBody()

    def setupEmitters(self, threadProvider, sleepProvider):
        for key in self.body:
            elem = self.body[key]
            if hasattr(elem, 'pot'):
                threadProvider(elem._listen, sleepProvider)

    def setPosition(self, part, position):
        print('setting part')
        self.body[part].move(int(position))

    def setupListeners(self):
        self.ee.on("set", self.setPosition)

    def moveRobot(self, positions):
        pass
