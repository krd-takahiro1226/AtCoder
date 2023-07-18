N = int(input())
ans = False

for i in range(1,10):
    val = N / i
    if val.is_integer() and val <= 9:
        ans = True
        break

if ans:
    print('Yes')
else:
    print('No')
