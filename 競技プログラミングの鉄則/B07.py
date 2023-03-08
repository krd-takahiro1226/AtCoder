T = int(input())
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

clerk_num = [0] * 2 * (T+2)
ans = [0] * 2 * (T+2)

for i,j in LR:
    clerk_num[2*i] += 1
    clerk_num[2*j+1] -= 1
clerk_num.pop()

for i in range(1,2*(T+1)):
    ans[i] = clerk_num[i-1] + ans[i-1]
ans.remove(0)

for i in range(1,len(ans) - 2,2):
    print(ans[i])
