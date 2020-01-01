# using the property that the median divides a right triangle into 2 isoceles triangles

import math
ab = int(input())
bc = int(input())
print(round(math.degrees(math.atan2(ab, bc))), '°', sep='')