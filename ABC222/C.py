from collections import defaultdict
N, M = map(int,input().split())
A = [list(input()) for _ in range(2*N)]
dic = defaultdict(int)
rank = [r for r in range(1,2*N+1)]
for k in range(1,2*N+1):
    dic[k] = 0

def win(x,y):
    if (x == "G" and y == "C") or (x == "C" and y == "P") or (x == "P" and y == "G"):
        return 1
    elif (y == "G" and x == "C") or (y == "C" and x == "P") or (y == "P" and x == "G"):
        return -1
    else:
        return 0

def dic_sort(dic):
    return dict(sorted(dic.items(), key=lambda x:(x[1], -x[0]), reverse=True))

for i in range(M):
    for j in range(N):
        ind_s = rank[2*j] - 1
        ind_e = rank[2*j+1] - 1
        s_hand = A[ind_s][i]
        e_hand = A[ind_e][i]
        if win(s_hand, e_hand) == 1:
            dic[ind_s+1] += 1
        elif win(s_hand, e_hand) == -1:
            dic[ind_e+1] += 1
    # 順位の変動を行う
    dic = dic_sort(dic)
    rank = []
    for keys in dic.keys():
        rank.append(keys)

for ans in rank:
    print(ans)
