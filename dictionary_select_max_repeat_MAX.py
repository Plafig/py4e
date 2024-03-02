num = [5, 5, 3, 7, 8, 1, 1, 1, 5, 5, 5, 3, 5, 5, 5]

max_key = max(num, key = num.count)
max_count = num.count(max_key)
print(max_key, max_count)