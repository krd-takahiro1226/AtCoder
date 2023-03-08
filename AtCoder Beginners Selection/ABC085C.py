import numpy as np
N, Y = map(int, input().split())
# N, Y = 1, 5000
ANS = []
Y_box = []
# iが10000円，jが5000円，kが1000円に関するfor文
for i in range(N + 1):
    Y_cal1 = Y - 10000 * i
    if(Y_cal1 < 0):
        break
    for j in range(N - i + 1):
        Y_cal2 = Y_cal1 - 5000 * j
        if(Y_cal2 < 0):
            break
        Y_cal3 = Y_cal2 - 1000 * (N - i - j)
        if(Y_cal3 < 0):
            break
        Y_box.append(Y_cal3)
        if(Y_cal3 == 0):
            ans = []
            ans.append(i)
            ans.append(j)
            ans.append(N - i - j)
            ANS.append(ans)
if(np.count_nonzero(Y_box) == len(Y_box)):
    ANS.append([-1, -1, -1])
print(*ANS[0])
