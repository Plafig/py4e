'''Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary'''

def read(filename):
    auth = {}
    sor = []
    newdict = {}
    fhand = open(filename)
    for line in fhand:
        if not line.startswith("From: "): continue
        words = line.split()
        word = words[1]
        #print("Debug: ", word)
        auth[word] = auth.get(word, 0) + 1
    return auth




t = "mbox.txt"

print(read(t))

