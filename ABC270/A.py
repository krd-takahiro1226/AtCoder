A, B = map(int,input().split())
AC = [False] * 3
problem = [1,2,4]
cnt = 1
ans = 0

def check(A,AC):
    if A == 1:
        AC[0] = True
    elif A == 2:
        AC[1] = True
    elif A == 3:
        AC[0] = True
        AC[1] = True
    elif A == 4:
        AC[2] = True
    elif A == 5:
        AC[0] = True
        AC[2] = True
    elif A == 6:
        AC[1] = True
        AC[2] = True
    elif A == 7:
        AC[0] = True
        AC[1] = True
        AC[2] = True
    else:
        pass

check(A,AC)
check(B,AC)

for i in AC:
    if i == True and cnt == 1:
        ans += 1
    elif i == True and cnt == 2:
        ans += 2
    elif i == True and cnt == 3:
        ans += 4
    cnt += 1

print(ans)
