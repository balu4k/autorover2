import backwheels as backwheels
import time


def ride_a_loop():
    back_wheels = backwheels.BackWheels()
    back_wheels.debug = True

    back_wheels.forward()
    time.sleep(3)

    back_wheels.left_turn()
    time.sleep(3)

    back_wheels.forward()
    time.sleep(3)

    back_wheels.left_turn()
    time.sleep(3)

    back_wheels.forward()
    time.sleep(3)

    back_wheels.left_turn()
    time.sleep(3)

    back_wheels.forward()
    time.sleep(3)

    back_wheels.left_turn()
    time.sleep(3)

    back_wheels.stop()

if __name__ == '__main__':
	ride_a_loop()