H, W = map(int,input().split())
S = [list(input()) for _ in range(H)]
start_ind = []
ans = []

for i in range(H):
    for j in range(W):
        if S[i][j] == "#" and len(start_ind) == 0:
            start_ind = [i,j]
        else:
            if S[i][j] == "#":
                end_ind = [i,j]

for k in range(start_ind[0],end_ind[0]+1):
    for l in range(start_ind[1],end_ind[1]+1):
        if S[k][l] == ".":
            ans = [k+1,l+1]
if len(ans) == 0:
    if S[start_ind[0]][start_ind[1]-1] == "." and S[start_ind[0]+1][start_ind[1]-1] == "#":
        ans = [start_ind[0]+1,start_ind[1]]
    elif S[end_ind[0]][end_ind[1]+1] == "." and S[end_ind[0]-1][end_ind[1]+1] == "#":
        ans = [end_ind[0]+1,end_ind[1]+2]
print(*ans)
