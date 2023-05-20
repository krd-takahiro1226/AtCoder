from collections import deque
N, Q = map(int,input().split())
cnt = 0
call_list = deque()
done = [False] * N
i = 0

# 受付に行った人をリストからremoveしようとしていた→計算量がO(N)だからTLEする
# doneというリストを作成し、受付に行った人をTrue,Falseで管理することで計算量削減
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        cnt += 1
        call_list.append(cnt)
    elif query[0] == 2:
        done[query[1] - 1] = True
    else:
        while call_list and done[i]:
            i += 1
            call_list.popleft()
        print(call_list[0])
