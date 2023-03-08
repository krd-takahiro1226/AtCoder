import numpy as np
N = int(input())
A = list(map(int, input().split()))
Alice = []
Bob = []

for i in range(N // 2 + 1):
    if (len(A) == 0):
        break
    else:
        Max = max(A)
        # Max_ind = A.index(Max)
        Max_ind = np.argmax(A)
        Alice.append(Max)
        del A[Max_ind]
        if (len(A) == 0):
            break
        else:
            Max = max(A)
            # Max_ind = A.index(Max)
            Max_ind = np.argmax(A)
            Bob.append(Max)
            del A[Max_ind]
Alice_sum = sum(Alice)
Bob_sum = sum(Bob)
print(Alice_sum - Bob_sum)
