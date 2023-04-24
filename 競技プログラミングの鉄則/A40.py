import math
N = int(input())
A = list(map(int,input().split()))
A_set = set(A)
stick_num= []
ans = 0

for i in A_set:
    stick_num.append(A.count(i))
for j in stick_num:
    ans += math.comb(j,3)
print(ans)
