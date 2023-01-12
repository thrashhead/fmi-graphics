def neighbours(xc, yc, x, y):
    yield (xc+x, yc+y)
    yield (xc-x, yc+y)
    yield (xc+x, yc-y)
    yield (xc-x, yc-y)
    yield (xc+y, yc+x)
    yield (xc-y, yc+x)
    yield (xc+y, yc-x)
    yield (xc-y, yc-x)

# Function for circle-generation
# using Bresenham's algorithm
def get_circle_points(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    yield list(neighbours(xc, yc, x, y))
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
        yield list(neighbours(xc, yc, x, y))