from cmath import sqrt
import json
from re import X

x0 = 1; y0 = 2; x1 = 2; y1 = 3; x2 = 1; y2 = 2; x3 = 2; y3 = 3


arrayy

print(pointList[0])

def pointLocation(x):
    hey = x
    return hey


def distanceBetweenPoints(xi, yi, xj, yj):
    print(xi + yi + xj + yj)
    
    delta = sqrt((xi-xj)**2 + (yi-yj)**2)
    pointLocation(xi)

    return delta, yi

result = distanceBetweenPoints(x0, y0, x1, y1)

value = result[1]
print(result)
print(type(result))
print(value)


# algortithm
# input:
'''
BEFORE THE INPUT OF COMPUTERS IS GIVEN TO US, BE AWARE IT IS SORTED 
INPUT:
    communicated_computers_total: 2D array of the triple data 
    computer_infected: infected comp at time x
    computers_contaminated_list: list of conatimnated comps at time y
 '''

# define the infected computer 
computer_infected = [1]
communicated_computers_total = \
[comm_computers_1[1,2,time_1],comm_computers_2[2,3,time_2],... comm_computers_m[3,...n,time_n]]

infection_start_time = [0]
computers_contaminated_list = [0]
increment_m = 0

# needs to find a virus infected computer 
while increment_m < length(computers_contaminated_list):
    for s = 0 in length(communicated_computers_total):
        if computer_infected in communicated_computers_total[s][0]:
            add communicated_computers_total[s][0] to computers_contaminated_list
            add [s][2] to infection_start_time
        if computer_infected in communicated_computers_total[s][1]:
            add communicated_computers_total[s][1] to computers_contaminated_list
            add [s][2] to infection_start_time
        increment_m += 1



