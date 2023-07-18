S = list(input())
str_set = {"a", "b", "c"}
ans = True

for i in S:
    if i in str_set:
        str_set.remove(i)
    else:
        ans = False

if ans:
    print('Yes')
else:
    print('No')
