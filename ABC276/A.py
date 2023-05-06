S = list(input())
index_num = [n for n, v in enumerate(S) if v == "a"]
if len(index_num) != 0:
    print(max(index_num)+1)
else:
    print(-1)
