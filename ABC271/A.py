N = int(input())
base_16 = hex(N)

if len(base_16[2:]) == 1:
    ans = "0" + base_16[2:]
else:
    ans = base_16[2:]

print(ans.upper())
