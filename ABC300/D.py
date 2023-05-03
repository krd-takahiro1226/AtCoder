# エラトステネスのふるい(x以下の素数列挙)
def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]
    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0
    primes = sorted(list(set(nums)))[2:]
    return primes

# cの最大値を見積もる→a,bがそれぞれ最小なのは2,3であることを利用するとc<3*10**5となることがわかる
# 3*10**5以下の素数をエラトステネスの篩で列挙
# 列挙した素数について全探索
# N以下の数ができているか判定→Nより大きかったらbreakして探索打ち切り
# 全探索という発想を持つために
# 最後の入力例から答えが3*10**6より小さくなることがわかる→ループの回数をO(∣P∣**2 +ans)と見積もることが出来る。
# Pは3*10**5以下の素数をエラトステネスの篩で列挙したリストのサイズ(2.5*10**4)、ansは問題の答え
# |P|**2←二重for分、ans←3重forが実際に回る数
N = int(input())
prime_list = sieve_of_eratosthenes(3*(10**5))
len_prime = len(prime_list)
ans = 0

for i in range(len_prime-2):
    a = prime_list[i]
    for j in range(i+1, len_prime-1):
        b = prime_list[j]
        if (a**2) * (b**3) > N:
            break
        else:
            for k in range(j+1,len_prime):
                c = prime_list[k]
                if (a**2) * b * (c**2) > N:
                    break
                ans += 1

print(ans)


# コンテスト中の解答(間違っている)
# 素数を列挙せず全探索しようとしているため、TLEする。
# def eratosthenes_sieve(n):
#     is_prime = [True]*(n + 1)
#     is_prime[0] = is_prime[1] = False
#     for p in range(2, n + 1):
#         if is_prime[p]:
#             for q in range(2*p, n + 1, p):
#                 is_prime[q] = False
#     return is_prime

# def prime_factorize(n):
#     a = []
#     if  n % 4 == 0:
#         a.append(4)
#         n //= 4
#         f = 3
#         while f * f <= n:
#             if eratosthenes_sieve(f):
#                 if n % f == 0 and f > 2:
#                     a.append(f)
#                     n //= f
#                     break
#                 else:
#                     f += 2
#             else:
#                 f += 2
#         if n != 1 and (n ** .5).is_integer() and n > f and n % 2 !=0 and n % f != 0:
#             a.append(n)
#     else:
#         f = 3
#         while f * f <= n:
#             if eratosthenes_sieve(f):
#                 if n % f** 2 == 0:
#                     a.append(f ** 2)
#                     n //= f ** 2
#                     break
#                 else:
#                     f += 2
#             else:
#                 f += 2
#         g = 3
#         while g * g <= n:
#             if eratosthenes_sieve(g):
#                 if n % g** 2 == 0:
#                     a.append(g ** 2)
#                     n //= g ** 2
#                     break
#                 else:
#                     g += 2
#             else:
#                 g += 2
#         if n != 1 and (n ** .5).is_integer() and n > g:
#             a.append(n)
#     return a

# import math
# n = int(input())
# n_sqrt = int(math.sqrt(n)) + 1
# count = 0
# for i in range(n):
#     pf = prime_factorize(i + 1)
#     # print(pf)
#     if len(pf) == len(set(pf)) == 3:
#         # print(i+1)
#         # print(pf)
#         count += 1
# print(count)
