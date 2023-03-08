N, Q = map(int,input().split())
event = [list(map(int, input().split())) for l in range(Q)]
player = [0] * (N + 1)

for i in event:
    if i[0] == 1:
        player[i[1]] += 1
    elif i[0] == 2:
        player[i[1]] += 2
    else:
        if player[i[1]] >= 2:
            print("Yes")
        else:
            print("No")
