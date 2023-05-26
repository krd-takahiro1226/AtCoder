N = int(input())
H = list(map(int,input().split()))
ans = True

for i in range(N-1):
    if not(H[i] <= H[i+1] or H[i] <= H[i+1]-1):
        ans = False
        break
    if H[i] != H[i+1]:
        H[i+1] -= 1

if ans:
    print("Yes")
else:
    print("No")
