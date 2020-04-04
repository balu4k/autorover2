
from __future__ import division
import time
from pca9685 import PCA9685

class Motor(object):
    _DEBUG = False
    _DEBUG_INFO = "ln298n motor module"

    _FREQUENCY = 60
    _MAX_SPEED_PULSE = 4095
    _MIN_SPEED_PULSE = 0


    def __init__(self, forwardbus, reveresebus, speedbus, speed = 50, debug=False):
        self._DEBUG = debug
        self._pwm = PCA9685()
        self._pwm.set_pwm_freq(self._FREQUENCY)
        self._forwardbus = forwardbus
        self._reversebus = reveresebus
        self._speedbus = speedbus
        self._speed = speed
        self._speed_pulse = int(speed * self._MAX_SPEED_PULSE /100)

    def _debug_(self,message):
        if self._DEBUG:
            print(self._DEBUG_INFO,message)


    def forward(self):
        self._debug_("running motor in forward direction")
        self._pwm.set_pwm(self._speedbus, 0, self._speed_pulse)
        self._pwm.set_channel_on(self._forwardbus)
        self._pwm.set_channel_off(self._reversebus )

    
    def reverse(self):
        self._debug_("running motor in reverse direction")
        self._pwm.set_pwm(self._speedbus, 0, self._speed_pulse)
        self._pwm.set_channel_on(self._reversebus)
        self._pwm.set_channel_off(self._forwardbus)


    def stop(self):
        self._debug_("motor is stopped")
        self._pwm.set_pwm(self._speedbus, 0, self._MIN_SPEED_PULSE)
        self._pwm.set_channel_off(self._reversebus)
        self._pwm.set_channel_off(self._forwardbus)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
		self._debug_("Motor speed set to {0}".format(speed))
		self._speed = speed
		self._speed_pulse = int( self._speed * self._MAX_SPEED_PULSE / 100)
		self._pwm.set_pwm(self._speedbus, 0, self._speed_pulse )
		self._debug_("Motor speed pulse set to {0}".format(self._speed_pulse))



def test():
    motor = Motor(1,2,0,debug=True)

    motor.forward()
    time.sleep(2)

    motor.speed = 25
    time.sleep(2)

    motor.speed = 100
    time.sleep(2)


    motor.stop()
    time.sleep(2)


    motor.speed = 50
    motor.reverse()
    time.sleep(2)

    motor.speed = 75
    time.sleep(2)

    motor.speed = 100
    time.sleep(2)

    motor.stop()



if __name__ == "__main__":
    test()