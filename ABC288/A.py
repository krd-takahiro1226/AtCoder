N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

for i,j in AB:
    print(i+j)
