H, W = map(int,input().split())
S = [list(input()) for _ in range(H)]
moji = ["s","n","u","k","e"]
Di = [-1,-1,-1,0,0,1,1,1]
Dj = [-1,0,1,1,-1,-1,0,1]
ans = []

for i in range(H):
    for j in range(W):
        for l in range(8):
            si = i
            sj = j
            di = Di[l]
            dj = Dj[l]
            for k in range(5):
                if 0 <= si < H and 0 <= sj < W and S[si][sj] == moji[k]:
                    ans.append([si+1,sj+1])
                    si += di
                    sj += dj
                else:
                    ans = []
                    break
            # if k == 4 and len(ans) != 0:
            if k == 4:
                for g in ans:
                    print(*g)
