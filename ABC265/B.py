N, M, T = map(int,input().split())
A = list(map(int,input().split()))
XY = [list(map(int,input().split())) for _ in range(M)]
room = [0] * (N+1)
room[1] = T
for i in range(M):
    room[XY[i][0]] += XY[i][1]
ans = True

# 詰まった理由:移動ができるか判定した上で移動しないといけないのに、移動先の回復込みで移動できるかで判断していた
for j in range(1,N):
    if room[j] - A[j-1] > 0:
        room[j+1] += room[j] - A[j-1]
    else:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
