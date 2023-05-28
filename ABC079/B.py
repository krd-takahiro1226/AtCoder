N = int(input())
L0 = 2
L1 = 1
i = 2
L = []
L.append(L0)
L.append(L1)

while(len(L) != N+1):
    L.append(L[i-1]+L[i-2])
    i += 1

print(L[N])
