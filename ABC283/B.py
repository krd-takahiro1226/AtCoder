N = int(input())
A = list(map(int,input().split()))
Q = int(input())

for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        A[query[1]-1] = query[2]
    else:
        print(A[query[1]-1])
