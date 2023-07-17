N = int(input())
a = list(map(int,input().split()))
ans = 0
# 2で何回割り切れるかを足し合わせる
for i in a:
    if i % 2 == 0:
        value = format(i, 'b')[::-1].find('1')
        ans += value

print(ans)
