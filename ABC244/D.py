s1,s2,s3 = input().split()
t1,t2,t3 = input().split()
s = [s1,s2,s3]
t = [t1,t2,t3]
cnt = 0
ans = True

for i in range(3):
    if s[i] != t[i]:
        cnt += 1

if cnt == 2:
    ans = False

if ans:
    print("Yes")
else:
    print("No")
