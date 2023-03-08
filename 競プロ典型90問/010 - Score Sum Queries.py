N = int(input())
CP = [list(map(int, input().split())) for l in range(N)]
Q = int(input())
LR = [map(int, input().split()) for _ in range(Q)]
L , R = [list(i) for i in zip(*LR)]
score = [[0,0]]
score_i = [0,0]
# LR = [list(map(int, input().split())) for l in range(Q)]
# print(CP)
# # print(LR)
# print(L,R)

for i in range(N):
    if CP[i][0] == 1:
        # score_i.append([CP[i][1],0])
        score_i = [score_i[0] + CP[i][1] , score_i[1]]
    if CP[i][0] == 2:
        # score_i.append([CP[i][1],0])
        score_i = [score_i[0] , score_i[1] + CP[i][1]]
    # score_i = []
    # print(score_i)
    score.append(score_i)
# print(score)

for j in range(Q):
    L_j = L[j] # 1
    R_j = R[j] # 3
    sum_1 = score[R_j][0] - score[L_j - 1][0]
    sum_2 = score[R_j][1] - score[L_j - 1][1]
    print(sum_1,sum_2)


# 全探索(計算量的に無理)
# for i in range(Q):
#     Score_1 = 0
#     Score_2 = 0
#     for j in range(L[i] - 1,R[i]):
#         if CP[j][0] == 1:
#             Score_1 += CP[j][1]
#             # print(CP[j][1])
#         elif CP[j][0] == 2:
#             Score_2 += CP[j][1]
#             # print(CP[j][1])
#     print(Score_1, Score_2)
