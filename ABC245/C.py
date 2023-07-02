N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = False
# dp[i][0]:i番目のAを採用することがあるか、dp[i][1]:i番目のBを採用することがあるか
dp = [[False] * 2 for _ in range(N)]
dp[0] = [True,True]

if N >= 2:
    for i in range(N-1):
        aa_diff = abs(A[i] - A[i+1])
        ab_diff = abs(A[i] - B[i+1])
        ba_diff = abs(B[i] - A[i+1])
        bb_diff = abs(B[i] - B[i+1])
        if dp[i][0] and aa_diff <= K:
            dp[i+1][0] = True
        if dp[i][0] and ab_diff <= K:
            dp[i+1][1] = True
        if dp[i][1] and ba_diff <= K:
            dp[i+1][0] = True
        if dp[i][1] and bb_diff <= K:
            dp[i+1][1] = True
else:
    ans = True

if dp[N-1][0] or dp[N-1][1] or ans:
    print("Yes")
else:
    print("No")








# a_select,b_select:AまたはBに遷移することがあるか
# if A_diff[0][0] <= K or B_diff[0][0] <= K:
#     a_select = True
# else:
#     a_select = False
# if A_diff[0][1] <= K or B_diff[0][1] <= K:
#     b_select = True
# else:
#     b_select = False

# for j in range(1,N-1):
#     aa_diff = A_diff[j][0]
#     ab_diff = A_diff[j][1]
#     ba_diff = B_diff[j][0]
#     bb_diff = B_diff[j][1]
#     if a_select:
#         if aa_diff <= K:
#             a_select_tmp = True
#         else:
#             a_select_tmp = False
#         if ab_diff <= K:
#             b_select_tmp = True
#         else:
#             b_select_tmp = False
#     if b_select:
#         if ba_diff <= K or a_select_tmp:
#             a_select = True
#         else:
#             a_select = False
#         if bb_diff <= K or b_select_tmp:
#             b_select = True
#         else:
#             b_select = False
#     if a_select or b_select:
#         cnt += 1
# if cnt == N-1:
#     print("Yes")
# else:
#     print("No")
