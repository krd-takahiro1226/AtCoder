N = int(input())
h = list(map(int,input().split()))
ans = [0] * N
ans[1] = abs(h[0]-h[1])

for i in range(2, N):
    ans[i] = min(ans[i-1] + abs(h[i] - h[i-1]), ans[i-2] + abs(h[i] - h[i-2]))
print(ans[N-1])
