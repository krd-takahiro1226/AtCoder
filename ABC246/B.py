import math
A, B = map(int,input().split())
if A != 0:
    tilt = B / A
    x = math.sqrt(1.0 / (1 + tilt ** 2))
    y = tilt * x
    print(x,y)
else:
    x = 0
    y = 1.0
    print(x,y)
