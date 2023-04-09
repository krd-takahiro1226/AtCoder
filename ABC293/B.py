N = int(input())
A = list(map(int,input().split()))
student = [0] * N
cnt = 0

def func1(lst, value):
    return [i for i, x in enumerate(lst) if x == value]

for i in A:
    if student[cnt] == 0:
        student[i - 1] = 1
    cnt += 1
ans = func1(student, 0)
ans_true = []
for i in ans:
    ans_true.append(i+1)
ans_true.sort()
print(len(ans_true))
print(*ans_true)
