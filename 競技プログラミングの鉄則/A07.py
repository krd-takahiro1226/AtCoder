D = int(input())
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

attend = [0] * (D+2)
ans = [0] * (D+1)

for i,j in LR:
    attend[i] += 1
    attend[j+1] -= 1

for i in range(1,D+1):
    ans[i] = ans[i-1] + attend[i]

ans.remove(0)

for j in ans:
    print(j)
