import copy
N = int(input())
AB = [list(map(int, input().split())) for l in range(N)]
A = []
B = []
sum_AB = []
score_A = []
score_B = []

for i in range(N):
    A.append(AB[i][0])
    B.append(AB[i][1])

def index_Multi(List,liter):
    #Listはリスト本体・literは検索したい文字
    index_L = []
    for val in range(0,len(List)):
        if liter == List[val]:
            index_L.append(val)
    return index_L

A_i_min = min(A)
A_min_ind = index_Multi(A, A_i_min)
B_i_min = min(B)
B_min_ind = index_Multi(B, B_i_min)

for l in AB:
    sum_AB.append(sum(l))
sum_AB = min(sum_AB)

A_copy = copy.deepcopy(A)
B_copy = copy.deepcopy(B)
# Aの最小から処理
for l in A_min_ind:
    B = copy.deepcopy(B_copy)
    B.pop(l)
    B_min = min(B)
    score_A.append(max(B_min , A_i_min))
score_A = min(score_A)

# Bの最小から処理
for g in B_min_ind:
    A = copy.deepcopy(A_copy)
    A.pop(l)
    A_min = min(A)
    score_B.append(max(A_min , B_i_min))
score_B = min(score_B)

ans = min (score_A, score_B, sum_AB)
print(ans)

# 8
# 8 5
# 4 4
# 7 9
# 4 6
# 1 2
# 5 9
# 6 6
# 10 12
