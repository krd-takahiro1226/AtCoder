A, B = map(int,input().split())

connect = []
counter = 1

for i in range(8):
    connect.append([counter*2, counter*2 + 1])
    counter += 1
# print(connect)

if A<= 7:
    if B in connect[A - 1]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
