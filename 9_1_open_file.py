fhand = open('words.txt')
text = {}
for line in fhand:
    words = line.split()
    for i in words:
        text[i] = 0

print(text)
