class Servo:
    def __init__(self, kitServo, name, pin, pulse_min, pulse_max, max_angle):
        self.servo = kitServo
        self.name = name
        self.pin = pin
        self.pulse_min = pulse_min
        self.pulse_max = pulse_max
        self.max_angle = max_angle
        self.configure()

    def configure(self):
        self.servo.set_pulse_width_range(self.pulse_min, self.pulse_max)
        self.servo.actuation_range = self.max_angle

    def _move(self, angle):
        self.servo.angle = angle

    def move(self, angle):
        self._move(angle)