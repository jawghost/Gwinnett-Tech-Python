#101Computing.net/projection-motion-formula
#copy of original2.py
import math
from processing import *

x = 0
y = 400
gravity = 0 #changes gravity 9.81 to 0
angle = 10     #angle from 70 to 10
velocity = 50  #velocity from 60 to 50

vx = velocity * math.cos(math.radians(angle))
vy = velocity * math.sin(math.radians(angle))
dt = 0.1 #changed 0.02 to 0.1

def setup():
    strokeWeight(10)
    frameRate(100)
    size(1000,1000) #changes the size of grid from 400

def throwBall():
    global x, y, gravity, vx, vy, dt
    background(10)
    fill(0,7,184)
    stroke(255)

    x = x + vx * dt
    y = y - vy * dt
    vy = vy - 0.5 * gravity * dt
    
    ellipse(x,y,30,30)


draw = throwBall 
run()
