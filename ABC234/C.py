K = int(input())
# 10進数をn進数に変換する関数
def Base_10_to_n(X, n):
    if X//n:
        return Base_10_to_n(X//n, n)+str(X % n)
    return str(X % n)

K_2 = Base_10_to_n(K, 2)
ans = 2 * int(K_2)
print(ans)
