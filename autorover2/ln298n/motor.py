import RPi.GPIO as GPIO


class Motor(object):
    _DEBUG = False
    _DEBUG_INFO = "ln298n motor module"
    def __init__(self, control_pin_1, control_pin_2, debug=False):

        self._DEBUG = debug
        if self._DEBUG:
            print(self._DEBUG_INFO, "Debug on")
        self.control_pin_1 = control_pin_1
        self.control_pin_2 = control_pin_2
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        if self._DEBUG:
            print(
                self._DEBUG_INFO,
                "setup motor pin number at",
                control_pin_1,
                control_pin_2,
            )
        GPIO.setup(self.control_pin_1, GPIO.OUT)
        GPIO.setup(self.control_pin_2, GPIO.OUT)

    @property
    def debug(self, debug):
        return self._DEBUG

    def forward(self):
        """ Set the motor direction to forward """
        GPIO.output(self.control_pin_1, True)
        GPIO.output(self.control_pin_2, False)

        if self._DEBUG:
            print(self._DEBUG_INFO, "Motor moving forward")

    def backward(self):
        """ Set the motor direction to backward """
        GPIO.output(self.control_pin_1, False)
        GPIO.output(self.control_pin_2, True)
        if self._DEBUG:
            print(self._DEBUG_INFO, "Motor moving backward")

    def stop(self):
        GPIO.output(self.control_pin_1, False)
        GPIO.output(self.control_pin_2, False)
        if self._DEBUG:
            print(self._DEBUG_INFO, "Motor stoped")

    @debug.setter
    def debug(self, debug):
        """ Set if debug information shows """
        if debug in (True, False):
            self._DEBUG = debug
        else:
            raise ValueError(
                'debug must be "True" (Set debug on) or "False" (Set debug off), not "{0}"'.format(
                    debug
                )
            )

        if self._DEBUG:
            print(self._DEBUG_INFO, "Set debug on")
        else:
            print(self._DEBUG_INFO, "Set debug off")
            # added comment


def test():
    print("testing motor module")
    import time

    delay = 3

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)

    motor_a = Motor(8, 10,True)

    motor_a.forward()
    time.sleep(delay)

    motor_a.backward()
    time.sleep(delay)

    GPIO.cleanup()


if __name__ == "__main__":
    test()
