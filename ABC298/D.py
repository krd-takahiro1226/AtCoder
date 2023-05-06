from collections import deque
Q = int(input())
S = 1
S_str = str(S)
deq = deque([1])
MOD = 998244353

# 自分のコード(方針は合っている、計算量的に間に合わないケースに対応できていない)
# 桁数を求めるために毎回、数値→文字列をやると計算量使う？→代わりにdequeを使用してdequeの長さで代用する←多分、文字列の長さを求めるのが計算負荷高い？
# 10の累乗求めるときにあまりを取っておく→最後にまとめて余りを取るより計算量減らせる？
# ↑これも必要だけどMODの値を超えると値を保持しきれず、元の値が復元不可能になるからdequeに何が追加されてきたのかを記録→左から取り出すことで復元可能に
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        S = (S * 10 + query[1]) % MOD
        deq.append(query[1])
    elif query[0] == 2:
        num = deq.popleft()
        S_digit = len(deq)
# numは1桁の整数だからMODで割った余りと等しくなる→10の累乗とMODの余りのみを考えれば良い
        S -= num * pow(10, S_digit, MOD)
        # S = S - int(S_str[0]) * (10 ** S_digit)
    elif query[0] == 3:
        ans = S % MOD
        print(ans)







# 自分のコード(スライスによって文字を更新)
# query = []
# for _ in range(Q):
#     query.append(list(input()))
# for q in query:
#     if q[0] == "1":
#         S = S + q[2]
#     elif q[0] == "2":
#         S = S[1:]
#     elif q[0] == "3":
#         S_int = int(S) 
#         ans = S_int % 998244353
#         print(ans)
