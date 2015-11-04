import time

import BBCON
import arbitrator

import motob_camera
import motob_wheels

import camera_behavior
import CollisionBehavior
import MovementBehavior

import sensob_reflectance
import sensob_ultrasonic

from zumo_button import ZumoButton

arb = arbitrator.Arbitrator()
bbcon = BBCON.BBCON(arb)

sensob_ref = sensob_reflectance.SensobReflectance()
sensob_ultr = sensob_ultrasonic.SensobUltrasonic()

bbcon.add_sensob(sensob_ref)
bbcon.add_sensob(sensob_ultr)

bbcon.add_motob(motob_camera.MotobCamera())
bbcon.add_motob(motob_wheels.MotobWheels())

bbcon.add_behavior(camera_behavior.CameraBehavior(sensob_ultr))
bbcon.add_behavior(CollisionBehavior.CollisionBehavior(sensob_ref))
bbcon.add_behavior(MovementBehavior.MovementBehavior())


ZumoButton().wait_for_press()

for i in range(0, 100):
	bbcon.run_one_timestep()
	time.sleep(0.1)