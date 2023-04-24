N, Q = map(int,input().split())
A = list(range(N+1))
reverse = False

# 反転操作は実際に行わない、現在反転している状態か正常な状態かを記録
# 正常:A[x] = y、反転:A[N+1-x] = yとする
for _ in range(Q):
    query = list(map(int,input().split()))
    if reverse == False:
        if query[0] == 1:
            A[query[1]] = query[2]
        elif query[0] == 2:
            reverse = True
        else:
            print(A[query[1]])
    else:
        if query[0] == 1:
            A[N+1-query[1]] = query[2]
        elif query[0] == 2:
            reverse = False
        else:
            print(A[N+1-query[1]])


# 自分の解答(間違い)
# for _ in range(Q):
#     query = list(map(int,input().split()))
#     if query[0] == 1:
#         A[query[1]] = query[2]
#     elif query[0] == 2:
#         A.reverse()
#     else:
#         print(A[query[1]])
