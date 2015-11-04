import motors

class MotobWheels(object):
    def __init__(self):
        self.motors = motors.Motors()
        self.value = []
    
    def update(self, value):
        self.value = value

    def operationalize(self):
        if self.value != None:
            direction = self.value[0]
            degrees = self.value[1]
            if direction == 'L':
                if degrees == 90:
                    self.motors.set_value([0.6, 0.6], dur=0.5)
                elif degrees == 180:
                    self.motors.set_value([-0.6, 0.6], dur=0.5)
            elif direction == 'R':
                if degrees == 90:
                    self.motors.set_value([0.6, -0.6], dur=1)
                elif degrees == 180:
                    self.motors.set_value([0.6, -0.6], dur=1)
            elif direction == 'F':
                self.motors.set_value([1, 1])
            elif direction == 'B':
                self.motors.set_value([-1, -1])
        else:
            self.motors.set_value([0, 0])

