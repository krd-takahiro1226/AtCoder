N = int(input())
num_list = [i for i in range(1,2*N+2)]
for i in range(2*N+1):
    if i == 0:
        print(num_list[0],flush=True)
        num_list.remove(num_list[0])
    else:
        ni = int(input())
        if ni != 0:
            num_list.remove(ni)
            print(num_list[0],flush=True)
            num_list.remove(num_list[0])
        else:
            exit()
