N = int(input())
S = list(input())
T_cnt = 0
A_cnt = 0
N_half = N // 2
N_half_over = N // 2 + 1

def index_Multi(List,liter):
    index_L = []
    for val in range(0,len(List)):
        if liter == List[val]:
            index_L.append(val)
    return index_L


for i in S:
    if i == "T":
        T_cnt += 1
    else:
        A_cnt += 1
if T_cnt >= N_half_over:
    print("T")
elif A_cnt >= N_half_over:
    print("A")
else:
    if max(index_Multi(S,"T")) > max(index_Multi(S,"A")):
        print("A")
    else:
        print("T")
