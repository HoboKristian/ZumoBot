import motob_wheels
import motob_camera

class Arbitrator(object):
	def __init__(self):
		self.wheels = motob_wheels.MotobWheels()
		self.camera = motob_camera.MotobCamera()

	def do_best_action(self, behaviors):
		best_behavior = behaviors[0]
		for b in behaviors[1:]:
			if b.get_value() > best_behavior.get_value():
				best_behavior = b

		camera_value = best_behavior.get_camera_value()
		wheel_value = best_behavior.get_wheel_value()

		self.wheels.update(wheel_value)
		self.camera.update(camera_value)