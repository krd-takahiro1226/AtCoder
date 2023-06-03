N = int(input())
A = [list(input()) for _ in range(N)]
ans = True

for i in range(N):
    for j in range(N):
        if A[i][j] == "W" and A[j][i] != "L":
            ans = False
            break
        elif A[i][j] == "L" and A[j][i] != "W":
            ans = False
            break
        elif A[i][j] == "D" and A[j][i] != "D":
            ans = False
            break
if ans:
    print("correct")
else:
    print("incorrect")
