N = int(input())
A = [list(map(int,input())) for _ in range(N)]
std_value = 1
start_ind = []
x = 0
y = 0
cnt = 1
score = 0
score_list = []

shift_x = [1,1,1,0,0,-1,-1,-1]
shift_y = [0,1,-1,1,-1,0,1,-1]

for i in range(N):
    std_value = max(max(A[i]),std_value)

for i in range(N):
    for j in range(N):
        if A[i][j] == std_value:
            x = i
            y = j
            start_ind.append((x,y))

for x_s,y_s in start_ind:
    for k in range(8):
        score = A[x_s][y_s] * 10 **(N-1)
        x = x_s
        y = y_s
        shift = (shift_x[k],shift_y[k])
        cnt = 1
        for _ in range(N-1):
            x += shift_x[k]
            y += shift_y[k]
            x %= N
            y %= N
            score += A[x][y] * 10 ** (N-1-cnt)
            score_list.append(score)
            cnt += 1
print(max(score_list))
