import math
num=int(input())
length=float(input())
apothem=float(((length)/2*math.tan(math.pi/num)))
area=(num*length*apothem)/2
print(round((area)))
