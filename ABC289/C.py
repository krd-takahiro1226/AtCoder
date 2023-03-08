# N, M = map(int,input().split())
# C = []
# a = []
# cnt = 0
# for _ in range(2*M):
#     if cnt % 2 == 0:
#         C.append(int(input()))
#     elif cnt % 2 == 1:
#         a.append(list(map(int,input().split())))
#     cnt += 1


# 模範回答
N,M=map(int,input().split())
S=[]
for _ in range(M):
    input()
    S.append(set(map(int,input().split())))
print(S)

def dfs(pos,s):
    if pos==M:
        if s==set(range(1,N+1)):
            return 1
        else:
            return 0
    return dfs(pos+1,s)+dfs(pos+1,s|S[pos])

print(dfs(0,set()))
