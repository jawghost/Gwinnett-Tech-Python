#101Computing.net/projection-motion-formula
#edited version is williams_j_projectilemotion.py
import math
from processing import *

x0 = 0
y0 = 400
gravity = 9.81 #g
angle = 70     #theta
velocity = 80  #v0

vx = velocity * math.cos(math.radians(angle))
vy = velocity * math.sin(math.radians(angle))
t = 0

def setup():
    strokeWeight(10)
    frameRate(100)
    size(400,400)

def throwBall():
    global x0, y0, gravity, vx, vy, t
    background(100)
    fill(0,121,184)
    stroke(255)

    t += 0.02
    x = x0 + vx*t
    y = y0 -(vy*t - 0.5*gravity*t**2)

    ellipse(x,y,30,30)


draw = throwBall 
run()
