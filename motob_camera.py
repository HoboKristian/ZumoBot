__author__ = 'Kristian'
import camera

class MotobCamera(object):
    def __init__(self):
        self.camera = camera.Camera()
        self.value = None
        self.duration = 0.5
        self.img = None

    def update(self, camera_action):
        self.value = camera_action
        self.operationalize()

    def operationalize(self):
        if self.value == True:
            self.img = self.camera.update()
            self.img.save('pls.jpeg', 'jpeg')

    def set_duration(self, duration):
        if duration > 0:
            self.duration = duration
        else:
            raise ValueError("Duration can't be negative.")