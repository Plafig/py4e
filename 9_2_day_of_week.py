fhand = open("mbox.txt")
day = {}
for line in fhand:
    line = line.strip()

    if not line.startswith("From"): continue
    else:
        line = line.lower()
        words = line.split()
        #print("Debug: ", len(words))
        if len(words) < 3: continue
        else:
            word = words[2]
            #print("Debug: ", word)
            day[word] = day.get(word, 0) + 1

print(day)

