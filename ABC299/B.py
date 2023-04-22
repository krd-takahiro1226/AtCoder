N, T = map(int,input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))
C_set = set(C)
value = 0

if T in C_set:
    for i in range(N):
        if C[i] == T:
            if R[i] > value:
                value = R[i]
                ind = i+1
else:
    color = C[0]
    for i in range(N):
        if C[i] == color:
            if R[i] > value:
                value = R[i]
                ind = i+1

print(ind)
