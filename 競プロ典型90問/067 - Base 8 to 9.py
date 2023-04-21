import sys
sys.setrecursionlimit(10**6)
N, K = map(int,input().split())
N_str = str(N)
ind = len(N_str) - 1
value = 0
# こっちの関数だと通らない
# def Base_10_to_n(X, n):
#     if (int(X/n)):
#         return Base_10_to_n(int(X/n), n)+str(X % n)
#     return str(X % n)
# 10進数をn進数に変換する関数
def Base_10_to_n(X, n):
    if X//n:
        return Base_10_to_n(X//n, n)+str(X % n)
    return str(X % n)

for _ in range(K):
    if N != 0:
        N_str = str(N)
        ind = len(N_str) - 1
        value = 0
        # 8進数を10進数に
        for i in range(1,len(N_str)+1):
            value += int(N_str[ind]) * (8 ** (i-1))
            ind -= 1
        # 10進数を9進数に
        if value != 0:
            value_str = str(value)
            base_9 = Base_10_to_n(value,9)
        else:
            base_9 = "0"
        ans = base_9.replace("8","5")
        N = ans
    else:
        ans = 0
print(ans)



    # 自作の10進数→9進数(動かない)
    # for j in range(len(value_str)):
    #     if value >= 9:
    #         value_i = value // 9**(len(value_str)-j_cnt)
    #         value -= value_i * (9**(len(value_str)-j_cnt))
    #     else:
    #         value_i = value
    #     if j == 0:
    #         base_9 = str(value_i)
    #     else:
    #         base_9 += str(value_i)
    #     j_cnt += 1
