import math
a, b, x = map(int,input().split())

hgt = x / (a**2)

if 2 * hgt >= b:
    tall = 2*(b - hgt)
    ans = math.degrees(math.atan(tall / a))
else:
    width = a - 2*x / (a*b)
    ans = math.degrees(math.atan(a*b**2/(2*x)))

print(ans)
