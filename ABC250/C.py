from collections import defaultdict
N, Q = map(int,input().split())
ball = [i for i in range(1,N+1)]
ind = defaultdict(int)
for j in range(1,N+1):
    ind[j] = j - 1

for _ in range(Q):
    x = int(input())
    if ball[N-1] != x:
        # 入れ替え後に右にくる→right_ind
        left_ind = ind[x]
        # right_ind = ind[ball[ind[x]]] + 1
        right_ind = ind[x] + 1
        ind[x] = right_ind
        # tmp = right_ind
        # ind[ball[tmp]] = left_ind ↓より、tmpを使用してこう書いた方が可読性は良い
        ind[ball[ind[x]]] = left_ind
        tmp = ball[right_ind]
        ball[right_ind] = ball[left_ind]
        ball[left_ind] = tmp
    else:
        left_ind = ind[x]
        # right_ind = ind[ball[ind[x]]] - 1
        right_ind = ind[x] - 1
        ind[x] = right_ind
        ind[ball[ind[x]]] = left_ind
        tmp = ball[right_ind]
        ball[right_ind] = ball[left_ind]
        ball[left_ind] = tmp
print(*ball)
