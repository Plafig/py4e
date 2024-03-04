#: Read and parse the “From” lines and pull out the addresses from the line.
fhand = open("mbox.txt")
dct = {}
for line in fhand:
    if not line.startswith("From "): continue
    line = line.strip()
    words = line.split()
    em = words[1]
    dct[em] = dct.get(em, 0) + 1



srt = sorted([(v,k) for (k,v) in dct.items()], reverse=True)
print([(k,v) for (v,k) in srt][0])