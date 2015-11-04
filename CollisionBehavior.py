class CollisionBehavior(object):
    def __init__(self, sensob, threshold=0.2):
        self.sensob = sensob
        self.value = 0
        self.threshold = threshold
        self.wheel_value = []

    def update(self):
        self.sensob.update()
        sensob_value = self.sensob.get_value()
        if sensob_value[1] < self.threshold:
            self.value = 1
            if sensob_value[0] < 3:
                self.wheel_value = ['R', 90]
            else:
                self.wheel_value = ['L', 90]
        else:
            self.value = 0

    def get_value(self):
        return self.value

    def get_wheel_value(self):
        return self.wheel_value

    def get_camera_value(self):
        return False