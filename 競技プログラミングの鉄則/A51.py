from collections import deque
Q = int(input())
d = deque()

for _ in range(Q):
    query = list(input().split())
    num = int(query[0])
    if num == 1:
        d.append(query[1])
    elif num == 2:
        print(d[-1])
    else:
        d.pop()
