N = int(input())
A = list(map(int,input().split()))
DEGREE = 360
cut = 0
cut_list = [0,360]
ans = []

for i in A:
    cut += i
    cut %= DEGREE
    cut_list.append(cut)
cut_list.sort()
for j in range(len(cut_list)-1):
    diff = abs(cut_list[j] - cut_list[j+1])
    ans.append(diff)

print(max(ans))
