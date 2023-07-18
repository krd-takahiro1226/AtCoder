import math
N = int(input())
N_sqrt = math.sqrt(N)
ans = []

for i in range(1,int(N_sqrt)+1):
    val = N / i
    if val.is_integer():
        ans.append(val+i)

print(int(min(ans))-2)
