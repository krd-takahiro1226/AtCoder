N = int(input())

ans = 0
count = 0
for i in range(N - 1):
    count += 1
    ans += N/(N - count)
print(ans)
# print(type(ans))
