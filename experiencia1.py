#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
sensor = UltrasonicSensor(Port.S4)
motorI = Motor(Port.B)
motorD = Motor(Port.C)
robot=DriveBase(motorI, motorD, wheel_diameter=56, axle_track=114)
speed = 75
while True:
    robot.drive(speed,0)
    if sensor.distance()<=200:
        robot.stop()
        motorD.run(speed)
        wait(2000)





