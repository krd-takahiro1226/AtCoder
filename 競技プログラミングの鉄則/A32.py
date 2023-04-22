N, A, B = map(int,input().split())
remain = min(A, B)
# 4 * 10 ** 5に変える(変える必要ない)
ans = [False] * (4 * 10 ** 5)
# ans = [False] * (10 ** 2)
for i in range(remain):
    ans[i] = 1

# 1が負け、0が勝ち
for i in range(N+1):
    if ans[i-A] == 1 and i >= A:
        ans[i] = 0
    elif ans[i-B] == 1 and i >= B:
        ans[i] = 0
    elif ans[i-A] == 0 and i >= A:
        ans[i] = 1
    elif ans[i-B] == 0 and i >= B:
        ans[i] = 1
print(ans)


if ans[N] == 0:
    print("First")
else:
    print("Second")


# 自分の処理(何が間違っているかわからない)
# for i in range(N):
#     if ans[i] == 1:
#         ans[i+A] = 0
#         ans[i+B] = 0
#     elif ans[i] == 0 and (ans[i+A] == 1 or ans[i+A] == False):
#         ans[i+A] = 1
#     elif ans[i] == 0 and (ans[i+B] == 1 or ans[i+B] == False):
#         ans[i+B] = 1
