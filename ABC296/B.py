# width_name = ["h","g","f","e","d","c","b","a"]
# height_name = ["1","2","3","4","5","6","7","8"]
width_name = ["a","b","c","d","e","f","g","h"]
height_name = ["8","7","6","5","4","3","2","1"]

for i in range(8):
    S = list(input())
    for j in range(len(S)):
        if S[j] == "*":
            print(width_name[j]+height_name[i])
