N = int(input())
half_over = N // 2 + 1
cnt = 0
for _ in range(N):
    if input() == "For":
        cnt += 1

if cnt >= half_over:
    print("Yes")
else:
    print("No")
