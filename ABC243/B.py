N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
pos_num = 0
num = 0

for i in range(N):
    if A[i] == B[i]:
        pos_num += 1
    else:
        if A[i] in B:
            num += 1
print(pos_num)
print(num)
