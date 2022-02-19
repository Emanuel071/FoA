from cmath import sqrt

x0 = 1; y0 = 2; x1 = 2; y1 = 3; x2 = 1; y2 = 2; x3 = 2; y3 = 3


arrayy

print(pointList[0])



def distanceBetweenPoints(xi, yi, xj, yj):
    print(xi + yi + xj + yj)
    
    delta = sqrt((xi-xj)**2 + (yi-yj)**2)

    return delta

result = distanceBetweenPoints(x0, y0, x1, y1)

print(result)



