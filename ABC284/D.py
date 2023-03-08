import math
T = int(input())
test = []
for _ in range(T):
    test.append(int(input()))
# print(test)
test_cube_root = []
ind = -1


for i in test:
    test_cube_root.append(math.ceil(i**(1/3)))
    # test_cube_root.add(math.ceil(i**(1/3)))


for i in range(T):
    ind += 1
    # for j in range(2, test_cube_root[ind] + 1):
    for j in range(2, test[ind]):
        if test[ind] % j == 0:# 条件で与えられる数字は素数同士の積で表せることがわかっているから割り切れたらそれは素数
            if test[ind] % (j*j) == 0:
                q = test[ind] // (j*j)
                print(j, q)
                break
            else:
                # p = math.sqrt(n)
                p = math.sqrt(test[ind] // j)
                print(int(p), j)
                break
        else:
            pass




# 参考にしたコード
# T = int(input())
# for t in range(T):
#     lst = []
#     n = int(input())
#     for i in range(2, round(pow(n,1/3))+1):
#         if n % i == 0 :
#             if n % (i**2) == 0:
#                 lst = [i, n//(i**2)]
#             else:
#                 lst = [round(pow(n//i,1/2)), i]
#             print(*lst)
#             break

# 11
# 154453
# 76313
# 625759
# 3757
# 3041239736903
# 3297080028589
# 1542202543
# 727699
# 135693
# 3459622062971
# 18







# def make_divisors(n): # iが約数、n//iが約数に対する商
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0: # 割り切れたら=約数だったら
#             lower_divisors.append(i)
#             # print(lower_divisors)
#             # print("lower_divisors",i,n//i)
#             if i != n // i: # 対象の数字を約数で割ったときに商が一致しなかったら
#                 upper_divisors.append(n//i)
#                 # print("upper_divisors",i,n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]


# def make_divisors_original(n):
#     divisors = []
#     i = 1
#     while i*i <= n:
#         if i == 1:
#             pass
#         else:
#         # if is_prime(i):
#             lower_divisors = []
#             if n % (i*i) == 0:
#                 lower_divisors.append(int(i))
#                 lower_divisors.append(int(n/(i*i)))
#                 # print(int(n/(i*i)))
#                 divisors.append(lower_divisors)
#             else:
#                 pass
#         i += 1
#     # print(lower_divisors)
#     # print(upper_divisors)
#     # divisors = ' '.join(divisors[0])
#     # return print(*divisors[0])
#     return divisors[0]

# # for i in test:
# #     print(make_divisors(i))

# for i in test:
#     print(*make_divisors_original(i))
