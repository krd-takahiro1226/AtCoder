N = int(input())
X = list(map(int,input().split()))
X.sort()
for _ in range(N):
    X.pop(0)
    X.pop(len(X)-1)
# print(X)
print(sum(X)/len(X))
