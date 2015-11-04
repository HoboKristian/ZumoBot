import time

import BBCON

import motob_camera
import motob_wheels

import camera_behavior
import CollisionBehavior
import MovementBehavior

import sensob_reflectance
import sensob_ultrasonic

from zumo_button import ZumoButton

arb = Arbitrator()
bbcon = BBCON(arb)

bbcon.add_sensob(sensob_reflectance.SensobReflectance())
bbcon.add_sensob(sensob_ultrasonic.SensobUltrasonic())

bbcon.add_motob(motob_camera.MotobCamera())
bbcon.add_motob(motob_wheels.MotobWheels())

bbcon.add_behavior(camera_behavior.CameraBehavior())
bbcon.add_behavior(CollisionBehavior.CollisionBehavior())
bbcon.add_behavior(MovementBehavior.MovementBehavior())


ZumoButton().wait_for_press()

while 1:
	bbcon.run_one_timestep()
	time.sleep(0.1)