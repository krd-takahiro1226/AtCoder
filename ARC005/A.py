N = int(input())
w = input().split()
ans = 0
search = {"TAKAHASHIKUN","Takahashikun","takahashikun","TAKAHASHIKUN.","Takahashikun.","takahashikun."}

for i in w:
    if i in search:
        ans += 1

print(ans)
