from components.configure import configPWMBoard, configADC, configServos, addServosToBody, configDCMotors, addDCsToBody, \
    configUartServos, addUartsToBody


class RobotController:
    def __init__(self, config):
        self.config = config
        self.kit = None
        self.adc = None
        self.body = None
        self.configure()

    def createBody(self):
        body = {}
        config = self.config
        motorsConfig = config.motors
        if motorsConfig.servos:
            servos = configServos(motorsConfig.servos, self.kit, self.adc)
            body = addServosToBody(body, servos)

        if motorsConfig.dc_motors:
            motors = configDCMotors(motorsConfig.dc_motors)
            body = addDCsToBody(body, motors)

        if motorsConfig.uart_servos:
            uartServos = configUartServos(config.uart_board, motorsConfig.uart_servos, self.adc)
            body = addUartsToBody(body, uartServos)

        return body

    def configure(self):
        config = self.config
        self.kit = configPWMBoard(config.pwm_board)
        self.adc = configADC()
        self.body = self.createBody()

    def moveRobot(self, positions):
        pass
