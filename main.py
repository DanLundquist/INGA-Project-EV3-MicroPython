!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
ev3 = EV3Brick()
#test_motor = Motor(Port.B,Port.A)
test_motor = Motor(Port.A)

ev3.speaker.beep()
#test_motor.run_target(500,360)
test_motor.run_target(500,360)
ev3.speaker.beep(1000,500)

