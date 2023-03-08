import numpy as np
N, A, B = map(int, input().split())
# N, A, B = 100, 4, 16
digits = np.arange(N + 1)
digits_1_N = digits[1:N + 1]
Sum = []
for i in digits_1_N:
    s = str(i)
    array = list(map(int, s))
    if (A <= sum(array) <= B):
        Sum.append(i)
print(sum(Sum))
