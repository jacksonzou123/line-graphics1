from display import *

#A = deltaY
#B = -1 * deltaX
#C = deltaX + y-intercept
def draw_line( x0, y0, x1, y1, screen, color ):
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    if x1 < x0:
        x0, x1, y0, y1 = x1, x0, y1, y0

    deltaX = x1 - x0
    deltaY = y1 - y0

    if deltaX == 0:
        if y0 > y1:
            y0, y1 = y1, y0
        for y in range(y0, y1 + 1):
            plot(screen, color, x0, y)
        return 0

    slope = deltaY*1.0/deltaX
    A = deltaY
    B = -1 * deltaX

    if slope >= 0 and slope <= 1: #octant 1
        d = 2 * A + B
        x, y = x0, y0
        A *= 2
        B *= 2
        while x <= x1:
            if d > 0:
                y+=1
                d+=B
            x+=1
            d+=A
            #print(x, y)
            plot(screen, color, x, y)
    if slope > 1:
        d = A + 2 * B
        x, y = x0, y0
        A *= 2
        B *= 2
        while y <= y1:
            if d < 0:
                x+=1
                d+=A
            y+=1
            d+=B
            #print(x,y)
            plot(screen, color, x, y)
    if slope >= -1 and slope < 0:
        d = A * 2 - B
        x, y = x0, y0
        A *= 2
        B *= 2
        while x <= x1:
            if d > 0:
                y-=1
                d+=B
            x+=1
            d-=A
            #print(x, y)
            plot(screen, color, x, y)
    if slope < -1:
        d = A - 2 * B
        x, y = x0, y0
        A *= 2
        B *= 2
        while y >= y1:
            if d < 0:
                x+=1
                d-=A
            y-=1
            d+=B
            #print(x, y)
            plot(screen, color, x, y)
