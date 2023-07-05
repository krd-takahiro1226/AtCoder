A, B, C, D = map(int,input().split())
cnt = 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(A,B+1):
    for j in range(C,D+1):
        value = i + j
        prime = is_prime(value)
        if prime:
            cnt += 1
            break

if cnt == (B-A+1):
    print("Aoki")
else:
    print("Takahashi")
