__author__ = 'Mads'
import time

class BBCON(object):
    def __init__(self, arb=None):
        self.behaviors = []
        self.active_behaviors = []
        self.inactive_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = arb

        self.halt_time = 1

    def run_one_timestep(self):
        self.update_sensobs()
        self.update_behaviors()

        self.arbitrator.do_best_action(self.active_behaviors)

    def halt(self):
        time.sleep(self.halt_time)

    def update_sensobs(self):
        for sensob in self.sensobs:
            sensob.update()

    def update_behaviors(self):
        for behavior in self.active_behaviors:
            behavior.update()

    def add_motob(self, motob):
        self.motobs.append( motob )

    def add_behavior(self, behavior):
        self.behaviors.append( behavior )
        self.inactive_behaviors.append( behavior )

    def add_sensob(self, sensob):
        self.sensobs.append( sensob )

    def activate_behavior(self, behavior):
        self.active_behaviors.append( behavior )
        self.inactive_behaviors.remove( behavior )

    def deactivate_behavior(self, behavior ):
        self.active_behaviors.remove( behavior )
        self.inactive_behaviors.append( behavior )