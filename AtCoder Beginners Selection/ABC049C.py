S = input()
# S = "erasedream"
words = ["dream", "dreamer", "erase", "eraser"]
S_reverse = S[::-1]
text = ""
j = 0
for i in range(10**5):
    if (S_reverse[j:j + 5] == "maerd"):
        text += "maerd"
        j += len("dream")
    elif(S_reverse[j:j + 5] == "remae"):
        text += "remaerd"
        j += len("dreamer")
    elif(S_reverse[j:j + 5] == "esare"):
        text += "esare"
        j += len("erase")
    elif(S_reverse[j:j + 5] == "resar"):
        text += "resare"
        j += len("eraser")
    elif(len(S) == len(text)):
        break
    else:
        break

# print(text[::-1])
if(text[::-1] == S):
    print("YES")
else:
    print("NO")
