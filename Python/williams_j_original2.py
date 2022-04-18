#101Computing.net/projection-motion-formula
#edited version is williams_j_projectilemotion2.py
import math
from processing import *

x = 0
y = 400
gravity = 9.81 #g
angle = 70     #thera
velocity = 60  #v0

vx = velocity * math.cos(math.radians(angle))
vy = velocity * math.sin(math.radians(angle))
dt = 0.02

def setup():
    strokeWeight(10)
    frameRate(100)
    size(400,400)

def throwBall():
    global x, y, gravity, vx, vy, dt
    background(100)
    fill(0,121,184)
    stroke(255)

    x = x + vx * dt
    y = y - vy * dt
    vy = vy - 0.5 * gravity * dt
    
    ellipse(x,y,30,30)


draw = throwBall 
run()
