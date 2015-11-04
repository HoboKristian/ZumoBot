import reflectance_sensors

class SensobReflectance(object):
	def __init__(self):
		self.sensors = reflectance_sensors.ReflectanceSensors()
		self.value = []

	def get_value(self):
		return self.value

	def update(self):
		raw_value = self.sensors.get_value()
		min_value = raw_value[0]
		darkest_sensor = [0, 1]
		for i, value in enumerate(raw_value):
			if value < min_value:
				min_value = value
				darkest_sensor = [i, min_value]
		self.value = darkest_sensor