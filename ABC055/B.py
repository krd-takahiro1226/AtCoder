import math
N = int(input())
ans = math.factorial(N)
wari = 10**9 + 7
print(ans % wari)
