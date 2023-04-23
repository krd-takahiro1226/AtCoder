D , N = map(int,input().split())
ans = [0] * (D+1)

# 何も指定がないと24時間働くことが抜けていて詰まった
for _ in range(N):
    L, R, H = map(int,input().split())
    for i in range(L,R+1):
        if ans[i] == 0:
            ans[i] = H
        else:
            if ans[i] >= H:
                ans[i] = H
for j in range(1, D+1):
    if ans[j] == 0:
        ans[j] = 24
# print(ans)
print(sum(ans))
