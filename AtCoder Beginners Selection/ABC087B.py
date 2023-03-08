A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0
# 500円玉,100円,50円,合計金額
# A, B, C, X = 30, 40, 50, 6000

for i in range(C + 1):
    X_A = X - 50 * i
    # print(X_A)
    if(X_A == 0):
        count = count + 1
    else:
        for j in range(B + 1):
            X_B = X_A - 100 * j
            if (X_B == 0):
                count = count + 1
            else:
                for k in range(A + 1):
                    X_C = X_B - 500 * k
                    if (X_C == 0):
                        count = count + 1
print(count)
