H,W = map(int,input().split())
A = [list(map(int, input().split())) for l in range(H)]
visited_num = set()
visited_num.add(A[0][0])
