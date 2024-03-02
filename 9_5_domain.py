'''Add code to the above program to figure out who has the most messages in the file. '''

def read(filename):
    auth = {}
    maxim = None
    fhand = open(filename)
    for line in fhand:
        if not line.startswith("From: "): continue
        words = line.split()
        word = words[1]
        wor = word[word.find("@") + 1 : ]
        #print("Debug: ", wor)
        auth[wor] = auth.get(wor, 0) + 1
        for c, i in auth.items():
            i = int(i)
            if maxim is None:
                maxim = i
            elif i > maxim:
                maxim = i
                key = c
    print("Debug: ",key, maxim)



    return auth




t = "mbox-short.txt"

print(read(t))

