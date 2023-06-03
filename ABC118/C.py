N = int(input())
A = list(map(int,input().split()))
cnt = 0
min_A = min(A)

# 詰まった理由:最小の値で割った余りに更新する処理を行う中で、最小が0になった時、1に変更する処理を行なった
# この処理だと、0を除く最小の値が1以外である時にWAする
while cnt != N:
    cnt = 0
    A_unique = list(set(A))
    A_unique.sort()
    if A_unique[0] == 0:
        min_A = A_unique[1]
    else:
        min_A = A_unique[0]
    for i in range(N):
        if A[i] % min_A == 0:
            cnt += 1
        if A[i] != min_A:
            A[i] %= min_A
print(min_A)
