import math
N = int(input())
N_str = str(N)
N_ln = len(N_str)

if N_ln <= 3:
    print(N)
else:
    print(math.floor(N//10**(N_ln-3))*10**(N_ln-3))
