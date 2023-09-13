from visual import *
ball = sphere(pos=(-5,0,0), radius=0.5, color=color.cyan)
ball.trail = curve(color=ball.color)
wallR = box(pos=(6,0,0), size=(0.2,12,12), color=color.green)
wallL = box(pos=(-6,0,0), size=(0.2,12,12), color=color.green)
wallUP = box(pos=(0,-6,0), size=(12.0,0,12), color=color.blue)
wallD = box(pos=(0,6,0), size=(12.0,0,12), color=color.blue)
wallBA = box(pos=(0,0,-6), size=(12.12,12,0), color=color.red)
# wallBAK = box(pos=(0,0,6), size=(12.12,12,0), color=color.white)
ball.velocity = vector(25,5,0)
deltat = 0.005
t = 0
vscale = 0.1
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.yellow)
scene.autoscale = False
while t < 3:
    rate(100)
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
    elif ball.pos.x < wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
    elif ball.pos.x > wallUP.pos.x:
        ball.velocity.x = -ball.velocity.x
    elif ball.pos.x < wallD.pos.x:
        ball.velocity.x = -ball.velocity.x
    elif ball.pos.x < wallBA.pos.x:
        ball.velocity.x = -ball.velocity.x
    # elif ball.pos.x < wallBAK.pos.x:
        # ball.velocity.x = -ball.velocity.x
    ball.pos = ball.pos + ball.velocity*deltat
    t = t + deltat
    ball.trail.append(pos=ball.pos)
