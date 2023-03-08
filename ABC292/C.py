N = int(input())
ans = 0

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return len(lower_divisors + upper_divisors[::-1])

for i in range(1, N//2 + 1, 1):
    AB = i
    CD = N - i
    if AB == CD:
        ans += make_divisors(AB) * make_divisors(AB)
    else:
        tmp_AB = make_divisors(AB)
        tmp_CD = make_divisors(CD)
        ans += tmp_AB * tmp_CD * 2
print(ans)
