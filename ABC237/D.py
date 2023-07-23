from collections import deque
N = int(input())
S = list(input())
A = deque([0])
ind = 0
val = 1

# insertがO(N)かかるからTLEする
# 処理をまとめる必要あり→基準の場所から右にあるものと左にあるものに分け、dequeで管理するという発想がなかった(特に基準の場所から見てという発想)
# for i in S:
#     if i == "L":
#         A.insert(ind, val)
#     else:
#         ind += 1
#         A.insert(ind, val)
#     val += 1
# print(*A)

L = deque([])
R = deque([])

for i in S:
    if i == "L":
        R.appendleft(val-1)
    else:
        L.append(val-1)
    val += 1

L.append(val-1)
L.extend(R)
ans = list(L)
print(*ans)
