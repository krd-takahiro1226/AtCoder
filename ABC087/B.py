A = int(input()) # 500
B = int(input()) # 100 
C = int(input()) # 50
X = int(input())
ans = 0

for i in range(A+1):
    for j in range(B+1):
        val = 500 * i + 100 * j
        diff = X - val
        if diff >= 0 and diff // 50 <= C and diff % 50 == 0:
            ans += 1

print(ans)
