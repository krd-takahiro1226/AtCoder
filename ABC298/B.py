N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
B = [list(map(int,input().split())) for _ in range(N)]
ans = "No"
A_cnt = 0
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            A_cnt += 1
# 全てに対して等しいか判定している→1のところだけ一致しているか判定するように変更
for num in range(4):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if num == 0:
                if A[i][j] == B[i][j] == 1:
                    cnt += 1
            elif num == 1:
                if A[N-j-1][i] == B[i][j] == 1:
                    cnt += 1
            elif num == 2:
                if A[N-i-1][N-j-1] == B[i][j] == 1:
                    cnt += 1
            elif num == 3:
                if A[j][N-i-1] == B[i][j] == 1:
                    cnt += 1
    # print(cnt)
    if cnt == A_cnt:
        ans = "Yes"
print(ans)
