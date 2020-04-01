import backwheels as backwheels
from hcsr04.hcsro4 import Echo

def avoid_obstacle_and_drive():
    back_wheels = backwheels.BackWheels()
    back_wheels.debug = True

    """ Define GPIO pin constants """
    TRIGGER_PIN = 17
    ECHO_PIN = 18
    """ Calibrate sensor with initial speed of sound m/s value """
    SPEED_OF_SOUND = 343
    """ Initialise Sensor with pins, speed of sound. """
    echo = Echo(TRIGGER_PIN, ECHO_PIN, SPEED_OF_SOUND)
    try:
        while true:
            if(echo.is_ready):
                distance = echo.read('cm',1)
                if(distance > 30):
                    back_wheels.forward()
                elif:
                    back_wheels.left_turn()
            elif:
                back_wheels.stop()

    finally:
        back_wheels.stop()
        echo.stop()

if __name__ == '__main__':
	ride_a_loop()