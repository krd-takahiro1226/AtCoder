import numpy as np
N, D = map(int,input().split())
T = list(map(int,input().split()))
T_np = np.array(T)
cnt = 0
ans = False
T_diff = np.diff(T_np)
for i in T_diff:
    cnt += 1
    if i <= D:
        print(T[cnt])
        ans = True
        break
    else:
        pass
if ans == True:
    pass
else:
    print(-1)
