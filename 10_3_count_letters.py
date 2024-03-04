import string
abc = {}
lst = []
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.lower().strip()
    line = line.translate(str.maketrans("", "", string.digits + string.punctuation + string.whitespace))
    for i in line:
        abc[i] = abc.get(i, 0) + 1

lst = (sorted(abc.items()))
for k,v in lst:
    print(k,v)