#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



ev3 = EV3Brick()

motorI= Motor(Port.B)
motorE= Motor(Port.C)
sensor=UltrasonicSensor(Port.S4)

robot= DriveBase(motorI,motorE, wheel_diameter=56, axle_track=54)
speed=75
while True:
    ev3.light.on(Color.GREEN)
    motorI.stop()
    motorE.run(150)
    
    if sensor.distance()<=400:
        robot.stop()
        ev3.light.on(Color.YELLOW)
        ev3.speaker.beep()
            
        wait(1000)