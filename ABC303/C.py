N, M, H, K = map(int,input().split())
S = list(input())
heal_list = [tuple(map(int,input().split())) for _ in range(M)]
heal_list = set(heal_list)
ans = True
x = 0
y = 0

for i in range(N):
    if S[i] == "R":
        x += 1
        H -= 1
    elif S[i] == "U":
        y += 1
        H -= 1
    elif S[i] == "D":
        y -= 1
        H -= 1
    else:
        x -= 1
        H -= 1
    if H < 0:
        ans = False
        break
    else:
        if H < K and (x,y) in heal_list:
            H = K
            heal_list.remove((x,y))

if ans:
    print("Yes")
else:
    print("No")
