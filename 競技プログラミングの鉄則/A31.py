N = int(input())
ans = 0

ans += N // 3
ans += N // 5
ans -= N // 15

print(ans)


# バカがやること
# for i in range(1,N+1):
#     if i % 3 == 0:
#         ans += 1
#     elif i % 5 == 0:
#         ans += 1
#     elif i % 15 == 0:
#         ans -= 1
