N , M = map(int,input().split())
a = list(map(int,input().split()))

# [::-1]でリストを後ろから取り出す
a = a[::-1]
ans = []
tmp = []
for i in range(1, N+1):
    if a and i == a[-1]: # aに値が入っている、かつi(for文が回った回数)がaの末尾(最小値)と等しかったら
        a.pop()
        tmp.append(i)
    else:
        ans.append(i)
        ans += tmp[::-1]
        tmp = []
print(*ans)


# ↓自分のコード(なんでWAが出たかわからない)
# # 連続しているレをまとめる
# def continuty(a):
#     if len(a) != 0:
#         result = []
#         tmp = [a[0]]
#         for i in range(len(a)-1):
#             if a[i+1] - a[i] == 1:
#                 tmp.append(a[i+1])
#             else:
#                 if len(tmp) > 0:
#                     result.append(tmp)
#                 tmp = []
#                 tmp.append(a[i+1])
#         result.append(tmp)
#         for i in result:
#             i.append(max(i) + 1)
#             i.sort(reverse = True)
#         return result
#     else:
#         result = list(range(N+1))
#         return result


# def check(result,ans,cnt):
#     for _ in range(10**5):
#         if max(ans) == N:
#             break
#         elif M == 0:
#             ans = result
#         else:
#             for i in result:
#                 set_i = set(i)
#                 cnt += 1
#                 if cnt in set_i:
#                     ans.extend(i)
#                     cnt = max(i)
#                 else:
#                     ans.append(cnt)
#     ans.pop(0)
#     return ans


# def main(a, ans, cnt):
#     result = continuty(a)
#     ans = check(result, ans,cnt)
#     print(*ans)

# main(a, ans, cnt)
