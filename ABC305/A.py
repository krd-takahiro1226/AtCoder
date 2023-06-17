N = int(input())
syou = N // 5
if abs(N - syou * 5) > abs(N - (syou+1)*5):
    ans = (syou+1)*5
elif abs(N - syou * 5) > abs(N - (syou-1)*5):
    ans = (syou-1)*5
else:
    ans = syou * 5

print(ans)
