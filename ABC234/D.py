import heapq
N, K = map(int,input().split())
P = list(map(int,input().split()))
P_sort = sorted(P,reverse=True)
Ps = P[:K]
heapq.heapify(Ps)
Ps_k_max = Ps[0]

for i in range(K-1, N):
    if i == K-1:
        print(Ps_k_max)
    else:
        if P[i] > Ps_k_max:
            heapq.heappop(Ps)
            heapq.heappush(Ps, P[i])
            Ps_k_max = Ps[0]
        print(Ps_k_max)
