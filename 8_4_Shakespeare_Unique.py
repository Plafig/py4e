def shakespeare(file):
    unique = list()
    fhand = open(file)
    for line in fhand:
        line = line.strip()
        words = line.split()
        #print("Debug: ", words)
        for word in words:
            if word in unique: continue
            else:
                unique.append(word)
    unique.sort()
    return unique

print(shakespeare("romeo.txt"))
