num = [5, 5, 3, 7, 8, 1, 1, 1, 5, 5, 5, 3, 5, 5, 5]
dic = { }
max = 0
key = None
for i in num:
    dic[i] = dic.get(i, 0) + 1

print(dic)
for k, v in dic.items():
    if v > max:
        max = v
        key = k

print(key, max)