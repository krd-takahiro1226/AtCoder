N, K = map(int,input().split())
ab = []
b_sum = 0

for _ in range(N):
    a, b = map(int,input().split())
    ab.append([a,b])
    b_sum += b
ab.sort()

if b_sum <= K:
    print(1)
    exit()
    
for i in range(N):
    ai = ab[i][0]
    bi = ab[i][1]
    b_sum -= bi
    if b_sum <= K:
        print(ai+1)
        exit()
print(N)
