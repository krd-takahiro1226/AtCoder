N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A_mx = max(A)
ans = False

def index_Multi(List,liter):
    #Listはリスト本体・literは検索したい文字
    index_L = set()
    for val in range(0,len(List)):
        if liter == List[val]:
            index_L.add(val+1)
    return index_L

mx_ind = index_Multi(A,A_mx)

for i in B:
    if i in mx_ind:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")
