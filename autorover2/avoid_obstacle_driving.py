import rover as rover
from hcsr04.hcsro4 import Measurement
import time

TRIGGER_PIN = 4
ECHO_PIN = 17
""" Calibrate sensor with initial speed of sound m/s value """
SPEED_OF_SOUND = 343
""" Initialise Sensor with pins, speed of sound. """

back_wheels = rover.Rover()
back_wheels.debug = True
back_wheels.speed(75)
echo = Measurement(TRIGGER_PIN, ECHO_PIN, 20, "metric")
try:

    while True:
        time.sleep(0.5)
        try:
            object_distance = echo.raw_distance(sample_size=1,sample_wait=0.3)
            print("Object distance is ", object_distance)


            if object_distance > 100:
                back_wheels.speed(100)
            else:
                back_wheels.speed(50)

            if  object_distance > 50 :
                # move forward
                back_wheels.forward()
            else:
                # turn rover to right
                back_wheels.speed(100)
                back_wheels.left_turn()
        except:
            back_wheels.stop()
except:
    back_wheels.stop()

finally:
    back_wheels.stop()

    time.sleep(1)
    