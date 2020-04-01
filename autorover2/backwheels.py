from ln298n.motor import Motor
import filedb as filedb
import RPi.GPIO as GPIO


class BackWheels(object):
	''' Back wheels control class '''
	Motor_A1 = 14  #board pin 08
	Motor_A2 = 15  #board pin 10
	Motor_B1 = 23  #board pin 16
	Motor_B2 = 24  #board pin 18

	_DEBUG = False
	_DEBUG_INFO = 'DEBUG "backwheels.py":'

	def __init__(self, debug=False, db="config"):
        #self._DEBUG = debug
		self.forward_A = True
		self.forward_B = True

		self.db = filedb.FileDB(db=db)

		self.forward_A = int(self.db.get('forward_A', default_value=1))
		self.forward_B = int(self.db.get('forward_B', default_value=1))

		self.left_wheel = Motor(self.Motor_A1, self.Motor_A2, self.debug)
		self.right_wheel = Motor(self.Motor_B1,self.Motor_B2, self.debug)

	def forward(self):
		''' Move both wheels forward '''
		self.left_wheel.forward()
		self.right_wheel.forward()
		if self._DEBUG:
			print(self._DEBUG_INFO, 'Running both wheels forward')

	def backward(self):
		''' Move both wheels backward '''
		self.left_wheel.backward()
		self.right_wheel.backward()
		if self._DEBUG:
			print(self._DEBUG_INFO, 'Running both wheels backward')

	def left_turn(self):
		self.left_wheel.forward()
		self.right_wheel.backward()
		if self._DEBUG:
			print(self._DEBUG_INFO, 'Running left turn')

	def right_turn(self):
		self.left_wheel.backward()
		self.right_wheel.forward()
		if self._DEBUG:
			print(self._DEBUG_INFO, 'Running right turn')

	def stop(self):
		''' Stop both wheels '''
		self.left_wheel.stop()
		self.right_wheel.stop()
		if self._DEBUG:
			print(self._DEBUG_INFO, 'Stop')

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

	back_wheels = BackWheels()
	back_wheels.debug = True
	DELAY = 3
	try:
		back_wheels.forward()
		time.sleep(DELAY)

		back_wheels.backward()
		time.sleep(DELAY)
	except KeyboardInterrupt:
		print("KeyboardInterrupt, motor stop")
		back_wheels.stop()
	finally:
		print("Finished, back wheels stoped")
		back_wheels.stop()

if __name__ == '__main__':
	test()

