N , M = map(int,input().split())
ab = [list(map(int, input().split())) for l in range(M)]

print(ab)
count = 1
top_dic = {}

# 頂点が順番に並んでるとは限らない
# 一つの頂点に複数の頂点がつながっているときにうまくいかない
for i in range(M):
    if ab[i][0] == count:
        top_dic[count] = ab[i][1]
    else:
        pass
    count += 1
print(top_dic)
