D = int(input())
N = int(input())
LR = [list(map(int,input().split())) for _ in range(N)]
attend = [0] * (D+2)
ans = [0] * (D+1)
cnt = 1

for lr in LR:
    attend[lr[0]] += 1
    attend[lr[1]+1] -= 1

for i in range(D):
    ans[i+1] = ans[i] + attend[cnt]
    cnt += 1
ans.pop(0)
for i in ans:
    print(i)
