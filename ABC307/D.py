from collections import deque
N = int(input())
S = list(input())
T = ""
ind = deque()

# heapqだとTLEする←heapqが原因かは不明
# リストにappendするより、文字列の結合の方が圧倒的にはやい
for i in range(N):
    if S[i] == "(":
        T += S[i]
        ind.append(len(T)-1)
    elif S[i] == ")":
        if len(ind) != 0:
# )が来た時、一番後ろの(との間を消す
# →(のインデックスがindに格納されているため、ind.pop()で一番後ろの(に対応するインデックスが取り出せる
            s = ind.pop() 
            T = T[:s]
        else:
            T += S[i]
    else:
        T += S[i]
print(*T,sep='')



# for j in range(min(len(s_ind),len(e_ind))):
#     s_mn = s_ind[0]
#     e_mn= e_ind[0]
#     if e_mn > s_mn:
#         s = heapq.heappop(s_ind)
#         e = heapq.heappop(e_ind)
#         S_s = S[:s]
#         S_e = S[e+1-diff:]
#         diff = e + s + 1
#         S = S_s + S_e
#     else:
#         s = heapq.heappop(s_ind)
#         e = heapq.heappop(e_ind)
#         heapq.heappush(s_ind,s)
#     print("s",s)
#     print("S_s",S_s)
#     print("S_e",S_e)
#     print("S",S)

# print(*S,sep='')



# if len(s_ind) == len(e_ind):
#     for j in range(min(len(s_ind),len(e_ind))):
#         s = heapq.heappop(s_ind)
#         s_mx = heapq.heappop(s_mx_ind)
#         e = heapq.heappop(e_ind)
#         if -s_mx > e:
#             pass
#         else:
#             pass
#         S_s = S[:-s] 
#         S_e = S[e+1-diff:]
#         diff = e + s + 1
#         S = S_s + S_e
# else:
#     for j in range(min(len(s_ind),len(e_ind))):
#         s = heapq.heappop(s_ind)
#         e = heapq.heappop(e_ind)
#         S_s = S[:s] 
#         S_e = S[e+1-diff:]
#         diff = e + s + 1
#         S = S_s + S_e
