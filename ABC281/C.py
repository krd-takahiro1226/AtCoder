N, T = map(int,input().split())
A = list(map(int,input().split()))
A_sum = sum(A)
cnt = 1
remain = T % A_sum


for i in A:
    if remain > i:
        remain -= i
        cnt += 1
    else:
        ans = remain
        break
print(cnt,ans)
