N = int(input())
A = list(map(int,input().split()))
P = 0
pos = [0] * 4
tmp = [0] * 4

for i in range(N):
    pos[0] = 1
    for j in range(4):
        if pos[j] != 0:
            if j + A[i] <= 3:
                tmp[j+A[i]] = pos[j]
                pos[j] = 0
            else:
                P += pos[j]
    pos = tmp
    tmp = [0] * 4
print(P)
