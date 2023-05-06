N = int(input())
P = list(map(int,input().split()))

# 長さNでnum番目の順列を求める
from collections import deque
def Permutation_N(N,num):
    remain_deque = deque()
    serial_num = list(range(1,N+1))
    ans = []
    for i in range(1,N+1):
        remain = num % i
        num = num // i
        remain_deque.appendleft(remain)
    for j in range(N):
        ind = remain_deque.popleft()
        ans.append(serial_num[ind])
        serial_num.pop(ind)
    return ans

# 順列が辞書順に何番目か調べる関数
from math import factorial #x!を計算
def index_of_permutation(L):
    index = 0  #0-indexed
    while len(L)> 1:
        a = len([l for l in L if l<L[0]])
        index = index + a * factorial(len(L) - 1)
        L = L[1:]
    return index

num_ind = index_of_permutation(P)
print(*Permutation_N(N,num_ind - 1))
