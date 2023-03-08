N = int(input())
A = list(map(int, input().split()))

even = []
odd = []
max_value = []

for i in A:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

if len(odd) == 1 and len(even) == 1:
    print(-1)
elif len(odd) <= 1 and len(even) > 1:
    even_max = max(even)
    even.remove(max(even))
    max_value.append(even_max + max(even))
    print(max(max_value))
elif len(even) <= 1 and len(odd) > 1:
    odd_max = max(odd)
    odd.remove(max(odd))
    max_value.append(odd_max + max(odd))
    print(max(max_value))
else:
    odd_max = max(odd)
    odd.remove(max(odd))
    max_value.append(odd_max + max(odd))

    even_max = max(even)
    even.remove(max(even))
    max_value.append(even_max + max(even))
    # max(max_value)
    print(max(max_value))

# for i in A_max:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# if len(even) != 0:
#     print(max(even))
# else:
#     print(-1)

# print(result)
