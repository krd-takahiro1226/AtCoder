import math
a,b,d = map(int,input().split())

if a != 0 or b != 0:
    side_len = math.sqrt(a**2 + b**2)
    cos_origin = a / side_len
    sin_origin = b / side_len
    origin_degree = math.degrees(math.acos(cos_origin))
    if (a >= 0 and b < 0) or (a < 0 and b < 0):
        origin_degree = 360 - origin_degree
    next_degree = origin_degree + d
    a_next = side_len * math.cos(math.radians(next_degree))
    b_next = side_len * math.sin(math.radians(next_degree))
    print(a_next,b_next)
else:
    print(0,0)
