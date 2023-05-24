import random, time, ctypes
from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

width=1919
height=1079
xspeed= -10
yspeed= -10
walls=0
corners=0
xlist = [0,0,1919,1919]
ylist = [0,1079,0,1079]

   
def move():
    global xspeed, yspeed
    global x, y, walls, corners
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    nx = pt.x+xspeed
    ny = pt.y+yspeed
    if (nx >=width) or (nx<=0):
        xspeed= -xspeed
        walls+=1
        print(('='*60),'\nWall Hits:',walls)
        print('Corner Hits:',corners)
    if (ny >= height) or (ny<=0):
        yspeed = -yspeed
        walls+=1
        print(('='*60),'\nWall Hits:',walls)
        print('Corner Hits:',corners)
    for i in range(4):
        if pt.x==xlist[i] and pt.y==ylist[i]:
            corners+=1
            print(('='*60),'\nWall Hits:',walls)
            print('Corner Hits:',corners)
   
    ctypes.windll.user32.SetCursorPos(nx, ny)

ctypes.windll.user32.SetCursorPos(random.randint(0,1920),random.randint(0,1080))
try:
    while True:
        move()
        time.sleep(0.0001)
except KeyboardInterrupt:
    print('Stopped')
    pass
