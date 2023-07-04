N = int(input())
a = list(map(int,input().split()))
a_unique = set()

for i in range(N):
    if a[i] not in a_unique:
        a_unique.add(a[i])

print(len(a_unique))
