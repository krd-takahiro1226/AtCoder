S = input()
ans = 0
for i in S:
    if i.isupper():
        print(ans+1)
        break
    ans += 1
