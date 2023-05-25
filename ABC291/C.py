N = int(input())
S = list(input())
visit = set()
x = 0
y = 0
visit.add((x,y))
ans = False

for i in S:
    if i == "R":
        x += 1
    elif i == "L":
        x -= 1
    elif i == "U":
        y += 1
    else:
        y -= 1
# 多分だめ、後で確認してみる
    if (x,y) in visit:
        ans = True
        break
    else:
        visit.add((x,y))

if ans:
    print("Yes")
else:
    print("No")
