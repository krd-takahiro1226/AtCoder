import sys
sys.setrecursionlimit(10**5)
# N＋1の長さの配列を準備する必要がある
N = int(input())
t = [0] * (N + 1)
x = [0] * (N + 1)
y = [0] * (N + 1)
for i in range(1, N + 1):
    # 上から順番に代入していく
    t[i], x[i], y[i] = map(int, input().split())
# N = 2
# t = [0, 3, 6]
# x = [0, 1, 2]
# y = [0, 1, 1]
ans = "No"
for i in range(N):
    dt = t[i + 1] - t[i]
    dist = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])
    if(dist <= dt and dt % 2 == dist % 2):
        ans = "Yes"
    else:
        ans = "No"
print(ans)
