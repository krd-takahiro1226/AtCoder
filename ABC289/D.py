N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
X = int(input())
ans = [0] * (10**6)
ans[0] = 1
cnt = 0
B_Set = set(B)

for _ in range(X):
# 1試行で到達する可能性がある段を1に変更
    if ans[cnt] == 1:
        for i in A:
            if cnt not in B_Set:
                ans[cnt + i] = 1
            else:
                pass
    elif ans[cnt] == 0:
            pass
    cnt += 1
# print(ans)

if ans[X] == 1:
    print("Yes")
else:
    print("No")
