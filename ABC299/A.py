N = int(input())
S = list(input())
def index_Multi(List,liter):
    #Listはリスト本体・literは検索したい文字
    index_L = []
    for val in range(0,len(List)):
        if liter == List[val]:
            index_L.append(val)
    return index_L

tmp = index_Multi(S,"|")
tmp_i = S.index("*")

if min(tmp) < tmp_i < max(tmp):
    print("in")
else:
    print("out")
