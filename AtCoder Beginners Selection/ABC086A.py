a, b = map(int, input().split())
a_b_product = a * b
mod = a_b_product % 2
if (mod == 0):
    print("Even")
else:
    print("Odd")
