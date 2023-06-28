N, A, B = map(int,input().split())
tile = [[False] * N for _ in range(N)]
tile[0] = [0] * N
ans = [[0] * B * N for _ in range(A*N)]

for i in range(N):
    for j in range(N):
        if tile[i][j] == 0 and i+1 < N:
            tile[i+1][j] = 1
        elif tile[i][j] == 1 and i+1 < N:
            tile[i+1][j] = 0
        if tile[i][j] == 0 and j+1 < N:
            tile[i][j+1] = 1
        elif tile[i][j] == 1 and j+1 < N:
            tile[i][j+1] = 0

for k in range(A*N):
    for l in range(B*N):
        if tile[k//A][l//B] == 0: # k//Aとしているのは「0~A-1」までは同じ色なので、tileのインデックスとして同じ値を指定したいから
            ans[k][l] = "."
        else:
            ans[k][l] = "#"

for g in ans:
    print(*g,sep='')
