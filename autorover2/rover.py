from pca9685.motor import Motor 
import filedb as filedb
import RPi.GPIO as GPIO
import Adafruit_PCA9685
import time


class Rover(object):
	''' Back wheels control class '''
	
	# Left Motor bus numbers
	Motor_L_BUS_S = 0  
	Motor_L_BUS_1 = 1
	Motor_L_BUS_2 = 2  
	
	#Right motor bus numbers
	Motor_R_BUS_1 = 4  
	Motor_R_BUS_2 = 3  
	Motor_R_BUS_S = 5


	_DEBUG = False
	_DEBUG_INFO = 'DEBUG "rover.py":'

	def __init__(self, debug=False, db="config"):
        #self._DEBUG = debug
		self.forward_R = True
		self.forward_L = True
		#self.debug = debug

		self.db = filedb.FileDB(db=db)

		self.forward_A = int(self.db.get('forward_A', default_value=1))
		self.forward_B = int(self.db.get('forward_B', default_value=1))

		self.left_wheel = Motor(self.Motor_L_BUS_1, self.Motor_L_BUS_2, self.Motor_L_BUS_S, debug=self.debug)
		self.right_wheel = Motor(self.Motor_R_BUS_1, self.Motor_R_BUS_2, self.Motor_R_BUS_S, debug=self.debug)


	def turn(self,angle):
		if angle < 75:
			self.right_turn()
		elif angle > 100 :
			self.left_turn()
		else:
			self.forward()

	def forward(self):
		''' Move both wheels forward '''
		#self.speed(50)
		self.left_wheel.forward()
		self.right_wheel.forward()
		if self._DEBUG:
			print(self._DEBUG_INFO, 'Running both wheels forward')

	def reverse(self):
		''' Move both wheels backward '''
		#self.speed(50)
		self.left_wheel.reverse()
		self.right_wheel.reverse()
		if self._DEBUG:
			print(self._DEBUG_INFO, 'Running both wheels backward')

	def left_turn(self):

		#self.speed(100)
		self.left_wheel.forward()
		self.right_wheel.reverse()
		if self._DEBUG:
			print(self._DEBUG_INFO, 'Running left turn')

	def right_turn(self):
		#self.speed(100)
		self.left_wheel.reverse()
		self.right_wheel.forward()
		if self._DEBUG:
			print(self._DEBUG_INFO, 'Running right turn')

	def stop(self):
		''' Stop both wheels '''
		self.left_wheel.stop()
		self.right_wheel.stop()
		if self._DEBUG:
			print(self._DEBUG_INFO, 'Stop')

	def speed(self, power):
		self.left_wheel.speed = power
		self.right_wheel.speed = power

	@property
	def debug(self):
		return self._DEBUG

	@debug.setter
	def debug(self, debug):
		''' Set if debug information shows '''
		if debug in (True, False):
			self._DEBUG = debug
		else:
			raise ValueError('debug must be "True" (Set debug on) or "False" (Set debug off), not "{0}"'.format(debug))

		if self._DEBUG:
			print(self._DEBUG_INFO, "Set debug on")
			self.left_wheel.debug = True
			self.right_wheel.debug = True
			#self.pwm.debug = True
		else:
			print(self._DEBUG_INFO, "Set debug off")
			self.left_wheel.debug = False
			self.right_wheel.debug = False
			#self.pwm.debug = False

	def ready(self):
		''' Get the back wheels to the ready position. (stop) '''
		if self._DEBUG:
			print(self._DEBUG_INFO, 'Turn to "Ready" position')
		self.stop()


def test():
	import time

	back_wheels = Rover()
	back_wheels.debug = True
	DELAY = 2
	try:
		print("Forward 50")
		#back_wheels.speed(50)
	
		# back_wheels.forward()
		# time.sleep(DELAY)

		# print("Forward 100")
		back_wheels.speed(25)
		# time.sleep(DELAY)

		back_wheels.forward()
		time.sleep(DELAY)
		back_wheels.right_turn()
		time.sleep(3)
		back_wheels.forward()
		time.sleep(DELAY)

		# back_wheels.speed(50)
		# back_wheels.left_turn()
		# time.sleep(DELAY)

		# back_wheels.right_turn()
		# time.sleep(DELAY)


	except KeyboardInterrupt:
		print("KeyboardInterrupt, motor stop")
		back_wheels.stop()
	finally:
		print("Finished, back wheels stoped")
		back_wheels.stop()

if __name__ == '__main__':
	test()

