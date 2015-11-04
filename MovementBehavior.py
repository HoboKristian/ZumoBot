class MovementBehavior(object):
    def __init__(self):
        self.value = 0.2
        self.wheel_value = ['F', 0]

    def update(self):
        return

    def get_value(self):
        return self.value

    def get_wheel_value(self):
        return self.wheel_value

    def get_camera_value(self):
        return False