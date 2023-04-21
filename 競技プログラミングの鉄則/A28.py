N = int(input())
TA = []
ans_i = 0
for _ in range(N):
    t, a = input().split()
    TA.append([t,int(a)])
    ans_i = ans_i % 10000
    if t == "+":
        ans_i += int(a) % 10000
    elif t == "-":
        ans_i -= int(a) % 10000
    else:
        ans_i *= int(a) % 10000
    if ans_i < 0:
        ans_i += 10000
    print(ans_i % 10000)
