N, X = map(int,input().split())
A_list = []
B_list = []
coin_num = 0
ans = False
for _ in range(N):
    A, B = map(int,input().split())
    A_list.append(A)
    B_list.append(B)
    coin_num += B
dp = [[False] * (X+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(1,N+1):
    for j in range(X+1):
        if dp[i-1][j] or dp[i][j]:
            dp[i][j] = True
        for k in range(B_list[i-1]+1):
            if dp[i-1][j] == True and j + k*A_list[i-1] <= X:
                dp[i][j+k*A_list[i-1]] = True
                dp[i][j] = True
                if j + k*A_list[i-1] == X:
                    ans = True
                    break
if ans:
    print("Yes")
else:
    print("No")






# 全額出してお釣りが分解できるかで判定(上手くいかなかった)
# score = []
# for j in range(N):
#     score.append(A[j] * B[j])
# score = sum(score)

# A = np.array(A)
# B = np.array(B)

# diff = score - X
# for l in range(N):
#     if diff > 0:
#         A_cross = min(B[np.argmax(A)], diff // max(A))
#         diff = diff - max(A) * A_cross
#         B = np.delete(B,np.argmax(A),0)
#         A = np.delete(A,np.argmax(A),0)
#     else:
#         break
# if diff == 0:
#     print("Yes")
# else:
#     print("No")


# 金額を所持硬貨の大きい順に分解して判定(上手くいかなかった)
# for i in range(N):  
#     if X > 0:
#         A_max = max(A)
#         # print(A_max) # 100
#         # print(X) # 500
#         # print(X // max(A)) # 5 これがいけない
#         # print(min(B[np.argmax(A)],(X // max(A)))) # 3
#         A_cross = min(B[np.argmax(A)],X // max(A))
#         # print(A_cross)
#         X = X - A_max * A_cross
#         A = np.delete(A,np.argmax(A),0)
#     else:
#         print("通過")
#         break
# if X == 0:
#     print("Yes")
# else:
#     print("No")


# 3 21
# 1 4
# 2 3
# 5 6


# 4 400
# 1 1
# 20 5
# 40 5
# 100 1


# 3 2500
# 1000 1
# 500 2
# 2500 1


# 3 1400
# 50 15
# 100 1
# 500 6

# 3 1000
# 1000 1
# 500 1
# 2500 1



# 例外
# 5 1000
# 600 9
# 1000 1
# 1400 1
# 2200 5
# 3000 1
