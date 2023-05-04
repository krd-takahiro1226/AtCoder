import bisect
N = int(input())
A = list(map(int,input().split()))
A_unique = list(set(A))
A.sort()
A_unique.sort()
ans = [0] * (N)
# ソートして対象のインデックスがいくつか調べてやる？
# 全要素について調べないといけないのにsetで重複削除したからそれができてない
for i in A:
    ind = bisect.bisect_right(A_unique,i)
    num = len(A_unique) - ind
    ans[num] += 1
for j in ans:
    print(j)

# 対象の値より大きい要素を検索(TLEする)
# for i in A:
#     A_big = list(filter(lambda x: x > i, A_unique))
#     A_big_len = len(A_big)
#     ans[A_big_len] += 1
