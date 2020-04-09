import backwheels as backwheels
import time
import re


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

def test():
    str = 'S55'
    print( bool(re.match("^S\d{2}$",str)))
    speed = int(str[1:3])
    print (speed)


if __name__ == '__main__':
	#ride_a_loop()
    test()