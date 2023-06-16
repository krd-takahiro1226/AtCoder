N = int(input())
T = list(input())
x = 0
y = 0
direct = [[1,0],[0,-1],[-1,0],[0,1]]
direct_now = direct[0]
cnt = 0

for i in range(N):
    if T[i] == "S":
        x += direct_now[0]
        y += direct_now[1]
    else:
        cnt += 1
        direct_now = direct[cnt % 4]

print(x,y)
