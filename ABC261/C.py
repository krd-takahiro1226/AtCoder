from collections import defaultdict
N = int(input())
S = []
S_dic = defaultdict(int)
# AC解
for _ in range(N):
    Si = input()
    if Si not in S_dic:
        print(Si)
        S_dic[Si] += 1
    else:
        num = S_dic[Si]
        S_dic[Si] += 1
        print(Si + "(" +str(num) + ")")


# 別解？→予想通りTLE
for _ in range(N):
    Si = input()
    if Si not in S:
        print(Si)
        S.append(Si)
        # S_dic[Si] += 1
    else:
        num = S.count(Si)
        S.append(Si)
        print(Si + "(" +str(num) + ")")
