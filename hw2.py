import numpy as np

def neighbours(xc, yc, x, y):
    return [(xc+x, yc+y),
            (xc-x, yc+y),
            (xc+x, yc-y),
            (xc-x, yc-y),
            (xc+y, yc+x),
            (xc-y, yc+x),
            (xc+y, yc-x),
            (xc-y, yc-x)]

# Function for circle-generation
# using Bresenham's algorithm

def get_circle_points(xc, yc, r):
    yield (xc, yc)

    for i in range(r+1):
        for p in get_circle_points_outer(xc, yc, i):
            yield p

def get_circle_points_outer(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    res = []
    
    res.append(neighbours(xc, yc, x, y))
    while (y >= x):
        # for each pixel we will
        # draw all eight pixels
         
        x+=1
 
        # check for decision parameter
        # and correspondingly
        # update d, x, y
        if (d > 0):
            y-=1
            d = d + 4 * (x - y) + 10;
        else:
            d = d + 4 * x + 6;
        res.append(neighbours(xc, yc, x, y))
        
    return list(np.reshape(res, (-1, 2)))