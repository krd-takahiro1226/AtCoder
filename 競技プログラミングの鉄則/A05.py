N ,K = map(int,input().split())

cand = []
cnt = 0
for red in range(1, N+1):
    for blue in range(1, N+1):
        cand.append(red + blue)

for i in cand:
    if i + 1 <= K <= i + N:
        cnt += 1

print(cnt)
