from collections import defaultdict
N = int(input())
S = [input() for _ in range(N)]
dic = defaultdict(int)
base = 0

for i in S:
    dic[i] += 1

for key, val in dic.items():
    if val > base:
        base = val
        ans = key

print(ans)
