N = int(input())
A = list(map(int, input().split()))

born_list = [0] * 2 * N
born_list.extend([0])
count = 0

for k in A:
    count = count + 1
    born_list[2 * count - 1] = born_list[k - 1] + 1
    born_list[2 * count + 1 - 1] = born_list[k - 1] + 1

for j in born_list:
    print(j)

# for i in A:
#     born_ameba_1 = i * 2
#     born_ameba_2 = i * 2 + 1
#     bin_born_ameba_1 = bin (born_ameba_1)
#     bin_born_ameba_2 = bin (born_ameba_2)
#     bin_born_ameba_1_len = len(bin_born_ameba_1[2:]) - 1
#     bin_born_ameba_2_len = len(bin_born_ameba_2[2:]) - 1
#     if i == 1:
#         print (0)
#         print(bin_born_ameba_1_len)
#         print(bin_born_ameba_2_len)
#     else:
#         print(bin_born_ameba_1_len)
#         print(bin_born_ameba_2_len)
