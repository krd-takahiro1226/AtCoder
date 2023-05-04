import numpy as np
N = int(input())
H = list(map(int,input().split()))
H = np.array(H)
print(np.argmax(H)+1)
