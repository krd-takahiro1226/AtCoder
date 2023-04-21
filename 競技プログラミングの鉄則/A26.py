import math
Q = int(input())
X = []
for _ in range(Q):
    X.append(int(input()))
max_x = max(X)
# O(NloglogN)
def eratosthenes_sieve(n):
    is_prime = [True]*(n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
        if is_prime[p]:
            for q in range(2*p, n + 1, p):
                is_prime[q] = False
    return is_prime

search_range = int(max_x) + 1
is_prime = eratosthenes_sieve(search_range)

for i in range(Q):
    if is_prime[X[i]]:
        print("Yes")
    else:
        print("No")
