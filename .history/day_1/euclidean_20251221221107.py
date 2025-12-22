import math 

p1 = [2,3]
p2 = [10,8]

delta_x = p2[0] - p1[0]
delta_y = p2[1] - p1[1]

squared_dist = delta_x**2 + delta_y**2

distance = math.sqrt(squared_dist)

print(distance)