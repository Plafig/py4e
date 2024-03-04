file = input("Enter the file name: ")
count = 0
fhand = open(file)
for line in fhand:
    if not line.startswith("From"): continue
    else:
        words = line.split()
        count += 1
        print(words[1])

print(count)