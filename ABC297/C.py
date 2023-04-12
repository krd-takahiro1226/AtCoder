H,W = map(int,input().split())
S = []
for _ in range(H):
    S.append(list(input()))
for i in range(H):
    for j in range(W):
        if  j+1 < W and S[i][j] == S[i][j+1] and S[i][j] == "T":
            S[i][j] = "P"
            S[i][j+1] = "C"
for i in S:
    print(*i,sep='')
