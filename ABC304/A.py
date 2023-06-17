N = int(input())
st = []
value = 10**9
cnt = 0

for _ in range(N):
    s,t = input().split()
    t = int(t)
    st.append([s,t])
    if t < value:
        value = t
        ind = cnt
    cnt += 1

for i in range(ind,N+ind):
    print(st[i % N][0])
