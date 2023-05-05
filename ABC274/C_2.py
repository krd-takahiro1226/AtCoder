N = int(input())
A = list(map(int,input().split()))
ameba = [0] * (2*N+2)
cnt = 1

for i in A:
    ameba[2*cnt] = ameba[i] + 1
    ameba[2*cnt+1] = ameba[i] + 1
    cnt += 1
ameba.pop(0)
for i in ameba:
    print(i)
