Q = int(input())
dic = {}

for _ in range(Q):
    query = list(input().split())
    num = int(query[0])
    if num == 1:
        dic[query[1]] = int(query[2])
    else:
        print(dic[query[1]])
