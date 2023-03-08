import numpy as np
import copy
N = int(input())
A = list(map(int, input().split()))

A_diff_num = copy.copy(A) # 理想と所持を比較して、持っていないのが何巻かをリストで保持、このリストの1要素目から交換していく
A_have_num = list(set(A)) # 持っている巻(重複して持っている分はカウントしない)
Shortage_num = N - len(A_have_num) # 売ることができる巻数
Ideal = [0] * N

for i in range(N):
    Ideal[i] = i + 1

Common = list(set(A) & set(Ideal)) # 理想と所持を比較して共通している巻をリストで保持
for j in Common:
    A_diff_num.remove(j)

if Shortage_num >= 2:
    for k in range(Shortage_num // 2):
        pass
else:
    pass


# A = [3,1,4,5,2]
# A.sort()
# print(A)
