import sensob_ultrasonic

class CameraBehavior(object):
	def __init__(self):
		self.ultrasonic = sensob_ultrasonic.SensobUltrasonic()
		self.value = 0

	def update(self):
		if self.ultrasonic.get_value() <= 10:
			self.value = 0.9
		else:
			self.value = 0

	def get_wheel_value(self):
		return None

	def get_camera_value(self):
		return True;