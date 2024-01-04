N = int(input())
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0 and i <= 9:
            lower_divisors.append(i)
            if i != n // i and n//i <= 9:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

divisor = make_divisors(N)
ans = ""

for i in range(N+1):
    if i == 0:
        ans += "1"
    else:
        judge = 0
        for j in divisor:
            if i % (N//j) == 0:
                ans += str(j)
                break
            else:
                judge += 1
            if judge == len(divisor):
                ans += "-"

print(ans)
