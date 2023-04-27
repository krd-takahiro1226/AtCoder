N , M = map(int,input().split())
graph = {}

# 自分で考えたコード、WAする(要素がないものが出力されていない→全要素のkeyについてvalue=set()で初期化)
for j in range(1,N+1):
    graph[j] = set()
# グラフの受け取り
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
# graphをsort(順番に並んでいるとは限らないため)
graph = sorted(graph.items())
graph = dict((x, y) for x, y in graph)  
# 全要素をprintする動作(この問題では、valueがないものがset()と出力されるため機能しない)
# for mykey, myvalue in graph.items():
#     print(str(mykey) + ": " + str(myvalue))
# そのままprintすると、valueがset()と出力されるため、valueがset()の時{}と出力するよう変更
for i in range(1,N+1):
    if graph[i] != set():
        print(str(i) + ": " + str(graph[i]))
    else:
        print(str(i) + ": " + "{}")


# 解説の出力方法を真似した
# N , M = map(int,input().split())
# graph = [[] for _ in range(N)]

# グラフの受け取り
# for _ in range(M):
#     i, j = map(int,input().split())
#     graph[i - 1].append(j)
#     graph[j - 1].append(i)

# for i in range(1, N + 1):
# 	output = ''
# 	output += str(i)
# 	output += ': {'
# 	output += ', '.join(map(str, graph[i-1])) # 例えば G[i] = { 2, 7, 5 } のとき、ここで "2, 7, 5" という文字列が output の後ろに連結される
# 	output += '}'
# 	print(output)
