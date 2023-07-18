from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
dic  =defaultdict(int)

for i in A:
    dic[i] += 1

for key, value in dic.items():
    if value != 4:
        print(key)
