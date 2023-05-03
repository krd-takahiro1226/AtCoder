N, M = map(int,input().split())
ans = [[0] * (N+1) for _ in range(N+1)]

# ansを2次元の記録表として、どの組み合わせが同じ舞踏会に参加しているかを全探索で記録(0は参加していない、1は参加した)
for _ in range(M):
    kx = list(map(int,input().split()))
    k = kx[0]
    for i in range(1,k+1):
        for j in range(1,k+1):
            ans[kx[i]][kx[j]] = 1

for k in range(1,N+1):
    for l in range(1,N+1):
# 1つでも例外があったらダメなのでNoを出力するよう処理
        if ans[k][l] == 0:
            print("No")
            exit()
print("Yes")



# 参考にしたACコード
# n, m = map(int, input().split())
# a = [[0]*n for _ in range(n)]
# for i in range(m):
#     k = list(map(int, input().split()))
#     for j in range(1, k[0]+1):
#         for l in range(1, k[0]+1):
#             a[k[j]-1][k[l]-1] = 1
# for i in range(n):
#     for j in range(n):
#         if a[i][j] == 0:
#             print('No')
#             exit()
# print('Yes')


# 間抜け解答(途中で断念)
# for _ in range(M):
#     kx = list(map(int,input().split()))
#     k = kx[0]
#     for i in range(1,k+1):
#         for j in range(i+1,k+1):
#             attend[kx[i]].append(kx[j])
#             ans.append([kx[i],kx[j]])
# ans_unique = list(map(list, set(map(tuple, ans))))
