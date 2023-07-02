N = int(input())
A = list(map(int,input().split()))
A_uniq = set(A)

for i in range(2001):
    if i not in A_uniq:
        print(i)
        break
