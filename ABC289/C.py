from itertools import product
N, M = map(int,input().split())
C = []
a = []
cnt = 0
ans = 0
for _ in range(2*M):
    if cnt % 2 == 0:
        C.append(int(input()))
    elif cnt % 2 == 1:
        a.append(set(map(int,input().split())))
    cnt += 1

product_list = product((0,1),repeat=M)

for pro in product_list:
    ans_i = set()
    cnt_pro = 0
    judge = True
    for i in pro:
        if i == 1:
            # ans_i.add(a[cnt_pro])
            ans_i = ans_i | a[cnt_pro]
        cnt_pro += 1
    for j in range(1,N+1):
        if j not in ans_i:
            judge = False
            break
    if judge:
        ans += 1

print(ans)



# 模範回答
# N,M=map(int,input().split())
# S=[]
# for _ in range(M):
#     input()
#     S.append(set(map(int,input().split())))
# print(S)

# def dfs(pos,s):
#     if pos==M:
#         if s==set(range(1,N+1)):
#             return 1
#         else:
#             return 0
#     return dfs(pos+1,s)+dfs(pos+1,s|S[pos])

# print(dfs(0,set()))
