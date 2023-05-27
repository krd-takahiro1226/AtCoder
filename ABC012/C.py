N = int(input())
value = 2025
diff = value - N
ans = []

for i in range(1,10):
    for j in range(1,10):
        if diff == i * j:
            ans_ij = str(i) + "x" + str(j)
            ans.append(ans_ij)

for k in ans:
    print(*k)
