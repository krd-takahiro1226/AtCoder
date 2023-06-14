N, Q = map(int,input().split())
S = list(input())
shift = 0


for _ in range(Q):
    que_num,que_value = map(int,input().split())
    if que_num == 1:
        shift += que_value
    else:
        print(S[(que_value-shift-1)%N])
