#101Computing.net/projection-motion-formula
#original is original1.py
import math
from processing import *

x0 = 0
y0 = 400
gravity = 20 #change from 9.81 to 20
angle = 90     #changed from 70 to 90
velocity = 70  #changed from 50 to 70

vx = velocity * math.cos(math.radians(angle))
vy = velocity * math.sin(math.radians(angle))
t = 0

def setup():
    strokeWeight(10)
    frameRate(100)
    size(700,700) #changed to 700

def throwBall():
    global x0, y0, gravity, vx, vy, t
    background(100)
    fill(0,121,184)
    stroke(255)

    t += 0.01 #changed to 0.01
    x = x0 + vx*t
    y = y0 -(vy*t - 0.5*gravity*t**2)

    ellipse(x,y,30,30)


draw = throwBall 
run()
