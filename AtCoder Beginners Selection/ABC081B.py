N = int(input())
A1_AN = list(map(int, input().split()))
# N = 4
# A1_AN = [5, 6, 8, 10]
count = 0

for i in range(210):
    # リストの中の偶数をカウント
    A1_AN_mod = list(map(lambda x: x % 2, A1_AN))
    if(A1_AN_mod.count(0) == len(A1_AN) and A1_AN.count(0) == 0):
        count = count + 1
    # リスト全体を2で割る
        A1_AN = list(map(lambda x: x / 2, A1_AN))
    else:
        break
print(count)

# for i in A1_AN:
#     if(i % 2 == 0):
#         count = count + 1
# if(count == N):
#     A1_AN = A1_AN / 2
#     ans = ans + 1
# print(ans)
