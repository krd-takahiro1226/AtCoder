N, X = map(int,input().split())
A = [0]
A.extend(list(map(int,input().split())))
visited = [False] * (N+1)
visited[X] = True
ind = A[X]

for i in range(N):
    visited[ind] = True
    ind = A[ind]
print(sum(visited))
