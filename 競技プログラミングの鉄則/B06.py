N = int(input())
A = list(map(int,input().split()))
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

win_cnt = 0
lose_cnt = 0

win = [0] * (N+1)
lose = [0] * (N+1)

for i in range(N):
    if A[i] == 1:
        win_cnt += 1
    elif A[i] == 0:
        lose_cnt += 1
    win[i+1] = win_cnt
    lose[i+1] = lose_cnt

for i,j in LR:
    win_score = win[j] - win[i - 1]
    lose_score = lose[j] - lose[i - 1]
    if win_score > lose_score:
        print("win")
    elif win_score == lose_score:
        print("draw")
    else:
        print("lose")
