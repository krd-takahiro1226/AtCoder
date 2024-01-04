N = int(input())
C = []
A = []
for _ in range(N):
    C.append(int(input()))
    A.append(set(map(int,input().split())))
X = int(input())

ind = 0
bet_num = 0
ans = []

for Ai in A:
    if X in Ai:
        if bet_num == 0 or C[ind] < bet_num:
            bet_num = C[ind]
            ans = []
            ans.append(ind+1)
        elif C[ind] == bet_num:
            ans.append(ind+1)
    ind += 1
print(len(ans))
print(*ans)
