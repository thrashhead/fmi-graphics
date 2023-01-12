# Python3 program for Bresenhams Line Generation
def plotPixel(x1, y1, x2, y2, dx, dy, decide):
   
  # pk is initial decision making parameter
  # Note:x1&y1,x2&y2, dx&dy values are interchanged
  # and passed in plotPixel function so
  # it can handle both cases when m>1 & m<1
  pk = 2 * dy - dx
   
  # for (int i = 0; i <= dx; i++) {
  for i in range(0,dx+1):
    yield (x1, y1)
     
    # checking either to decrement or increment the
    # value if we have to plot from (0,100) to (100,0)
    if(x1<x2):
      x1 = x1 + 1
    else:
      x1 = x1 - 1
    if (pk < 0):
       
      # decision value will decide to plot
      # either  x1 or y1 in x's position
      if (decide == 0):
         
        # putpixel(x1, y1, RED);
        pk = pk + 2 * dy
      else:
         
        #(y1,x1) is passed in xt
        # putpixel(y1, x1, YELLOW);
        pk = pk + 2 * dy
    else:
      if(y1<y2):
        y1 = y1 + 1
      else:
        y1 = y1 - 1
         
      # if (decide == 0):
      #   # putpixel(x1, y1, RED)
      # else:
      #   #  putpixel(y1, x1, YELLOW);
      pk = pk + 2 * dy - 2 * dx
 
# Driver code
x1 = 100
y1 = 110
x2 = 125
y2 = 120
 
def get_line_pixels(x1, y1, x2, y2): 

  dx = abs(x2 - x1)
  dy = abs(y2 - y1)
  
  # If slope is less than one
  if (dx > dy):
    # passing argument as 0 to plot(x,y)
    return list(plotPixel(x1, y1, x2, y2, dx, dy, 0))
  
  # if slope is greater than or equal to 1
  else:
    # passing argument as 1 to plot (y,x)
    return list(plotPixel(y1, x1, y2, x2, dy, dx, 1))