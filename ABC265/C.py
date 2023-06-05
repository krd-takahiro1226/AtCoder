H, W = map(int,input().split())
G = [list(input()) for _ in range(H)]
x = 1
y = 1
visit = set()
visit.add((x,y))
move = True
Loop = False

# ループの判定は一度訪れた場所を再度訪れるか
while(move):
    x_prev = x
    y_prev = y
    if G[x-1][y-1] == "U":
        if x != 1:
            x -= 1
        else:
            move = False
    elif G[x-1][y-1] == "D":
        if x != H:
            x += 1
        else:
            move = False
    elif G[x-1][y-1] == "L":
        if y != 1:
            y -= 1
        else:
            move = False
    else:
        if y != W:
            y += 1
        else:
            move = False
    if (x,y) in visit and move:
        Loop = True
        break
    else:
        visit.add((x,y))
if not move:
    print(x,y)
else:
    print(-1)


# for i in range(H):
#     for j in range(W):
#         x_prev = x
#         y_prev = y
#         if G[x-1][y-1] == "U":
#             if x != 1:
#                 x -= 1
#         elif G[x-1][y-1] == "D":
#             if x != H:
#                 x += 1
#         elif G[x-1][y-1] == "L":
#             if y != 1:
#                 y -= 1
#         else:
#             if y != W:
#                 y += 1
