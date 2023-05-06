N, M = map(int,input().split())
city = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,input().split())
    city[A].append(B)
    city[B].append(A)
# print(city)

for i in range(1,len(city)):
    len_city = len(city[i])
    city[i].sort()
    print(len_city,*city[i])
