N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]
time = 0
ans = 0

for i in range(N):
    A = AB[i][0]
    B = AB[i][1]
    time += A / B

collision = time / 2

for j in range(N):
    A = AB[j][0]
    B = AB[j][1]
    time_i = A / B
    if collision >= time_i:
        collision -= time_i
        ans += A
    else:
        ans += B * collision
        collision = 0

print(ans)
