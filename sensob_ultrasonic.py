__author__ = 'Mads'
import ultrasonic

class SensobUltrasonic(object):
    def __init__(self):
        self.sensor = ultrasonic.Ultrasonic()
        self.value = self.sensor.get_value()

    def update(self):
        self.value = self.sensor.update()

    def get_value(self):
        return self.value

    def reset(self):
        return