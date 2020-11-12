#!/usr/bin/env pybricks-micropython

"""
Gruppe 6, dytteleken.
Har forstatt problemer med at den ikke kjører på rett linje.
Finn en måte å sette fast startplass.
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, SoundFile
from pybricks.tools import wait
from random import randint

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)
belt_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)


# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55 , axle_track=157)#103 innerside

### FUNKSJONER FOR BELTE.
def beltUp(x,y):
    belt_motor.run_time(x, y)
beltUp(-1050, 3000)


# Go forward x distance.
robot.straight(750)

#Jukking
for i in range(0,25):
    robot.straight(30) #Originalt 15
    robot.straight(-20) #Originalt -5

#Rygg til startpos.
robot.straight(-800)    

#Belte ned
def beltDown(x,y):
    belt_motor.run_time(x,y)
beltDown(1050,3000)
