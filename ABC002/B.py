W = list(input())
str_list = ["a","i","u","e","o"]
str_unique = set(str_list)
ans = []

for i in W:
    if i not in str_list:
        ans.append(i)
print(*ans,sep='')
