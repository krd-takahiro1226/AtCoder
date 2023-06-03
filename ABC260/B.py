N, X, Y, Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = set()
S = []
ans_A = []
ans_B = []
ans_S = []
for i in range(len(A)):
    S.append(A[i]+B[i])

def index_Multi(List,liter):
    #Listはリスト本体・literは検索したい文字
    index_L = []
    for val in range(0,len(List)):
        if liter == List[val]:
            index_L.append(val+1)
    return index_L

A_unique = list(set(A))
A_unique.sort(reverse=True)
B_unique = list(set(B))
B_unique.sort(reverse=True)
S_unique = list(set(S))
S_unique.sort(reverse=True)

for i in A_unique:
    ans_A.append(index_Multi(A,i))
ans_A = sum(ans_A,[])
x = 0
while(len(ans) != X):
    if ans_A[x] not in ans:
        ans.add(ans_A[x])
    x += 1

for j in B_unique:
    ans_B.append(index_Multi(B,j))
ans_B = sum(ans_B,[])
y = 0
while(len(ans) != X + Y):
    if ans_B[y] not in ans:
        ans.add(ans_B[y])
    y += 1

for k in S_unique:
    ans_S.append(index_Multi(S,k))
ans_S = sum(ans_S,[])
z = 0
while(len(ans) != X + Y + Z):
    if ans_S[z] not in ans:
        ans.add(ans_S[z])
    z += 1
ans = list(ans)
ans.sort()
for g in ans:
    print(g)



# 康太のコード
# N,X,Y,Z = map(int,input().split())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# C = [x + y for (x, y) in zip(A, B)]
# C_sort= sorted(C,reverse=True)
# ans = set()

# A_sort = sorted(A,reverse=True)

# for i in range(X):
#     if A.index(A_sort[i]) not in ans:
#         ans.add(A.index(A_sort[i]))
#     A[A.index(A_sort[i])]=-1

# cnt = 0
# B_sort = sorted(B,reverse=True)
# for j in range(N):
#     if cnt == Y:
#         break
#     if B.index(B_sort[j]) not in ans:
#         cnt += 1
#         ans.add(B.index(B_sort[j]))
#     else:
#         continue
#     B[B.index(B_sort[j])]=-1

# cnt = 0

# for k in range(N):
#     if cnt == Z:
#         break
#     if C.index(C_sort[k]) not in ans:
#         cnt += 1
#         ans.add(C.index(C_sort[k]))
#         # C[C.index(C_sort[k])]=-1
#     else:
#         continue
# ans = list(ans)
# ans.sort()
# # print(ans)
# for i in ans:
#     print(i+1)
